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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 559fe71e-aa7a-3783-bea7-2da6904a17aa | -2.73874 | -46.74475 | 2024-10-11 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 109f6e03-a050-3a65-9caa-585ce90ef65d | -2.71917 | -46.71616 | 2024-10-11 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 618cfb41-2c9b-35c5-8e3a-97063b545b39 | -2.71582 | -46.71563 | 2024-10-11 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b678ba2-29c3-33eb-b0c9-d7c4caa261e2 | -2.63611 | -46.08121 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 064b797b-8749-326d-ae11-99b4be08fae6 | -2.60365 | -46.17932 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c721b02d-5bf4-393c-9744-8bab019b79b5 | -2.59978 | -46.18229 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b0e8923-2a02-300d-9f86-069e54f05407 | -2.59249 | -46.12064 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba566f1-f8c7-3f1c-a9ce-a76036d1e9fa | -2.59194 | -46.12411 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 111ecb29-71ae-3d0c-a062-7534a56d90d6 | -2.58862 | -46.1236 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67792f9f-9141-30a8-b468-29425be76423 | -2.53744 | -46.14766 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3dac201-be2c-31a0-808e-53373f5bcbb6 | -2.5369 | -46.15113 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37a2d016-f630-30fa-9fb1-693e8be2c3ee | -2.53357 | -46.15062 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3defbe8-4792-3d76-b74e-6f27be0b9cb0 | -2.53303 | -46.1541 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 875ab5d2-a102-37bf-b35c-2a788ca2f570 | -2.52971 | -46.15359 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 390af859-ccb5-32f1-99e5-ceec166a2955 | -2.5247 | -46.14213 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce7a4341-6076-3f0c-bb74-e6a9325c4bd9 | -2.52138 | -46.14161 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6ab1d55-1705-31a8-8921-eb14eadb04c9 | -2.51864 | -46.15899 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc20c1a4-aff3-3163-a26c-e1aa3331f192 | -2.51532 | -46.15848 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57346d12-dacb-39e9-b4e3-1c57ea1bd4b6 | -2.51255 | -46.15448 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2e3a344-562e-3a14-a84e-b206f58820da | -2.50977 | -46.15048 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72940ca1-2dab-3e0a-b7c6-67ef0fa29da7 | -2.40759 | -46.75524 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9f38e4e-c727-3ee4-aaa8-7cb998f2ab9c | -2.39755 | -46.70973 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b553c60-98a1-3dd8-b640-0491eeefb0e5 | -2.39698 | -46.7133 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b8aa97f-4c5f-3e85-93fb-f55b4934ebbc | -2.39419 | -46.70921 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fd4f573-6410-38fe-9645-bf16c4976614 | -2.39362 | -46.71277 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d1ff8b6-74db-3238-9aa4-7f4c7f31e4d4 | -2.39026 | -46.71224 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 953785fb-0024-3ffc-9daf-60284641fcbd | -2.35295 | -46.8385 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9277eba3-5725-3567-911f-864c6577e998 | -2.34958 | -46.83796 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2702b076-a0a1-322f-8902-176721dd8b58 | -2.34621 | -46.83741 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c31bf572-76de-3278-9985-10b2e76e6f4f | -4.47479 | -47.73887 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dde58d97-dfa5-34d9-acfc-909bca7a2c2b | -2.34169 | -46.84407 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1249f86c-bfa4-3240-8835-3eac58923d0e | -2.33844 | -46.4605 | 2024-10-11 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4c26646-7be2-310b-8a86-3e8779b09ed9 | -2.33568 | -46.6743 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fe68e95-c229-3630-9c99-a8d07fbc3c34 | -2.3351 | -46.45998 | 2024-10-11 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd6b4290-36a9-33cf-9054-c3ef0cff108e | -2.33231 | -46.67377 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7124d527-debc-34e6-998b-52e2cb0e4513 | -2.29216 | -46.97332 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33619dfc-8fad-38ac-90e5-683766ac6c75 | -2.24758 | -46.73001 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9839fa19-8db6-3606-b0c9-7b908d16d7dd | -2.24473 | -46.74788 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5966f621-701b-3d86-8b76-1d731735d43c | -2.24421 | -46.72949 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d87bbb4a-61d0-35c9-8fbd-c1d3108a9ff0 | -2.24416 | -46.75147 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fffbd785-fbb1-3246-a284-74e362994ef1 | -2.24307 | -46.73662 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66a511a8-0862-3dbc-9f93-bafb9c432c63 | -2.24193 | -46.74377 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28bcd84d-9553-314d-a831-4a90a28ca7e7 | -2.24084 | -46.72896 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1d5031a-d26e-3710-8947-1816b88057b1 | -2.24027 | -46.73252 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3acae59-4ad7-3cf3-956c-a4063ef1436a | -2.23971 | -46.7361 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27d4dd6c-b2dc-37fa-a928-2e5a417fff54 | -2.23965 | -46.75811 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6542d9ce-36cf-32df-9c69-6c14c24b92a2 | -2.23914 | -46.73967 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60bd77bf-503f-3bee-8527-6ebb9b73b3cd | -2.23908 | -46.76169 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cb979d7-5502-3671-94ed-454fe71dcd79 | -2.23853 | -46.7331 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bafcabf9-445a-3263-874c-9d80b561a979 | -2.23797 | -46.73668 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08476d1d-5fad-32f1-9975-6a13ee615c22 | -2.23571 | -46.76117 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44f365d9-52cc-3b12-9f73-b9efb2afb2b6 | -3.93163 | -46.44107 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e0610ba-67fb-3cf8-8154-e0767e196d21 | -2.23011 | -46.76483 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa3a7c4d-521b-3d0b-a2e3-81240f39c14b | -2.22955 | -46.76842 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5381c402-8b91-3881-bf3c-1893670ea2c0 | -2.19866 | -46.74522 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dc7f25f-13a4-379e-95e8-97398ba41a16 | -2.19586 | -46.74111 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bfc764b-a470-3552-b6d2-124fb428f93c | -2.19529 | -46.74469 | 2024-10-11 04:23:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c6a1d15-d15f-31b6-babf-8a204143b6e1 | -2.19106 | -46.44538 | 2024-10-11 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5777b78-179a-3737-a9e7-d5662aa2f191 | -3.5865 | -46.45485 | 2024-10-11 04:23:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| baffead0-bf6a-348c-b690-346dcf8dfb3c | -3.36505 | -46.49854 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 524fd638-8b03-3a41-99e2-2493b1979b28 | -3.3633 | -46.49171 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d716e76-9b77-3228-b29b-fe5e4ee5d9c9 | -3.36275 | -46.49522 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac51919a-d105-3b2b-9414-e17e73f7b025 | -3.30227 | -46.07959 | 2024-10-11 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 1525b837-e38e-3e6d-b7a7-7ba5d807726b | -3.29896 | -46.07907 | 2024-10-11 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 913aa960-cb19-3aba-b5e9-69b36dfbaebf | -3.27689 | -46.3492 | 2024-10-11 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fb34b64-90fc-3731-bf4d-50d9535478ae | -3.17665 | -46.46586 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f263f60a-3c94-3d0a-8ad5-c6375bc4500a | -3.06505 | -45.94667 | 2024-10-11 04:23:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c4d4d16-27d0-38f3-ba37-13f904e9e711 | -3.06174 | -45.94615 | 2024-10-11 04:23:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7080341-6c33-3125-a28f-f1cf3c4a2947 | -3.03466 | -46.87111 | 2024-10-11 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb15b559-60db-332e-886f-e01e843aa018 | -2.54083 | -47.22159 | 2024-10-11 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f5179d7-75cb-3e71-8ad9-66c906b7d771 | -2.54025 | -47.22526 | 2024-10-11 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 46d7902f-3467-3b2f-82e7-7533ec38c5ac | -2.53967 | -47.22894 | 2024-10-11 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2191f26c-793a-386b-9bae-74f5fdee0c2a | -2.53908 | -47.23262 | 2024-10-11 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6575128-b08c-31f2-8437-d9cd7ea032fd | -2.53742 | -47.22104 | 2024-10-11 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e8db58f-fe03-3cc6-a012-2fa7e40fe67d | -2.53684 | -47.22471 | 2024-10-11 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 99ab1347-4741-383d-8319-c9ca2e402c47 | -4.99442 | -47.36408 | 2024-10-11 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac0dc9af-728b-3d59-9b75-c2163baaad23 | -4.94839 | -47.40503 | 2024-10-11 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ed23d2f-7405-3513-a047-c3e3430b8554 | -4.94501 | -47.40451 | 2024-10-11 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44919e71-a6b3-3f6c-9cee-48eb87516965 | -4.91955 | -47.65345 | 2024-10-11 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f37dd6b-f2d4-3570-9652-937218c9a5e3 | -4.91615 | -47.65292 | 2024-10-11 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52f969db-7c6b-33b8-bc2e-8ce0a4a1f37f | -4.91558 | -47.65657 | 2024-10-11 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e256676b-0e68-344a-a382-5fe1ca6f784b | -4.91275 | -47.6524 | 2024-10-11 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dbb9688-5288-365f-80bc-2c49cda070b9 | -4.65537 | -47.44457 | 2024-10-11 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c890fb6-24a1-365d-bc8e-e42f800ff2b5 | -4.65199 | -47.44403 | 2024-10-11 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8630b030-fef5-3969-a224-ba80e93dafc9 | -4.33299 | -47.31182 | 2024-10-11 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f71831ce-5b3d-333e-88ed-4b5f288ed802 | -4.33241 | -47.31543 | 2024-10-11 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6529c83-2b35-315d-b0c1-66a6f54c5b44 | -4.32681 | -47.30721 | 2024-10-11 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b85beedf-569a-3cf0-8479-2ea83dc5dd1f | -4.32623 | -47.31079 | 2024-10-11 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 862fe995-7adc-3564-92b2-c2be0360d795 | -4.31857 | -47.70694 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cce58a47-6ca2-310c-a5ac-f5bad9db1902 | -4.31516 | -47.70635 | 2024-10-11 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd9ca311-7969-3266-871f-e0497fbf19a6 | -5.14103 | -46.57118 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ba51b34-081e-315f-9798-2d92cfe6242b | -5.14049 | -46.57465 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71de2a50-f833-3619-af0d-fa6a96222314 | -5.0035 | -46.49622 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8e01ad8-1979-3150-a9b2-63dc4c2978c7 | -5.00295 | -46.49969 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce05b895-0142-3fb3-8dec-7ac0c34cff1c | -5.00019 | -46.4957 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d059dd62-d7e0-350d-9d56-08afb1f320b5 | -4.99964 | -46.49916 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46bd7596-53bc-3eae-a6aa-0486c9573209 | -4.99227 | -46.50177 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41f33dd0-afe2-32f1-98b5-c85ba7bc1b61 | -4.91514 | -46.71054 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bf2181e-d706-3416-83e1-faa7c9c916fa | -4.91237 | -46.70652 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d91478e-8858-3428-8d78-c14bd9e09d03 | -4.91181 | -46.71002 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README58.md)
