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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 929d9412-1de0-3406-8ebc-8254dbf5134e | -13.25017 | -47.2445 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e19741b1-36bb-3f39-b3e6-fa2b0c671b53 | -12.64985 | -46.9733 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ddf61e7d-c4c3-3aa2-b07f-1b62b1dd0d00 | -13.1088 | -47.92743 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb5df621-db38-33bc-bfaa-39a3f04edaa8 | -14.67286 | -48.26194 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed087b23-10af-3ad3-8c11-4fde074c6412 | -11.14037 | -47.2127 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c64a5e9e-a96b-388f-8877-21965ce0978b | -13.30006 | -47.82104 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e344a3c-d36e-3f1f-bdec-6f2e219f41ef | -13.25657 | -47.27131 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37c73257-9462-34e1-a5fb-e0d222f8026b | -11.06199 | -47.78395 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 396ced22-54de-3e17-a3a0-8a48e009638e | -10.04852 | -54.33312 | 2025-10-04 04:14:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73807697-0de4-374f-80fd-ec87353f2a3b | -8.62683 | -54.99928 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09a12236-b49f-3bd2-a04a-6b2e53cdb356 | -10.82684 | -57.20089 | 2025-10-04 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 08ca53aa-ecf3-35c8-8ff7-ee7c4c08ea92 | -13.32758 | -47.61898 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d120f3b1-1bea-3064-9da7-20c5eab00654 | -11.44889 | -43.49584 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0eba6b4c-904a-3133-9b87-4d03bf519931 | -9.56561 | -48.68302 | 2025-10-04 04:14:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fcfd614-89da-317c-ad57-0c17b5dd8418 | -13.20464 | -47.80714 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc65388e-9f25-3353-83a8-fe21dbb9b436 | -14.88859 | -48.27391 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be4e7516-2965-3c39-8c4c-e441722f8c8b | -13.74826 | -47.94178 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5720fb24-930a-390e-a5dd-7e795e2f4130 | -9.3288 | -54.53054 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f31448be-6aaf-3a8f-a022-24fecd46e252 | -14.94477 | -46.86873 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44eaa5d0-c43a-3cab-baac-aa7220847d81 | -8.71469 | -44.84115 | 2025-10-04 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e308db4-f25a-3054-9bff-2045b85c412a | -11.51328 | -46.74142 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55555c73-9019-39d1-9dbb-c545e5d59a6d | -8.56335 | -44.64418 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 284c7b09-dad1-3190-b735-5842a96d5682 | -10.76047 | -46.60296 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9459b829-f122-3831-8d7a-e227bd5df81c | -8.6181 | -54.97394 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e367bdb-751b-342c-8f58-1262a6a123bb | -11.56949 | -47.66957 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0240692f-14fb-3f4e-ab93-95d12930b677 | -13.97276 | -48.12016 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c320e9f-5619-39d5-b62c-4b95811a0e82 | -13.31426 | -48.13089 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c062dae9-9a59-3826-a143-e784f0845af8 | -14.63029 | -48.2467 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f1a156e-c2c0-3b86-b009-90e7a0f63b23 | -14.66062 | -48.24626 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9b0de29-10bb-36e0-8aee-50d52b0dc163 | -14.89754 | -48.35201 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0664abfa-0134-30e1-afb7-033ca24f4167 | -13.26574 | -46.47337 | 2025-10-04 04:14:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28230e4b-e134-3b28-8f0e-38267fa215ef | -9.90731 | -43.7989 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 203682f9-e9b3-3b83-8191-b46ad44384cf | -9.94657 | -43.74376 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d84d9e1e-cbca-3ab1-a016-cfd1f83775b7 | -13.12182 | -47.93898 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7c4d96af-7848-3f2b-84ef-4b4950fc5f27 | -14.75212 | -48.14749 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ee31e2d-97e2-351e-b1b9-74c98130667b | -8.90533 | -46.59953 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b76d43a7-f32a-334e-b3ed-4ff186aff290 | -12.8117 | -46.85647 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 43e6452e-1591-3542-b1ef-ce701df58e22 | -13.25093 | -47.26165 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbfecbed-cb94-36db-93ec-43e20bc53b22 | -11.12955 | -47.21102 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c273d140-4fc6-31f6-9d1c-0c2b4609fd8c | -10.98509 | -46.67123 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e34f4d16-17ef-3a23-8d9c-90b0acec9715 | -13.57988 | -48.17697 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 108228e5-837e-3568-b4eb-2848bf10e06f | -11.64122 | -46.86774 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ffcb782d-88ab-3b42-9e17-674074d1859c | -8.53722 | -47.21209 | 2025-10-04 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6d94fc09-2c57-336e-9b71-9c1acdc0d7bb | -11.87139 | -44.97151 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e87043b0-7361-3492-8353-b121f5d79017 | -8.97419 | -46.72963 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc76dc1f-35eb-3584-a904-ae5922236c32 | -11.92088 | -46.39046 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| c37e908c-ae3f-36c7-8510-1c898b71913e | -8.70906 | -47.98098 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 822619af-3dad-34c4-a52c-2ffd7d2a5363 | -11.46911 | -45.1459 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c65dccb-4834-361a-9460-9165ba1edd10 | -13.47976 | -47.23765 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 929ad547-6394-3971-81ea-a1a6a519eac9 | -11.74262 | -54.72107 | 2025-10-04 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69e3d178-96c0-3752-853b-a94e08956eef | -13.97241 | -48.18828 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 7ccd03f2-83e2-3ea4-837f-e8e660b5b91a | -14.94413 | -46.87259 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e92eeb0-4c1a-32ed-8e0c-124c954659d7 | -14.91221 | -46.89548 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb567bda-f8f7-3776-bf95-e1ad932dbaaf | -11.48032 | -45.03431 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fe4456d-40ad-3e92-a488-509e61397ae7 | -14.87182 | -48.12745 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f908d8f-3b69-389a-b881-9b60d16053e5 | -13.13346 | -47.82687 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab73a785-f979-30ae-ab68-8fd9feffed46 | -13.9855 | -48.19978 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d0181bc0-0f40-39a2-b30d-3cbf2c56b8f0 | -11.91958 | -46.39825 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 2bbd725c-5760-3784-8381-4c388a9758bb | -13.13711 | -47.93721 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a0f39d6-5c3b-30a9-bde2-07e2d8192995 | -10.27963 | -44.34253 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f38784f6-68d1-34c5-8685-409725152a25 | -11.15347 | -43.38686 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 33d6cf36-2c24-320f-8971-75fd28e58a07 | -14.3095 | -52.91268 | 2025-10-04 04:14:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2327016-60f6-3630-b226-f588cae2f875 | -8.53321 | -47.83135 | 2025-10-04 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b09f0074-c2f4-303c-b801-6f84d462b1a4 | -13.11528 | -47.86774 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c530acb8-4072-3a54-a324-c090e84e7cff | -14.75358 | -48.13885 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0ce8a87-fb0a-3a1c-a51f-d52169fc4b1a | -11.9159 | -46.37788 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 425fa1f7-55b4-3f4b-a04a-1589548b52bd | -9.33324 | -45.65399 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c4560b3-27b3-36dd-913e-4bc359aaa384 | -8.16954 | -44.13104 | 2025-10-04 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5ae205e-ac0c-3026-946e-d9996bf8714b | -14.92568 | -46.87796 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0cb8483-5e2d-37fb-9fe6-cd3f0e908897 | -11.2473 | -47.79436 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ed7e2a48-ade9-3566-8ab9-6425f60203e9 | -13.17981 | -50.92981 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2950666e-635c-3db4-8d90-36b70ba9e70c | -14.84497 | -48.28586 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8cbde27-26a8-3e46-96b8-d63fcc4740a0 | -13.76012 | -47.82958 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c04fb1e-6736-3323-afaa-a10d76d55620 | -8.39125 | -44.01916 | 2025-10-04 04:14:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abe9e592-9a22-361b-844a-ba5cb70480ed | -8.51695 | -50.03479 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c47a9357-2cc3-3d81-8e84-fb4cc03b4ba7 | -12.0821 | -45.16289 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 771daf56-f26c-3866-b90c-01234e32e9fa | -14.86318 | -48.35564 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 926406a4-03a1-3416-8cdf-a4f85e08a04e | -14.04852 | -53.93015 | 2025-10-04 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82ea40d1-a791-397f-b672-6136c50528e3 | -13.55116 | -47.24496 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8c4425d-e3c4-3c51-8e11-ab3eb8333017 | -11.90486 | -46.36502 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfda8307-cfbd-3684-a4d4-1a61cd9a4b48 | -8.90841 | -49.70674 | 2025-10-04 04:14:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7195982-3103-3cb0-a79d-095ffd7af02a | -9.37447 | -45.85616 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75154edb-f9c5-3f9c-ad37-7aeb01e8c1d2 | -12.38712 | -54.45936 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 53e23dee-ef38-39d9-96fd-93ace355f8bb | -8.1694 | -46.99359 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ddf5f45-8f5c-3418-a41a-496e70f7f65a | -9.89845 | -43.72597 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c742c326-1871-3b40-941c-c9dd73d5c56d | -9.95479 | -43.66998 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 748e66a1-4f6e-3a52-814a-e4ab8ea9afa5 | -15.36367 | -46.28488 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8224e64-9069-318c-8e37-906d5fa40f23 | -8.61624 | -54.98351 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e050539-9855-35e1-9077-b7c8edfa3ebe | -12.59583 | -49.88218 | 2025-10-04 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 462c3eed-3ade-32e9-95e6-ae53fb133d60 | -14.96671 | -47.26334 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7494f9a3-4e76-3df7-aa7e-f73dfc073ac5 | -14.63967 | -48.23549 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 541b80b3-93f0-3e70-8749-f2cd8a0f5df7 | -7.73778 | -46.31644 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| dd253906-4a52-368f-aa67-45286d1ff879 | -12.20346 | -47.7798 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c37ad1da-51e4-30ee-b06f-f8e554cd7ee1 | -10.27484 | -44.33098 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| faabdc1f-b910-3660-b611-489457921ce1 | -13.68565 | -48.04257 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b58d5d6d-1908-3db0-a36f-7d6bac3c4cad | -12.87106 | -44.62447 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e47e1d8d-4cf7-3b37-b8c1-ce1e4cdec43b | -12.21366 | -47.78478 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db920b0a-6a02-3c91-bc15-42c089c7ec01 | -7.73915 | -46.30809 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 32a10f49-d697-3e34-a2b6-778eb8aab66c | -11.91549 | -46.40156 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 1094b6b5-1f4e-3db6-a636-d1fe9ae6efe9 | -8.61482 | -54.96145 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README85.md)
