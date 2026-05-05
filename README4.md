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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d75b6520-9b69-353a-a59e-790464d88f66 | -11.13312 | -45.14168 | 2026-05-05 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f81be19b-d6f1-323e-994b-8dd87f516bcb | -13.77692 | -47.24639 | 2026-05-05 04:23:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a99c1b33-13f3-3441-8f0e-14b50f528c72 | -11.80286 | -40.08238 | 2026-05-05 04:23:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54e3fde8-9083-3a82-82d4-50bc16041085 | -14.08054 | -47.78716 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6da7d6cc-ee7f-3fde-8865-3e024e28fa6b | -12.32488 | -52.47287 | 2026-05-05 04:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e41deb0-a969-3576-9db7-50873ee307dc | -13.68936 | -55.67814 | 2026-05-05 04:23:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 633abc2c-d899-3822-af50-815261d8dcfe | -13.96506 | -47.51108 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a16ac8ff-248a-353a-bc20-6f90f7b1e111 | -13.93113 | -47.28342 | 2026-05-05 04:23:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0636ddbe-c4a9-3425-bc39-48b57d104a8f | -10.98018 | -45.09922 | 2026-05-05 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92beb9bb-4649-3bdd-8c48-3423762b9c6e | -13.43845 | -43.84375 | 2026-05-05 04:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e5ee9d1-6b9b-3e72-95a2-9e01afec175b | -13.69598 | -55.6725 | 2026-05-05 04:23:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e2d50f3-3c5a-3d24-8de4-22155297f30a | -14.00087 | -56.63067 | 2026-05-05 04:23:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c255e44a-47a3-35dd-9109-5b9e7636c14e | -14.07276 | -47.62344 | 2026-05-05 04:23:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18ecce6e-a710-384a-967e-573255d0168b | -14.03291 | -47.63532 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d4ba2dd-9da1-3dee-bf0d-3169a4a29ad7 | -11.78392 | -43.62097 | 2026-05-05 04:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b1036a2-4b54-326b-8099-44743e99a5e4 | -13.607 | -44.38131 | 2026-05-05 04:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42b91d60-b34f-3741-8aad-e152bc5d5cee | -11.78509 | -43.61324 | 2026-05-05 04:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0bb444f0-c248-3e6c-927c-718670b0d1e6 | -11.88519 | -43.80894 | 2026-05-05 04:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e271c71b-bcba-3cdf-8fd9-ed457bc12508 | -13.43439 | -43.84712 | 2026-05-05 04:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5e31819f-31e4-388e-9522-d89de46a817e | -13.95206 | -47.52745 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe3abb10-ca9e-3c06-843c-8f69c71b37bb | -11.85141 | -55.01791 | 2026-05-05 04:23:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71cf0435-0e12-3384-8fad-566cb855af67 | -13.24126 | -44.46511 | 2026-05-05 04:23:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e97b15e-d1db-362b-970e-767b4918ce86 | -13.90858 | -47.52849 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fe59d45-a909-3762-8a45-e4b1f466ea6d | -14.01815 | -47.62885 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fac47a7c-8c2c-3d2f-9005-62cc6a980319 | -13.97547 | -47.53152 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7936452b-085c-308e-b596-d2c75f4085a8 | -12.42619 | -54.47799 | 2026-05-05 04:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eaa37e74-5481-380f-a288-9f1c05c7c57e | -12.07761 | -44.01603 | 2026-05-05 04:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d45dea0-e9b1-34ce-a1c8-9d7318fd2c77 | -13.24467 | -44.46564 | 2026-05-05 04:23:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10de4034-8709-39b4-9510-d9d5c60c9005 | -10.21118 | -44.76406 | 2026-05-05 04:23:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19b18a7e-6fa2-300f-b797-959bb83a1ee5 | -9.67899 | -47.02788 | 2026-05-05 04:23:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2752ffff-2f1d-3a0f-8694-6d5b9d256f61 | -13.68869 | -55.68151 | 2026-05-05 04:23:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 108d4131-2fa7-3288-af15-4ebe82aba90a | -12.7218 | -55.00252 | 2026-05-05 04:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9226bc9c-388d-3ab6-820e-cc7d3f10547a | -12.27123 | -43.50115 | 2026-05-05 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afac4091-dfa6-3c8f-b2e9-825e8bc0cf66 | -11.61103 | -48.05914 | 2026-05-05 04:23:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 727adade-60e6-3b8f-a3d3-42a94a8383a1 | -11.96465 | -43.97594 | 2026-05-05 04:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89f07609-7c77-3cb8-8e18-983359de0d0c | -14.0833 | -47.79145 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6505a6f3-007b-32ea-9f09-a29f024ee079 | -12.33855 | -50.00343 | 2026-05-05 04:23:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 283c6aef-90ad-3420-ab2e-e4e73259f2d3 | -11.78797 | -43.61764 | 2026-05-05 04:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73713d1e-09e6-3f61-9aa8-cc4979940669 | -9.46786 | -47.79846 | 2026-05-05 04:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4d119f8-d1ee-343a-854e-a7b2e8c10c1f | -14.05062 | -47.65344 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 764786ce-a6ba-3340-b138-3384c03e3dca | -11.79849 | -40.08286 | 2026-05-05 04:23:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 10fc0ae7-90ba-34ef-99a9-c96aef9304d6 | -11.96807 | -43.97648 | 2026-05-05 04:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 610c6fa1-4448-31cd-9ed8-4cda4fdf543f | -12.26714 | -43.50457 | 2026-05-05 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f07558b-e577-32af-9d39-be32c01cd577 | -11.78104 | -43.61657 | 2026-05-05 04:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20f12b4b-c348-35ef-8baf-5e23e4a832ec | -11.79489 | -43.61872 | 2026-05-05 04:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cb55c23-be77-34a8-a8aa-39fba965159c | -13.95876 | -47.52858 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d328a662-f71b-3651-b934-39ed1ec4868a | -13.8636 | -49.89073 | 2026-05-05 04:23:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39c6a136-6f70-3814-8567-c3caeff2fe26 | -13.97272 | -47.52732 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c98d263-676f-3f7f-bd50-990670f85809 | -12.91643 | -49.4857 | 2026-05-05 04:23:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f0dd4ec-bce1-3241-9b55-15e19fd05d61 | -10.58768 | -46.67384 | 2026-05-05 04:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b52d0846-952c-3ad0-bbbe-2f3e1601029d | -14.07992 | -47.79098 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c633d11-15f1-38d3-879a-601b19c088be | -13.68339 | -55.68045 | 2026-05-05 04:23:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee2658b0-eeab-3d05-b6ba-8e07fa85c423 | -13.69069 | -55.67145 | 2026-05-05 04:23:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94e9a4e4-e3e0-3410-9f20-49d2a7253841 | -14.05635 | -47.63946 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17b4317a-de44-30a7-9e7c-39216837c335 | -12.27064 | -43.50509 | 2026-05-05 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5eb1f91a-39d1-3b15-8182-16fdb54a7d83 | -14.04883 | -47.66433 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4d08e13c-f279-3fc0-b2c9-f8e9f9050b56 | -13.86397 | -49.89231 | 2026-05-05 04:23:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bd47fc8-265a-3bc3-9460-cd8a4e30e8c3 | -11.79143 | -43.61818 | 2026-05-05 04:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 923524dc-e24b-3468-9e4b-c7bd1c74e16b | -14.05599 | -47.62063 | 2026-05-05 04:23:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 28579180-0eba-3f5b-a106-b7290cec0751 | -14.08668 | -47.7919 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74cc61c4-84cb-3a6c-9a48-9dffc4ffb4a4 | -12.32327 | -52.48158 | 2026-05-05 04:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31b88b08-f71f-3985-8d20-1e857a66eb34 | -11.1298 | -45.14114 | 2026-05-05 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 07d385b7-2775-35ac-9e09-f4ffce4a824a | -14.05218 | -47.66492 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9cef3b3-0dcc-316a-a16a-7c8178a2b427 | -11.61473 | -47.10151 | 2026-05-05 04:23:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2f51f58-6c52-35f4-b862-691c8db5c11c | -14.03173 | -47.64251 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19ca75b5-cf05-3540-ae69-ca239f92a5cd | -11.94976 | -43.38219 | 2026-05-05 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6902901-1a6d-3cb2-bd86-0dda3912913c | -11.94685 | -43.37776 | 2026-05-05 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d963d5da-e7db-3fb4-a4d9-cd91a04e6b18 | -14.03471 | -47.62435 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34170fd8-7a3d-31f8-91e9-6b220ae62717 | -11.61137 | -47.10094 | 2026-05-05 04:23:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 652aecdd-c051-31fa-8bdb-df6e526dfdfc | -11.79201 | -43.61431 | 2026-05-05 04:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 073c5b7f-1991-352e-a500-4c5ed0eba61f | -12.27473 | -43.50169 | 2026-05-05 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d96c3df2-6182-3980-99f0-4e7cd30e81ed | -11.12924 | -45.12297 | 2026-05-05 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33630151-5804-30b4-be51-7797b5018ea1 | -14.07491 | -47.63135 | 2026-05-05 04:23:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 997e803b-cf8a-3bc7-9b30-bac77724f956 | -11.85205 | -55.01463 | 2026-05-05 04:23:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 679487a0-acf9-34c4-a409-2ed9ebddde85 | -12.7224 | -54.99941 | 2026-05-05 04:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d606dfb0-e190-350c-8aac-925db2d622fa | -14.04141 | -47.62554 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0075f40-f961-3da5-a54a-718d7ec4b9e6 | -11.67037 | -49.00307 | 2026-05-05 04:23:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37067700-9a06-3058-8f05-2089c8916596 | -14.07551 | -47.62769 | 2026-05-05 04:23:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92c10ffe-189d-3e5e-bf3c-90cef18be5bd | -11.84046 | -43.96474 | 2026-05-05 04:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c2008b7-78f6-3493-99da-6317d798bc20 | -13.9278 | -47.28288 | 2026-05-05 04:23:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29feb647-17c8-3239-9b18-261cae20b165 | -12.27486 | -43.50916 | 2026-05-05 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 00234f12-b260-32c1-a396-80537d52c9ed | -12.27544 | -43.50522 | 2026-05-05 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f9d79475-b8f2-34bb-b4e0-70d14f33551d | -12.42563 | -54.48094 | 2026-05-05 04:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab88be5f-6238-3763-865a-1f5b8e97d937 | -10.21173 | -44.76052 | 2026-05-05 04:23:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09c8a177-d69b-36a1-915d-baaf6d5384cb | -11.84388 | -43.96528 | 2026-05-05 04:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 003e524e-2488-3777-bf60-8041c0ae12aa | -10.58987 | -46.67397 | 2026-05-05 04:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b7b61e5-8b25-32f2-8970-a95d065a7e31 | -11.12869 | -45.1265 | 2026-05-05 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94e857d9-597c-30ba-8ec2-7afec173c795 | -11.61449 | -48.05972 | 2026-05-05 04:23:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5a89508-c931-3549-9874-67ea69c293f5 | -14.03625 | -47.63592 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eb0a6bca-90a5-33dd-83e2-9384a89725e8 | -12.39594 | -46.32698 | 2026-05-05 04:23:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6147a2d7-e039-39e4-ba8c-5d4a9cf9c92b | -13.28934 | -43.96189 | 2026-05-05 04:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa257afa-3d37-3236-913a-5bf6750607f0 | -11.13367 | -45.13815 | 2026-05-05 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4dab7637-24f8-3575-bff0-19186462271b | -12.33478 | -50.00276 | 2026-05-05 04:23:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3f7911f4-725d-3f90-9cf0-c84a9d19359e | -14.05278 | -47.66126 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e6ee7b0-7d08-3f38-b75a-ef7be6eea6ab | -11.95035 | -43.37828 | 2026-05-05 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53a555d6-e73e-3d76-99ee-31a115f29407 | -13.95541 | -47.528 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38a32eb6-d4de-3275-b62d-b4752b297d0a | -11.7845 | -43.61711 | 2026-05-05 04:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e20ed936-0a36-3af2-93df-e927cfe5e500 | -13.43497 | -43.84319 | 2026-05-05 04:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 54241a8e-1999-35a1-8da9-4ea176847379 | -11.12592 | -45.12244 | 2026-05-05 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7696f4b-e0be-3d4c-8902-f86245d9217f | -13.28875 | -43.96577 | 2026-05-05 04:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README5.md)
