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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4167b71c-d925-3d1d-814f-8441627393d2 | -2.45661 | -46.44717 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a65064a-1eb8-3e8c-a51b-9705f404f2c1 | -2.39318 | -46.72227 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9170b03a-4f31-32ea-a595-3ee7f26997e7 | -2.36671 | -46.54596 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8f9af4e-da1d-367e-8108-232ee9624cd8 | -2.36618 | -46.5494 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1482bede-76c4-3fe3-a236-f9b2b2295fc7 | -2.36341 | -46.54545 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 231e7c94-3f44-3ded-813d-133c1e368030 | -2.36287 | -46.54889 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38bc05b9-e763-30d3-8e65-900de1c8e7e4 | -2.32275 | -46.58427 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c920901-bd92-30cd-a2b7-2e22fcc0d9b6 | -2.31615 | -46.58324 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c9c48c4-1dd8-30ad-bba2-d9d717514dfe | -2.3037 | -46.64106 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26467fde-56a5-3b17-9e68-5a6401df9de8 | -2.29764 | -46.6366 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 878b70e4-6c80-3104-b709-962ee43d0ccf | -2.2971 | -46.64003 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cba6bcc-cb91-3fec-b1c2-22e83bfd2bdc | -2.29488 | -46.63267 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0819fe19-1213-3c6a-bd2c-de943304fda4 | -2.29212 | -46.62872 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 984ca566-f43b-32a2-9642-2adb96d778a5 | -2.28882 | -46.62821 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd9736fc-15e7-3126-b65c-aa20fc907960 | -2.28828 | -46.63164 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 647d6b33-3b7e-3696-8550-a5c30b34c020 | -2.28606 | -46.62427 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff7087ec-8375-35ac-9938-0c68bfb44f3e | -2.28043 | -46.74631 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b482d5ef-aac9-3006-821a-59b471c335a2 | -2.27989 | -46.74973 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fea74c4-8162-35f4-adba-d8541b2ceebe | -2.27821 | -46.73895 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c19180b9-87d9-3cfe-a079-7d60faed8302 | -2.27767 | -46.74237 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3375595-959c-312e-918a-33fb0daf84b8 | -2.27713 | -46.7458 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c05eae0-a017-351f-99ba-4ccfa6cff952 | -2.27652 | -46.72816 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97186657-1baf-3eb8-a56e-69a5cbf42647 | -2.27599 | -46.73158 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1572b710-dfc7-30e5-837f-34d74cbe0710 | -2.27491 | -46.73843 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 365b7796-2037-3dbd-87c7-1a720c9f9ffa | -2.26785 | -46.7619 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ebb6d58-a610-353e-b876-a5e8278fbe1e | -2.26455 | -46.76139 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86b03b0e-1abf-32ee-a35e-6f36d9dff324 | -2.23318 | -46.44004 | 2024-10-24 04:32:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 832f5a85-a3d6-3b99-a02d-3c9a170dab4f | -2.2313 | -46.53828 | 2024-10-24 04:32:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1c2a600-0197-3aa8-884e-84d16c8c342b | -2.21717 | -46.75735 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be8b3947-3078-3faf-b9f5-3fdb7ba0b1fa | -2.21334 | -46.76027 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c60f1fc-4924-3f98-ad44-bceb7ca0a780 | -2.20054 | -46.71267 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b8e293d-7b8a-3bd9-af1f-816925aeedd0 | -2.19725 | -46.71217 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0de0db84-781d-3224-a207-4bbc298f6086 | -2.19395 | -46.71165 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b38340f9-d0b2-3371-98d7-0aa937c6d7dc | -2.19065 | -46.71114 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 168ba76b-9c90-3588-9a49-d10679398546 | -2.19011 | -46.71457 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1eb3842c-dab3-3b72-968e-9aa38432fb39 | -2.18993 | -46.50022 | 2024-10-24 04:32:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cd73473-0184-31a9-9823-91f54288bbd7 | -2.18681 | -46.71406 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9627d345-29b0-39aa-9be8-0883d63dcfb9 | -2.18359 | -46.73461 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c57c7a5-8615-3d3b-87d1-1d23c68c3596 | -2.1819 | -46.72382 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3836ba8c-42ca-3cc7-bc22-6000dcdf056a | -2.18137 | -46.72725 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e40bf5b1-ab54-3334-9764-4ccd1d7c028d | -2.18083 | -46.73067 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0370124b-a73c-38c5-9f22-fa2d7136c461 | -2.18029 | -46.7341 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 668a1c35-9f2d-36db-91b2-29feb2c2a14b | -2.17914 | -46.71989 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd524074-250a-35d0-8c8b-7e47f43d99eb | -2.17861 | -46.72332 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e936de36-70b8-3041-a622-e558e96ce374 | -2.17753 | -46.73017 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ca4a962-f684-33b9-a95e-0eae5c81cfa4 | -3.81847 | -47.50565 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d220019c-ae39-302a-a342-1b0e029d7413 | -3.81571 | -47.50171 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a52b6479-8306-32c5-baf3-7f1dc4bb12b5 | -3.80965 | -47.49724 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 170e4e0f-77ba-32ea-ace4-a3ba70f92386 | -3.80911 | -47.50068 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 521fa650-4353-34b8-a3a1-24898e1fcb9c | -3.80856 | -47.50412 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d259763e-b3a3-360d-8833-bcc192d0fbb5 | -3.80635 | -47.49673 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| deefa585-5f1b-32af-a6de-d726d07bfadb | -3.8058 | -47.50016 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09f47dd3-b32d-3e85-86db-86c64464eca4 | -3.80526 | -47.5036 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00bab756-3aee-3ee7-8f03-e61814bd6f56 | -3.67231 | -47.22623 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddfb6618-3614-33b1-be52-9c60c74d83fb | -3.59868 | -47.26027 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a4cf854-7157-3770-8265-5a31d0bca0c4 | -5.02401 | -47.32714 | 2024-10-24 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 058d5629-8fa7-38fe-86bc-8b7e1f677345 | -4.90721 | -47.6363 | 2024-10-24 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 42066111-7a05-3c2a-a721-84903355a574 | -4.75244 | -47.56223 | 2024-10-24 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e3e700a-972a-381d-aab4-951cf1ad4cdb | -4.7519 | -47.56567 | 2024-10-24 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 493d6c7a-cb47-3f97-9402-2a9c3d95dae8 | -4.59902 | -47.78116 | 2024-10-24 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b30ab1d-31e8-3186-9ec3-7bbffd1f7948 | -4.49013 | -47.08763 | 2024-10-24 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a41db0d-b158-3fbd-bebb-b29a1886c86b | -4.48959 | -47.09108 | 2024-10-24 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f698212-a57b-3b0f-ac71-0ca0172e230f | -4.44049 | -47.76981 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 196913ab-2b4b-3a84-95ef-b431c75bd412 | -4.36967 | -47.48413 | 2024-10-24 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d69f50ea-11ad-3c2c-b9a7-2d0d2c29b6b2 | -4.33867 | -47.59539 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb9e2fcc-1374-3904-b239-f049f92c200c | -4.33591 | -47.59144 | 2024-10-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31c20599-ffa7-3556-95c1-8c9cd39e0d77 | -4.04317 | -46.24329 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6140fd23-6b34-3142-9a6b-1471e781a93e | -4.04263 | -46.2468 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7bdc394-e3cc-3e27-9a05-2e8e07224ab9 | -4.19381 | -46.63081 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c18034cf-37cf-3371-a88b-73d102876343 | -4.18772 | -46.8672 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34da9a14-dd9e-3b40-a2d7-424d48b2ec39 | -4.18272 | -46.85583 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34c19086-36e6-35d1-b858-80f640a8ac9a | -4.18103 | -46.84497 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c07848a7-6c40-35a6-97db-b6526ed00f8a | -4.18088 | -46.80252 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 193cc5e3-cd12-3650-886d-a669e57e44b1 | -4.18034 | -46.80597 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43439829-69b5-3c9c-b253-b6edcfa9b9de | -4.17942 | -46.85532 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2eccfe3-9dc6-3d55-afab-2b4c79fa4742 | -4.17888 | -46.85876 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28548026-419b-3daf-aa46-8c785b5804f1 | -4.17834 | -46.86221 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8eb1694-9423-34fd-a85b-453e84d49b4a | -4.17757 | -46.80199 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfd3adc2-c490-3301-be69-9c8e60e5ddcb | -4.16405 | -46.86705 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42b0662d-7c9f-3414-8be0-0b2ea81a5ca2 | -4.16351 | -46.8705 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 015b6eec-379d-37ca-9390-7f72a4c1affe | -4.16026 | -46.86635 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 085ba28a-d68f-321d-9b8c-2fd4fae32ef5 | -4.15972 | -46.86981 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84035bd2-d023-35fa-932b-bd4a033be8e4 | -4.15191 | -46.83329 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ed2c605-538b-3abe-bafb-6ae3ebd1c526 | -4.15137 | -46.83672 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8db91582-01ca-3db0-9971-9271e15b0f1e | -4.14807 | -46.83621 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 594fad65-5968-3132-bacd-e3710530e727 | -4.12723 | -46.86123 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83a125a0-a91a-3ff4-8d19-139f48d062ee | -4.0154 | -46.53237 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc1833fc-a7f6-3c70-a573-561c1310a0ea | -4.00137 | -46.44753 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f0db45f-aab6-38f8-91af-f0cf45670def | -3.99581 | -46.43958 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba94fc70-ba82-3868-8aa6-423e90a4bc5a | -3.99527 | -46.44305 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33bf2e86-1667-31cf-a335-848364910fe5 | -3.96358 | -46.3846 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e25a679-5e88-331c-ad4b-fb3237996d39 | -3.96308 | -46.40961 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcd24a1b-f45d-3c3f-bf34-a82ee633b2a6 | -3.95976 | -46.4091 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1558da7c-c682-3cd7-bc5a-8fa4508f9767 | -3.95971 | -46.38757 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7c6bd54-b9be-35ef-8713-2645e330176c | -3.95921 | -46.41262 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6ecde60-fc5a-3f55-b465-e7f19ab6bc91 | -3.95862 | -46.39457 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ccc794b-6393-3df2-8fde-5b3dac0e5103 | -3.95475 | -46.39757 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 44d84e97-f806-3fbc-a2a6-f61cf5fcd9c3 | -3.946 | -46.432 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| c5287b79-fc26-3807-8a38-a0504c50b6ae | -3.94545 | -46.43548 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 161d7f01-e67d-309a-b1f7-0ee479721b06 | -3.94322 | -46.428 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |


[Clique aqui para ver as próximas entradas](README30.md)
