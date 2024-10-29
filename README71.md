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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca30cef2-18be-366a-b984-c56b01c98131 | -2.31978 | -46.51079 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7890db44-dc67-3372-939e-f5d0cef6f3e6 | -4.50554 | -47.06166 | 2024-10-29 05:01:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3772d1f-8811-371f-aa80-c0713a86ea4e | -2.31808 | -46.14076 | 2024-10-29 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 628e4844-d3c6-3241-b031-66c3e32d1f88 | -2.31518 | -46.50703 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7123482-8766-31cd-8826-a9a08642555a | -2.31435 | -46.67945 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb5379b3-bcb5-34f3-a256-45878a778f55 | -2.31369 | -46.67998 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d985cde-a5c2-3d7b-ae9c-c26633d8002e | -2.31346 | -46.68517 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 485ded8f-c507-30ee-a690-40478f525865 | -2.31289 | -46.14 | 2024-10-29 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c261a2b-3a03-3c22-b277-972ca1e04922 | -2.31285 | -46.6857 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe2d117a-4ad2-35e9-b00d-b5c0b6467e71 | -2.31022 | -46.67303 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ded5c14-8369-3417-b9cc-4541af73c81b | -2.30952 | -46.67353 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fdc5842-e8c6-3767-a2b1-2e3c80f1e06c | -2.30935 | -46.67871 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7aeb671-e6c5-37cf-8c49-e70538a4395c | -2.30021 | -46.67159 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3a00021-335c-30ff-a619-069308fd8399 | -2.27278 | -46.65005 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d903a7a5-f9b1-3b81-92b3-d500b37f2381 | -2.27192 | -46.65573 | 2024-10-29 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db092835-2991-3cda-9a36-a0915a5124a8 | -2.26891 | -46.10755 | 2024-10-29 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0145f32-d5b3-3ca1-8d38-8352848926bd | -2.26844 | -46.11066 | 2024-10-29 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 705187e1-f4f1-362a-9082-4b1e15415be9 | -2.19366 | -46.46354 | 2024-10-29 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0287331d-3ed2-3bfd-8e90-e5a5ef2fc9ba | -4.43746 | -47.61531 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 87bed832-54b3-3ea9-9cf9-b03a85a50372 | -4.43671 | -47.61115 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4a64f23a-b554-3778-a147-1e97df3ff26e | -4.43595 | -47.61646 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9db34bd9-78a0-35ba-bb3b-9e66eafb0bc0 | -4.43262 | -47.61459 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 6d92686e-af71-3973-acdd-be7ea655eb85 | -4.43186 | -47.61041 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 70cde8a8-bd37-329d-bad7-d29ee66ffc5a | -4.43111 | -47.61572 | 2024-10-29 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ae7b596e-0d79-3c28-a7c4-aa7276aeb8d6 | -4.8885 | -46.87066 | 2024-10-29 05:01:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d923d59-a2db-3370-94a7-a5c3a9c9242d | -4.88807 | -46.87372 | 2024-10-29 05:01:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 87b55872-75a9-3cee-95b0-8ee38863ff21 | -4.54186 | -46.60412 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b97ab3ba-c5c6-39e0-b176-446940598c80 | -4.54142 | -46.60715 | 2024-10-29 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| deffc402-8ca3-3e13-bc99-8d20a8d2e06f | -4.50595 | -47.05891 | 2024-10-29 05:01:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e912c630-5ff8-3b6a-b95b-7cd2a3531b84 | -4.50091 | -47.05822 | 2024-10-29 05:01:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f71b102c-62a1-3a5d-bc70-f05599d18adf | -4.50049 | -47.06101 | 2024-10-29 05:01:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 86a8a5c1-f2ac-3ade-9bdf-6397265e21ed | -4.50007 | -47.06381 | 2024-10-29 05:01:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c961dcab-c2f2-3bf4-8ace-209ede572e31 | -4.35133 | -46.78403 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a117f4c4-e5c9-3cd4-bc3f-1b555bb9e5ed | -4.35086 | -46.78728 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 82f9b9a9-04bc-3433-9b3b-5c00b43132cc | -4.34915 | -46.78146 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 392c727a-aa3d-314d-ad21-1b0f21d0454b | -4.34865 | -46.78471 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5551033-6075-3306-b110-3e90bbf8d136 | -4.34817 | -46.78791 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 500cf4cf-4f88-345b-96dd-454402982c55 | -4.34669 | -46.77989 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ba4ca99c-954c-35a4-9dd9-6337c483da74 | -4.34623 | -46.78312 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d14e5d7f-f259-3476-ad6a-6e4e62e87739 | -4.34577 | -46.78636 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a8b76ef8-56fe-3c24-881a-e7a4952ac76e | -4.34403 | -46.78064 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df6abcea-6269-3b40-baac-b506f4503dbf | -4.34355 | -46.78387 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8664108-2934-3ebb-8bee-3c7d63bd447b | -4.34306 | -46.78709 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dff32ad7-2593-3f0d-a71d-21e3f60d0cd5 | -4.21778 | -46.87629 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69ba9a53-28bc-3f19-a765-f98226ef7126 | -4.2154 | -46.87626 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 507c7957-e4a2-3dad-acdd-863c5bfeee9b | -4.21498 | -46.87922 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3c337e6-c9d1-3bb8-92e9-1e3252cd217e | -4.13275 | -46.89051 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 272eed0f-c8f7-3e05-b193-129093fbf46a | -4.13192 | -46.89621 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8000177d-f73a-32ed-ba90-9e505a067d89 | -3.9516 | -46.4034 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a750e429-89d3-3bc3-9062-691ea5c95a1b | -3.9084 | -46.44307 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 182f7c05-6aac-3b0c-b4ae-441e0aa8ab46 | -3.90794 | -46.44621 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3884b55-e555-39a6-972d-e672e8bfbafe | -3.8332 | -46.48228 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d73dcb0-38ee-32c1-861f-75fe0568ced4 | -3.6175 | -47.30029 | 2024-10-29 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b3b0144-c54e-3a39-9731-87b39d735881 | -3.61575 | -47.29581 | 2024-10-29 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24b8ef0f-dd9c-372f-84c8-38e2b7e72315 | -3.61498 | -47.30114 | 2024-10-29 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00bdc9cb-cb97-3dd8-9940-159e6993c028 | -3.61435 | -47.2552 | 2024-10-29 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05145e21-5791-3b66-90a7-cb68fcfc3d30 | -3.61259 | -47.29972 | 2024-10-29 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6d36b4a-e012-3926-b480-58c555b4c7b4 | -3.61008 | -47.30045 | 2024-10-29 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ce73469-740e-36a5-b460-97abfebc92e9 | -3.60771 | -47.29894 | 2024-10-29 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ae02d39-3242-3976-b9f9-5b3509b634fd | -3.60367 | -47.29266 | 2024-10-29 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5771bf6-3991-3447-97ed-93011f616165 | -3.60283 | -47.29819 | 2024-10-29 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8517f832-ea52-3870-9143-ed1df9096325 | -3.58978 | -47.28529 | 2024-10-29 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 289e2c3a-5edd-30d0-b398-1be322104278 | -4.21734 | -46.87923 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8cca554-d483-3f27-964f-9b1e9c93023b | -4.21267 | -46.87576 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f7f9b32-554c-3711-961b-dbd161c0899c | -4.21223 | -46.8787 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74b8d47e-6d6a-3247-bfe8-0271d6d23dfc | -4.13739 | -46.89418 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 705c9dd5-1d0b-390d-bc7e-d82cb933758a | -4.13234 | -46.89334 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8bf960b5-8188-33b4-881c-a4c3d556f9a5 | -3.96151 | -46.40855 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fd89bfc-4d7b-3c53-9d34-2351e3d6540f | -3.95626 | -46.40791 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fc9e201-18f5-3a7a-b374-6ef9c551ef47 | -3.95572 | -46.41153 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 915feafa-c533-34e3-94cc-7f8d48abf6d9 | -3.95108 | -46.40686 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 334b349f-2cc2-33a6-9fdc-976dc2a6f34c | -3.95055 | -46.41043 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a1c5a1ca-0ee6-39af-a52a-2c6bd7a91a02 | -3.91358 | -46.44402 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85d05e1d-337e-37f8-afc3-bf63c68de75d | -3.83273 | -46.48538 | 2024-10-29 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec74cfbf-0829-3e51-8577-bc0306f73dbd | -5.05846 | -47.75466 | 2024-10-29 05:01:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5217f1d4-b1b4-3588-8def-0fd2c46d1929 | -5.0551 | -47.75314 | 2024-10-29 05:01:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a19c496f-253c-312d-9c0b-25f4d01ba44b | -2.11082 | -48.11393 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 094bab17-b9a5-349b-9ff5-6b8ab9fa4da4 | -2.04434 | -48.0279 | 2024-10-29 05:01:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6940ae42-c54a-36dd-b3f5-f163e3026600 | -1.77838 | -47.83868 | 2024-10-29 05:01:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d5d460cf-ebd0-3af0-8955-e0fb8ce23f3c | -1.52508 | -47.2043 | 2024-10-29 05:01:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c99711cc-77ee-37da-9314-f61fe4a1255a | -1.13412 | -48.38371 | 2024-10-29 05:01:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c213ea6-af73-3ead-9768-b4848970e520 | -1.05228 | -47.6409 | 2024-10-29 05:01:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b86072d-d6a4-3f92-bdae-37ea08edf2ff | -2.18236 | -47.94775 | 2024-10-29 05:01:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbde6860-3ab3-3fb8-87b4-5a4723ae7ca3 | -2.18165 | -47.95239 | 2024-10-29 05:01:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ddaa343-494b-3cf5-a702-0db3b7a015ad | -2.18095 | -47.957 | 2024-10-29 05:01:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf0ba76e-506c-38ef-8595-7943d81cdc90 | -2.1778 | -47.94702 | 2024-10-29 05:01:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e4a81f9-df1d-374a-85c6-e3f54a15b29c | -2.17709 | -47.95166 | 2024-10-29 05:01:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41efb1bd-19e0-3e36-b62f-c3c251d35c2d | -2.11008 | -48.11179 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0508549f-13db-3883-8ce9-01331569816e | -1.98441 | -48.68481 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec929e18-fcb8-3bad-9ff4-5a017a3763aa | -1.98008 | -48.68418 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe8b3c23-08f8-3b93-968a-1c5d0b279eb8 | -1.67307 | -47.38889 | 2024-10-29 05:01:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b93c822-9da1-34df-99b4-60091fbf19bc | -1.67173 | -47.38715 | 2024-10-29 05:01:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3ce323b-9177-36c6-8384-4a0bb196eb03 | -1.5243 | -47.2094 | 2024-10-29 05:01:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3c5ba915-effa-36b6-8285-1fbdc6a90082 | -1.12668 | -48.37403 | 2024-10-29 05:01:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78f253d2-4ce0-310a-9d69-c20e389ff922 | -2.1992 | -48.8309 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48425ac4-3326-38b0-ad76-49f9f14dee97 | -2.17548 | -48.72747 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ef6889a-565d-3a49-a21f-a31e12ac7180 | -2.61239 | -47.94567 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8dae61f4-c690-3373-93cd-b7f16951d8fa | -2.6122 | -48.36821 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0c73485-09e0-3f8e-8e0f-b2f2ad3429fb | -2.61214 | -48.32539 | 2024-10-29 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b7eb0bc-9f5f-35e0-b1da-fae8a2b0db0a | -2.60778 | -47.94501 | 2024-10-29 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README72.md)
