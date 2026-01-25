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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5497fe4-2edc-3c9e-826e-2ef7e4c55fee | -19.65035 | -57.25349 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ada8ac10-137a-3132-9f3e-c66924fb4bc1 | -20.34074 | -57.8342 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 07980434-89e2-3f75-948c-cfe5f99f59d3 | -19.6467 | -57.25292 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 77523edf-666e-38b1-a77b-56025ba5a46e | -20.63754 | -51.67543 | 2026-01-25 05:20:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8cee3a57-3965-3757-a47e-bc2e8d09a928 | -18.78885 | -57.65868 | 2026-01-25 05:20:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e07e9872-b01b-3966-952e-4f4d60777d7f | -15.60378 | -59.93966 | 2026-01-25 05:20:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9988639e-adde-35a1-9d6f-242172db55a6 | -23.53842 | -55.50815 | 2026-01-25 05:22:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 48b1036c-480b-34d7-97eb-d9004e1cd36f | -26.02695 | -52.69604 | 2026-01-25 05:22:00 | NPP-375D | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 14e30d67-ae7d-302f-92b9-5d1fd3ec8271 | -26.02728 | -52.69246 | 2026-01-25 05:22:00 | NPP-375D | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c7bee2d7-3358-3455-a275-8ef427a25d0c | -19.6357 | -57.2917 | 2026-01-25 05:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 84b52dab-c399-3f9b-b472-dda9d732767b | -19.636 | -57.2708 | 2026-01-25 05:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.9 |
| d35b8177-a0dd-35a8-9c2c-4d0075465043 | 3.80542 | -60.7027 | 2026-01-25 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb096382-8007-3eda-b14a-4a8acc2d72df | -16.4423 | -58.1695 | 2026-01-25 05:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4979a44b-d274-3331-be83-81d59b57e1dd | -16.4443 | -58.1678 | 2026-01-25 05:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| f08f97b5-b232-3cc3-9678-9a726b7666c7 | -19.6237 | -57.24028 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e81718e5-9bab-3bfc-9d81-27631ead8e55 | -20.33374 | -57.83257 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6b42aea9-0540-3e41-bc4a-042d77d33c7e | -20.3285 | -57.83195 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f20a6303-e245-3860-a0ce-5e2b094efaa7 | -19.62841 | -57.27742 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| de0a400d-c465-3536-971a-b495cab2e5c3 | -18.79465 | -57.65649 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 657f5478-f46d-3cf5-93ef-8aea201b272f | -19.61581 | -57.2647 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 53c3161e-78ed-3dfa-8730-1c0694f674d6 | -18.7943 | -57.65977 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8fa6ebee-0d61-35cc-9738-194808db73fc | -19.64166 | -57.27857 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 80d8c52b-1854-338b-a73e-2bb72a94b68a | -19.64821 | -57.214 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b268a0b5-047f-3c9c-a47f-badc6d073614 | -19.66123 | -57.19359 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e81e5ec6-775d-32fb-8a16-4fe6510e1cda | -19.63418 | -57.27447 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 1a2668f7-61ed-35ca-99f0-2aad6703e8b8 | -19.6428 | -57.21337 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 81b90721-53a8-3ece-b89b-57743f5a9ac1 | -19.64959 | -57.25419 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f084e7c8-60b2-347a-9171-56d4c19faac8 | -16.18239 | -59.33494 | 2026-01-25 05:40:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e196da7a-0bbf-3b54-93a1-f52a6a78d173 | -19.68364 | -57.18886 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2553bd3f-dad2-31df-843c-76a073f0a963 | -19.61617 | -57.26113 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7e72b5aa-7987-3fc5-9b6d-11cb9ef1c1a5 | -19.64244 | -57.21697 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 71f76827-6514-3fea-ac58-295a01150324 | -19.61303 | -57.26843 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 880d8e0b-cda9-390b-b171-b0486af37291 | -19.62803 | -57.28098 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.8 |
| 9d688d20-a606-3af7-9e0a-11d846fc5429 | -19.64202 | -57.27499 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 1df84620-0451-3dba-ae9c-2269e0243ecc | -19.66701 | -57.19061 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 13076874-2c06-3d02-95d5-e39e863de822 | -19.62334 | -57.24387 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6c1b20cc-42a5-34cd-b951-4b191726f7ab | -19.62687 | -57.24108 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ed63684b-c71f-3d61-af27-58942ef53b63 | -19.67859 | -57.18462 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 64431d96-0915-305e-9419-8207515d7041 | -16.18497 | -59.33305 | 2026-01-25 05:40:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07b0cad8-61e8-3488-bbf3-4bd26d35457f | -20.34422 | -57.83383 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8462d7ee-537b-35db-97f4-c589a466ba98 | -19.61841 | -57.26906 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1ad0453c-559a-3a99-b25d-425d8b5823cf | -19.63342 | -57.23093 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 89133de8-816b-3f69-826e-47730553321e | -19.6338 | -57.27804 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 41634d72-3e83-3106-b482-57872beca12e | -19.62012 | -57.27604 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8e41abcb-a09b-38ae-8ed3-3ed83edafedf | -19.6151 | -57.27183 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4cc96a24-8186-3f8f-a6bb-29ced1c5f80d | -20.31768 | -57.83407 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f80e470f-0aa3-328e-abb3-12367b3ea491 | -16.18688 | -59.33551 | 2026-01-25 05:40:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 056fcde4-e74f-314c-96b9-6287c7530521 | -19.64886 | -57.26134 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f68846c6-c0fa-3041-a27d-81b3c53d4451 | -19.61474 | -57.27539 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0a37c508-b6c2-3db2-a612-e96a345a5b0c | -19.65545 | -57.19658 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e54f03a2-f906-37c9-aff2-9192eaa1c287 | -19.61545 | -57.26827 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5c1a67df-9619-3387-a6fd-e26334038757 | -19.61803 | -57.27262 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4b3384c0-cb85-31be-9c64-31539d1fe765 | -19.62726 | -57.23749 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cc9c11c9-260e-3d58-9628-0a77046ffba6 | -19.62071 | -57.24762 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 01810c94-7be0-314f-bff9-719e15a3022a | -19.68401 | -57.18524 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 257fb7b7-b784-328a-bd41-34004de2e849 | -19.6396 | -57.22437 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3a90025d-146f-3c8e-a855-afa01c133705 | -19.63089 | -57.2773 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 6ec0d0d9-646a-3a28-9354-11b4e4ff92b3 | -19.63053 | -57.28086 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.0 |
| ff304d54-c6fb-363b-927c-fc34a88b07e6 | -18.78946 | -57.65586 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a3b6aa4c-1cfa-3859-b9a2-175d215f0eba | -19.66738 | -57.18699 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 851c3016-7cd5-3c0c-b478-98a7d1c156da | -19.63018 | -57.23012 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ff235729-f644-3abe-b0c0-a63497b95ec8 | -20.32292 | -57.83469 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ef21f95a-dd73-3058-9be2-e0d1f5d3c858 | -16.44295 | -58.16389 | 2026-01-25 05:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e95fa16c-8cd2-3d45-81c3-91cee9fdc82b | -20.34945 | -57.83445 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cc16d87f-a37f-3c4a-8e9a-1c4c35f8a05c | -20.33898 | -57.83321 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 507e0cf8-13ce-36f8-88f3-9ceb144eae93 | -19.61341 | -57.26487 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| bcec90f3-635b-36ad-8f09-06562efec5bc | -18.7891 | -57.65914 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f19c75fa-5789-320c-8c62-28e954be8bf6 | -19.67317 | -57.18399 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 06ce9ea1-4e57-3f84-9f5b-7ecd35798faa | -19.61379 | -57.2613 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cafba81f-949b-3a42-bcdd-144ffff72ef6 | -19.62109 | -57.24404 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8a1d7f9f-5192-3d7c-afcc-831602df911b | -19.6616 | -57.18997 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8e56a508-ad30-3613-9e6b-52443d482d08 | -19.63664 | -57.27436 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 3776663e-dd65-3a6b-b2cb-c62b3c925c61 | -19.64038 | -57.21719 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0a9cdaf2-9f67-3502-9f73-78cbe92dc0e7 | -19.61765 | -57.27619 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bfa950d8-9f55-30fd-8c2e-a5001ed1e699 | -19.64923 | -57.25777 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8d19fdc1-d890-307c-a117-771dad7b2df8 | -19.62982 | -57.23372 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 884e4f7b-1fd7-3429-9b5b-9a0ae22afc15 | -19.63628 | -57.27794 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.7 |
| d2b68bfd-6aac-33a5-b035-7d39fc043664 | -19.63341 | -57.28161 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.8 |
| 9e729202-23c3-3b9c-92c4-67cbc9fefab8 | -20.32326 | -57.83133 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 402a24a6-d6a1-35be-9070-ae6ab398a39c | -19.62764 | -57.23391 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d827d559-f181-35f9-b59e-fc43c55d5a65 | -19.63592 | -57.28151 | 2026-01-25 05:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.5 |
| 9148d8c4-d9be-38c4-a134-611b50d8afb3 | -21.35556 | -56.87038 | 2026-01-25 05:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd99b283-1fdb-3ad2-abb9-648600fa8fb4 | -21.35269 | -56.87243 | 2026-01-25 05:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea60296b-7e6b-3872-8e34-d29e19a4cdd6 | -21.35303 | -56.86868 | 2026-01-25 05:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4695ab7a-1305-3378-be67-194e86d0df2c | -3.0603 | -40.1072 | 2026-01-25 05:50:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 59.4 |
| 647f04df-1835-3757-ab75-c01a55d1c584 | -6.05918 | -43.73806 | 2026-01-25 05:54:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| efc030ae-1bdc-3cc3-83bc-f211ddf3087a | -3.0652 | -40.11483 | 2026-01-25 05:54:00 | AQUA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 24c81b43-d444-3a12-9453-22cf8343daf9 | -3.06659 | -40.10545 | 2026-01-25 05:54:00 | AQUA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 48.5 |
| f90190cc-d06d-3cda-bae4-799e6aaf3737 | -3.0603 | -40.1072 | 2026-01-25 06:00:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 60.0 |
| 03cd1766-d5a9-313e-99c6-d5c8c306fd2b | -3.0603 | -40.1072 | 2026-01-25 06:10:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 60.0 |
| f716ccee-4347-3445-8180-2acf701aae0d | -3.0603 | -40.1072 | 2026-01-25 06:20:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 57.4 |
| 7949eeb1-04a8-39b0-9b4e-5e2068a0f42d | -3.0603 | -40.1072 | 2026-01-25 06:30:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 66.7 |
| 2ac669fd-ccec-387b-ab3c-0724cdd85ea9 | -3.0603 | -40.1072 | 2026-01-25 06:40:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 79c5b5ef-a928-3916-a62b-d3fa4e82f533 | -3.0603 | -40.1072 | 2026-01-25 07:00:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 39d236d8-5022-329c-99dc-3b311c1e3560 | -19.6357 | -57.2917 | 2026-01-25 08:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 82911728-0c15-3b00-b871-8e6f7c54caca | -19.6357 | -57.2917 | 2026-01-25 08:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 4fc335a6-5727-3ef9-a121-b3cb2038c7ee | -19.636 | -57.2708 | 2026-01-25 08:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.8 |
| cdfc13c6-b74f-3ed9-8fd9-a1cc03eb2ad9 | -19.636 | -57.2708 | 2026-01-25 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 936fc476-32c1-383e-a78f-cc3b76517c2b | -19.6357 | -57.2917 | 2026-01-25 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.1 |
| 73c2368f-bbad-3bdd-8e92-5955fdddfc23 | -19.616 | -57.2735 | 2026-01-25 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |


[Clique aqui para ver as próximas entradas](README9.md)
