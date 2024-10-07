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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 943346d4-a8ba-3f4e-b1ad-aa4e8d801ca8 | -21.56194 | -47.73275 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 570a9ebd-c55c-3c8c-a441-5258df5bf84d | -21.56147 | -47.73943 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02a4a59f-58b5-386b-8ff9-926ce188c856 | -21.41498 | -57.22955 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00856d4d-b335-3232-a1f2-cc974c8661cd | -18.10034 | -54.27554 | 2024-10-07 05:21:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bacfd8a-5cf8-3a64-8826-d77c9ca29d28 | -23.04298 | -49.84715 | 2024-10-07 05:21:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 22707d62-2876-3464-9b58-d0ce1b8fbba9 | -23.04255 | -49.85296 | 2024-10-07 05:21:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5fc865d2-a4e6-36d4-a356-e87fae3c8e54 | -23.055 | -51.45245 | 2024-10-07 05:21:00 | NPP-375D | PRADO FERREIRA | PARANÁ | Brasil | 4120333 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e89f5b25-31c5-3954-ad55-abff463137a9 | -23.05462 | -51.45687 | 2024-10-07 05:21:00 | NPP-375D | PRADO FERREIRA | PARANÁ | Brasil | 4120333 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| be3db68e-b0d7-3dcc-8900-7685aebe338c | -19.65833 | -56.4725 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1a1a99a4-6def-3be0-9c52-d3eb34b851e3 | -19.65802 | -56.50746 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f12aad48-781b-356f-a54a-de6ce2cca0a1 | -19.65753 | -56.51128 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4ca0f9fb-7fed-3bb7-8bfb-0bfb623785bf | -19.65735 | -56.48015 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| dde20fd1-94fa-3fd5-9f15-ed3f13bd58e7 | -19.6431 | -56.49369 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b8fc3247-d832-330b-b408-6881ff9f84da | -19.63901 | -56.49311 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ee0f2441-5e7b-364d-90fb-a88ff4fe0cac | -19.58826 | -56.53237 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7a75eb8a-dcf7-3b60-b007-ee4b30161e58 | -19.58418 | -56.53178 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cfa642c6-de81-3df2-92c1-e5deca383262 | -19.58009 | -56.53119 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4dbbb27c-37bb-368f-90f6-046196aa7b44 | -19.57554 | -56.5344 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a4cb1b20-ff64-3152-9477-d5d6423eceb7 | -21.561 | -47.74615 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d862dffc-17e6-371c-84e1-f2a039ad402c | -21.55524 | -47.72483 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec6e068c-c883-33cc-8b11-ce127088330e | -21.55473 | -47.73215 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c14dd41-af59-3d5e-aaa4-e06edc77c42c | -21.55424 | -47.7391 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 618fc248-869a-36cb-87e0-874fea0c7085 | -21.40208 | -57.24596 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ff31d72d-29d4-3842-a491-fcb2f8911ea2 | -21.40144 | -57.25118 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1e87b068-6c60-3a0a-9e4f-891f7b3f4c78 | -21.40076 | -57.24479 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a492406-1b4a-32c2-bd31-61edea7484f5 | -21.40009 | -57.25005 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eb69fc5b-7c27-349b-9d69-8926f1e7c181 | -21.39941 | -57.25528 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 20066e21-65c5-38b0-854f-dfb97ac824fd | -21.39744 | -57.23893 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8777383-37e2-3b6a-819f-d98f61e22e1a | -21.39675 | -57.24435 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f770c3de-83ad-3715-b935-412d6679dc70 | -18.07704 | -54.31309 | 2024-10-07 05:21:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f6996e1-6e8e-3664-9aaf-458aa7cc6332 | -18.07649 | -54.31772 | 2024-10-07 05:21:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f2f030e-d1a0-3025-9319-b91c8d8c72bb | -18.07185 | -54.31728 | 2024-10-07 05:21:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f5be74f8-253f-3ff1-8e2e-da3475a55b32 | -18.19966 | -54.45484 | 2024-10-07 05:21:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 232e779a-a201-3ff7-8b38-14f9be02f35a | -20.50951 | -48.13188 | 2024-10-07 05:21:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b05ba910-c023-3c47-bb0a-0eae6adb6eb3 | -18.59626 | -47.30856 | 2024-10-07 05:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84db2fac-6a0c-3e96-b694-d72694b887fb | -20.51761 | -48.11861 | 2024-10-07 05:21:00 | NPP-375D | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5fdc061c-298d-3d3d-96e0-86c7345cec2b | -20.51704 | -48.12574 | 2024-10-07 05:21:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5e9a93f0-d6cb-3f40-bcdb-16a32304964a | -20.51489 | -48.12333 | 2024-10-07 05:21:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 54951b9d-29d6-380c-a357-15f0639083d2 | -20.51007 | -48.12479 | 2024-10-07 05:21:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e46083f3-ffa7-3614-93c7-8b2cd589e95e | -20.50789 | -48.12272 | 2024-10-07 05:21:00 | NPP-375D | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 32840b56-0d0b-3270-88f4-49ce3fa871c1 | -20.5074 | -48.12949 | 2024-10-07 05:21:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0a10237c-ab68-32da-a656-22a5100ed1df | -20.50687 | -48.13679 | 2024-10-07 05:21:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c8852d97-9f47-3e25-86ac-c75573f174bb | -20.50255 | -48.13085 | 2024-10-07 05:21:00 | NPP-375D | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dbaa9074-84d9-35be-ad63-aff3535e07b6 | -20.50199 | -48.13802 | 2024-10-07 05:21:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 82bc3c1d-aef3-3177-9749-ff6b3586406b | -20.47033 | -47.66463 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc637221-cdde-34bb-bba4-63e88e3355d0 | -20.46978 | -47.6717 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 512e5b8f-6fd5-33b6-a0d6-914b69c7b171 | -20.46924 | -47.6786 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 892f2994-1daa-36e2-9c04-a368f4cdcb67 | -20.46868 | -47.68583 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d188fc77-3c89-32c9-8a25-c1d02e9c7bd5 | -20.46808 | -47.69349 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 48f378ef-bc56-38d6-a1c9-37ba57b6c7a6 | -20.46706 | -47.65157 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b7dd4d6-57a2-306e-a511-4c3e3c1d42f6 | -20.46656 | -47.65866 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77fae64b-c2ee-3c0c-910c-29f7d6f89b8f | -20.46605 | -47.6658 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a40d975f-666e-3ed8-a131-78f973713574 | -20.46554 | -47.67283 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 05682a1c-9e3b-3216-98f9-1dd99d3d50b1 | -20.46505 | -47.67973 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e2740cfb-84bb-3b70-8822-03a68ae15b19 | -20.46453 | -47.68692 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 420631c1-51e2-359f-8d57-49f836ccd352 | -20.46399 | -47.69447 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f03210cf-4d3c-3f99-a651-ed0959464e71 | -20.46366 | -47.65749 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ffbacb7-8853-31ab-8200-bfe2bed1a241 | -20.46311 | -47.66467 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6752719b-bb01-32a0-8cc9-ba2e564d7b7a | -20.46256 | -47.67167 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 86bd1300-7d39-3fa9-8ae8-aa412b4f2bb9 | -20.46203 | -47.67852 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e3ba2297-1a7d-3837-b1b8-88e6ac07c7ec | -20.46148 | -47.68564 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cce36e32-a8fd-3cf6-9fa3-afe5688ffc05 | -20.46091 | -47.69304 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 55fcf9db-7e81-34f6-b381-e833c55b5c15 | -20.45786 | -47.67933 | 2024-10-07 05:21:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60f3d89e-2d6b-3882-b51e-698bef96cc26 | -20.45486 | -47.67797 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c69f86b4-0e0e-39ba-b95f-45b4d9fa762d | -20.4512 | -47.67143 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 457fe8af-d8c6-3858-b2d9-f48cb68e7657 | -20.4507 | -47.67845 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b13dd3bf-c22b-3902-8a5c-715ca959d181 | -20.45018 | -47.68584 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a49a4a31-6f71-35d3-bdc8-839e11449946 | -20.44827 | -47.66983 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b95fbec3-1d0c-3da7-ba5d-59ddedfa539f | -20.44773 | -47.67683 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6452c140-8716-3931-a8f7-98019ababe08 | -20.44716 | -47.68416 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5750af96-b6c7-3282-aa4b-0d879dad5fa2 | -20.44661 | -47.69141 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8334101d-c683-39e7-ab33-faed2d5f95aa | -20.44305 | -47.68461 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 046a9655-3c65-3491-bd7b-cbe05a1a3ee1 | -20.44254 | -47.69183 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d242a1fa-bca2-3f13-9fbd-7472a5ac003e | -20.44202 | -47.69922 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e69f504e-8596-39e1-a225-75099587ade1 | -20.44004 | -47.68292 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 378c86de-7321-37e4-8bd8-4d64dd49bda9 | -20.43948 | -47.69026 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e19e83f7-7bf1-3539-b048-46c6ea10b738 | -20.43893 | -47.69741 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4452744c-b7c1-32ed-bffa-72dd45635cc9 | -20.43833 | -47.70525 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 887563ae-d732-38f5-bb93-ba446f56aece | -20.43542 | -47.69062 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8d968898-265d-37dd-99b4-30b5a588a0df | -20.4349 | -47.69799 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b137997d-8775-3deb-8683-091710c06cd3 | -20.43237 | -47.68892 | 2024-10-07 05:21:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6fef975-b97a-33da-9a89-f70f2cda32c7 | -21.66506 | -47.72984 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3941bba4-36cd-3610-a32f-ca345dbf265c | -21.66451 | -47.73763 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd8c64be-e476-303f-9f20-c703ee54ff5f | -21.65829 | -47.72268 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0135232f-7053-37d2-820f-6b6209a8a19f | -21.65779 | -47.7298 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bee31dca-e64c-344c-92f9-97d4f4729812 | -21.65103 | -47.72259 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e746c9b-46ed-39db-9fc4-31839f1ae5e0 | -21.65052 | -47.7299 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91f14b07-662d-33df-adf5-81991221819e | -21.64378 | -47.72226 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| babb5b3b-b5dd-3e8d-9a96-837a200213ce | -21.63659 | -47.72122 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 425828ff-7a7a-3c64-89b1-1a9696edf1eb | -21.60044 | -47.71838 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e5518f5-0749-321a-965b-720c29b26482 | -21.59993 | -47.72594 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e74df866-9d36-3ed6-b351-f76458287781 | -21.59969 | -47.71292 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ce0b8ff-35e4-327a-ac58-f34b12645c08 | -21.59912 | -47.7208 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f62c5008-2f2f-32dc-8712-ac31cb28f42d | -21.59892 | -47.95462 | 2024-10-07 05:21:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0edbf0b4-96c9-3db8-bf37-b9c8d486d798 | -21.59859 | -47.72807 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60012a41-cbe6-3bc6-a845-7902547e625f | -21.59809 | -47.73502 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d2e6ab0-1806-316b-8762-d94c86bca84f | -21.59681 | -47.94881 | 2024-10-07 05:21:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 73c880e8-e182-3e58-b460-6a7248f39a00 | -21.59627 | -47.95608 | 2024-10-07 05:21:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cece71dd-e15d-3e1d-949f-48f205ae74cc | -21.59362 | -47.71163 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c19e6fe2-d6ec-3427-a604-febb59f0a0a8 | -21.59308 | -47.71972 | 2024-10-07 05:21:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README127.md)
