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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05ee3d25-2b1a-3e0a-8ee9-9dcdc318130d | -10.6793 | -48.6415 | 2025-09-12 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 456b0ae4-a661-3ec4-bd2c-671a512a3554 | -16.3127 | -50.0868 | 2025-09-12 12:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 163.3 |
| a736b6ec-c3d6-30d3-af7d-cca40658dfed | -10.8785 | -45.5597 | 2025-09-12 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| efcf0df2-48c5-38bc-b41d-2ba7125adb5d | -8.9563 | -46.0849 | 2025-09-12 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| e1aebf2e-e4c9-36dc-a49a-5da7daf67d2a | -14.4394 | -47.3206 | 2025-09-12 13:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| fc53189f-1342-3ae1-9fbf-a88158b1ae5c | -10.0943 | -47.1664 | 2025-09-12 13:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 424d9833-fb6d-3acd-bb62-7ea4e0dcf9a5 | -10.8972 | -45.58 | 2025-09-12 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| ff22a837-b410-3826-a80a-cad05b1ee4d6 | -11.5425 | -50.5947 | 2025-09-12 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 24670f4b-527c-3f88-8e4b-f458c50c7eee | -11.429 | -43.5307 | 2025-09-12 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| e9b7d4e5-5851-3b21-abb4-f6d9ce046d2c | -12.9292 | -54.7538 | 2025-09-12 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 787e1d35-a6fc-3a33-b470-4a6beb2b1b40 | -9.057 | -47.0355 | 2025-09-12 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 1f9ac6ee-0c9e-3da7-b7da-576904eb26f3 | -9.72 | -46.8749 | 2025-09-12 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 6a605a19-1fe0-384b-9964-9f257e15603c | -6.1703 | -41.0901 | 2025-09-12 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 632.3 |
| 1581454b-7f2d-30e7-be6f-e2e263224a80 | -12.6628 | -45.3239 | 2025-09-12 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 79cccf13-55f5-3b0e-b9a9-92cc9e42dd91 | -8.4893 | -47.2694 | 2025-09-12 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 2cd06dc9-116e-391a-8dd7-75882553127e | -13.0018 | -46.7341 | 2025-09-12 13:00:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 2efff99a-fab0-3ccd-99c8-fdd70013a05a | -12.0849 | -47.6065 | 2025-09-12 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 320.5 |
| da4e7478-e77d-3a17-a6c1-95c927623b9a | -7.542 | -44.6844 | 2025-09-12 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 23426f62-dcc8-3563-b47f-8afe4df60053 | -8.9566 | -46.0623 | 2025-09-12 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| d95cd433-248d-3c35-a160-59d524fd6f63 | -12.0852 | -47.5842 | 2025-09-12 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 5a333c5f-416d-38b6-9e58-ff4ae26cc277 | -10.2217 | -46.2332 | 2025-09-12 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 0d2359b6-2c75-33fc-b48d-cf1efcdc0782 | -11.4863 | -49.2658 | 2025-09-12 13:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 79c526c6-c398-3d64-a853-7e32b4a1394b | -11.5422 | -50.6161 | 2025-09-12 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 9630f50f-ee14-385f-ab49-a293012e3b99 | -8.9746 | -46.1279 | 2025-09-12 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| b748e96e-9912-3397-b6c0-e7e31b76a0b5 | -8.956 | -46.1074 | 2025-09-12 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| ff580324-f05a-339a-8676-c9de15a5b2a1 | -16.08 | -49.9709 | 2025-09-12 13:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 49428613-d348-35eb-94d2-52b5911652bf | -8.1837 | -46.0965 | 2025-09-12 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f0018b81-8887-3c8b-834b-86fc26e62055 | -12.9101 | -54.7558 | 2025-09-12 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 17be059d-57c7-3004-b955-09310bead83b | -10.1176 | -48.2013 | 2025-09-12 13:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 9363e4f1-d372-3965-9532-4183639b9c5a | -6.309 | -42.2311 | 2025-09-12 13:00:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| da453718-6d70-36b5-aec2-bc01693d9037 | -7.5641 | -44.4068 | 2025-09-12 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| da34db22-abd4-36e6-b433-f9c9e16cff06 | -14.1492 | -45.4009 | 2025-09-12 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1d959d67-7038-36e7-bd85-b2a6836172ed | -14.1907 | -46.2012 | 2025-09-12 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d7f42e2e-91e7-3191-89cb-ff4438ba0376 | -9.0379 | -47.0597 | 2025-09-12 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| d56a1133-f0d0-3b15-a63d-3bc3b6b84d34 | -16.633 | -49.7905 | 2025-09-12 13:00:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 3fe7309e-3f06-3dae-81b4-c1f6751ae0c5 | -11.9713 | -51.164 | 2025-09-12 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 1d45737a-edc5-3db5-9cd4-99c003af06de | -14.1717 | -46.1815 | 2025-09-12 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| c85cb3b9-b346-367b-a8d8-a43c2cb4e01d | -15.1402 | -50.1628 | 2025-09-12 13:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 168.1 |
| d386c86e-53c1-3c76-9c04-d03464d978eb | -7.3212 | -49.6255 | 2025-09-12 13:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| b474674e-1306-32d6-a896-b489ab5ddbea | -9.0373 | -47.1041 | 2025-09-12 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 1d07aae5-5122-3acf-9953-51897a2f9451 | -8.4705 | -47.2712 | 2025-09-12 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| e0110321-7c9e-32f5-aa9e-2013c38a9a8c | -15.1406 | -50.1409 | 2025-09-12 13:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| d7e03648-6dbf-355e-8a8b-3e8c4b24adf9 | -10.8785 | -45.5597 | 2025-09-12 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 2ec3869b-c987-3716-b4ee-b623308685c3 | -8.9374 | -46.0869 | 2025-09-12 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c6d4761d-7c09-360c-b1f7-8783b3307a26 | -10.679 | -48.6633 | 2025-09-12 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| b9b6bf99-8d4d-3fd5-85d4-0f5361942201 | -9.7197 | -46.8972 | 2025-09-12 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 69da7b62-6af0-3051-84ca-b215662427c2 | -7.5455 | -44.3856 | 2025-09-12 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 26c327f8-5a4e-3273-831f-3c6df57b4e0f | -7.5452 | -44.4086 | 2025-09-12 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 916f7d90-c743-38ef-8f2f-0ed37540db64 | -11.4285 | -43.5544 | 2025-09-12 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 1166f904-96d2-3c52-a5ca-bd00efcb37f2 | -9.9004 | -51.8811 | 2025-09-12 13:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 2f16f496-9e55-35a4-9e08-94c59e79c8a2 | -10.7172 | -48.6371 | 2025-09-12 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3082015e-9806-3189-8425-d7ac5ab3bbfc | -14.4588 | -47.3174 | 2025-09-12 13:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 556c9e16-cf3d-33fa-ab49-42478891a7c6 | -6.8369 | -45.6559 | 2025-09-12 13:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 6da3b0a9-b29d-3904-808e-d6f54f946d9c | -7.5643 | -44.3838 | 2025-09-12 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ac7aff36-8df2-3d1d-86fc-01be40a1e831 | -12.1431 | -48.7038 | 2025-09-12 13:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| e618be31-1376-3153-94a2-6727d6df1e8b | -9.0376 | -47.0819 | 2025-09-12 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 2556be22-d59d-3f80-95fa-8ed18d7f6dc1 | -14.3937 | -52.9456 | 2025-09-12 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1480aae3-3d5c-359d-85b8-91ce7041d6e2 | -8.9087 | -49.9433 | 2025-09-12 13:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 32356d52-5fe1-3bb0-b46a-f22025ef2e68 | -6.1891 | -41.0884 | 2025-09-12 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 273.5 |
| 760e7f70-7683-3ade-b42c-ec5f9166dd40 | -14.394 | -52.9245 | 2025-09-12 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| b6becc69-0971-3489-8bc7-638f434cfbd6 | -15.5236 | -48.5332 | 2025-09-12 13:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 352fa6ed-0aaa-3a2c-95ec-4dc556f89d91 | -12.1626 | -48.6793 | 2025-09-12 13:00:00 | GOES-19 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 951b0365-0e14-3f62-b8e9-24953e923162 | -10.1179 | -48.1794 | 2025-09-12 13:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 14fd59d6-edd5-3cac-a899-cb6403a43c60 | -12.6821 | -45.3209 | 2025-09-12 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5a1a7a26-b15f-3316-a582-88e8c8ec0db7 | -10.8781 | -45.5826 | 2025-09-12 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 234.0 |
| 12c0136e-d270-3f0a-a563-1489fab8e468 | -9.6919 | -47.5438 | 2025-09-12 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 0dcae80d-708b-3cfc-b021-0e1958b39f09 | -7.5232 | -44.6862 | 2025-09-12 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f9c6d043-f461-3e30-858e-cc2f32e77fba | -9.6727 | -47.568 | 2025-09-12 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 95201738-e996-3cb2-b896-57031cc9b010 | -16.9621 | -45.8176 | 2025-09-12 13:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 8e8bd32b-62eb-35d1-9440-a2eb2fe7bdbd | -14.2727 | -45.0765 | 2025-09-12 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 4d23a867-5ed5-358c-897f-3014f8e5f17c | -9.673 | -47.5459 | 2025-09-12 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 2cf4977b-b213-3d88-b32d-019c381eda09 | -8.8899 | -49.945 | 2025-09-12 13:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 32d3cf28-755f-34e2-b699-b7a4c1a62e12 | -6.8369 | -45.6559 | 2025-09-12 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3342fc43-1331-357c-b811-b700f57c6f92 | -9.0759 | -47.0335 | 2025-09-12 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| cd49473d-2e6e-3c60-96b4-25b03f94e642 | -11.5053 | -49.2635 | 2025-09-12 13:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b99f0c82-3ce8-3f97-8edd-705f2ae260f5 | -11.4402 | -48.5513 | 2025-09-12 13:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 8e7e7e1d-ee7a-3bba-82a4-7a066153b506 | -9.0373 | -47.1041 | 2025-09-12 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| b32b38af-710e-3512-9a63-a1ad17b7be0a | -8.4893 | -47.2694 | 2025-09-12 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 1d65b724-fb82-3a54-bb7e-4bad7a52274d | -14.4394 | -47.3206 | 2025-09-12 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a806cd30-42a6-35e3-baa2-56d5e63f3814 | -15.1402 | -50.1628 | 2025-09-12 13:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| d992047a-5bbb-37d1-bfea-4e66380af206 | -8.9746 | -46.1279 | 2025-09-12 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b1a6d75a-f0a6-36ef-9553-613506e00fae | -10.8785 | -45.5597 | 2025-09-12 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 250.6 |
| ad0555db-9fcd-39f0-b4e5-928e38b940f0 | -6.5541 | -43.9684 | 2025-09-12 13:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 2c7ff224-ac11-3feb-8b45-bd50fd0ddc62 | -8.956 | -46.1074 | 2025-09-12 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 304.2 |
| bcc46fe2-f994-3328-b6db-a95774274691 | -9.8963 | -46.452 | 2025-09-12 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d3212512-b7ab-35bc-bc9d-c1a01f3238ba | -11.5422 | -50.6161 | 2025-09-12 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| b6c9c9ce-f88c-3e66-a7ec-bc1cd3855e48 | -10.1216 | -47.9154 | 2025-09-12 13:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 7a58007c-6a70-3e16-9d5f-7eb333db21d2 | -10.1405 | -47.9133 | 2025-09-12 13:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 1e80920c-03fc-323b-958c-16c9f723c7e8 | -16.4118 | -45.6963 | 2025-09-12 13:10:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 2a1bc335-f701-385b-b1e1-e0a1e15bff74 | -11.4398 | -48.5733 | 2025-09-12 13:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 288.3 |
| 1ecb0401-774f-3078-86d6-b3a1af4db99f | -9.0376 | -47.0819 | 2025-09-12 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 19262327-3ac5-307d-81b0-15ef6de7e069 | -6.1891 | -41.0884 | 2025-09-12 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 289.1 |
| dd3fb875-c28e-3b6b-a27d-4940a935e5cd | -10.2217 | -46.2332 | 2025-09-12 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 366714e7-407d-3303-a496-8f1e8ec7ef8b | -8.9566 | -46.0623 | 2025-09-12 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 69152c54-6b42-3780-8539-e05f45ada079 | -12.9101 | -54.7558 | 2025-09-12 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 391705dd-1ca0-311d-83c2-df2212e63c84 | -7.5641 | -44.4068 | 2025-09-12 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| f6bdc252-6689-3c56-b886-d2f7d3134b19 | -11.4863 | -49.2658 | 2025-09-12 13:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 7785b7ba-f45a-33c7-9ec7-5d1109eb5d36 | -7.5452 | -44.4086 | 2025-09-12 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 9e334bb6-8a99-3a40-a5b3-000439543d9f | -8.4705 | -47.2712 | 2025-09-12 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| d06dcd10-1b77-398f-b72f-45bbaa5d8845 | -8.8899 | -49.945 | 2025-09-12 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |


[Clique aqui para ver as próximas entradas](README129.md)
