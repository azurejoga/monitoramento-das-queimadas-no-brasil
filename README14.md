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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 816246fa-77ff-34fe-ae97-db3e28aa2699 | -11.90126 | -57.78892 | 2026-06-16 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 693b637d-d1e9-319a-9ebe-22be447d04e0 | -14.11279 | -59.45452 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| deb54cfc-acf5-37b5-85a6-f281ffa4e0a9 | -14.0909 | -59.45189 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 083d13a0-e1d6-35a2-9f49-b4e53200fe06 | -12.92496 | -54.22543 | 2026-06-16 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f4b81c33-9618-35f7-a4b3-5bc9c263518a | -14.10461 | -59.46148 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 380bcd31-3627-3eaa-b195-0e267b0df023 | -14.10985 | -59.44992 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 059874a4-9cf2-3967-b1bb-75bc1444dab5 | -12.60202 | -52.91474 | 2026-06-16 05:25:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8074ac5-60c1-3f55-95f4-65073809f147 | -12.59679 | -52.91419 | 2026-06-16 05:25:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ee604eb-5f16-37fb-8616-a69b0b74b4d8 | -14.0952 | -59.45182 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e5742f7-e403-3b63-b65e-498ccbbab21c | -12.67379 | -54.58365 | 2026-06-16 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45b78f4a-4cfb-3a29-b1f4-f355ccc4612d | -11.47815 | -57.12111 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b57f7f8e-7f5b-3be7-9b22-be3fa8efe4c9 | -12.60163 | -52.91795 | 2026-06-16 05:25:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e38d43b6-dfa3-3b15-abbc-b159b8222625 | -14.10224 | -59.45286 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| badf4c27-3ded-3ae3-b15b-c93a5780f41c | -7.36644 | -49.86837 | 2026-06-16 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e4792eb-da43-3818-92f0-b9d02021f5d7 | -11.88795 | -55.13467 | 2026-06-16 05:25:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c98a0b28-b6b4-3109-8262-5d287a36320d | -11.47885 | -57.11625 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| caf185fc-454e-3c63-9431-86553ef15d59 | -13.49965 | -56.57796 | 2026-06-16 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb474ff8-f26f-3285-b307-c88890e0e330 | -14.10109 | -59.46094 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d02f040-192b-3af0-8d5a-0280d643542b | -12.92563 | -54.2201 | 2026-06-16 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3516302a-104f-3a6a-9568-ee363e483f70 | -14.1087 | -59.458 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05402c90-2b4f-38cf-9f7b-193b979bad4d | -12.5592 | -57.75846 | 2026-06-16 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 97a4a77d-ae34-3acf-b4ff-b5baf731dd24 | -12.59641 | -52.91738 | 2026-06-16 05:25:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0b63e18-a07e-3b61-8d1b-e14fa3103849 | -11.48411 | -57.10698 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d8c7eab5-2e57-32cb-9486-4e82dfedfc6f | -11.51367 | -56.12883 | 2026-06-16 05:25:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b3d7b1e-3b26-33f9-9e0e-6595b77dc7e8 | -12.67844 | -54.58428 | 2026-06-16 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03d1379e-4715-38ae-88f5-a418cee224f0 | -14.09814 | -59.45638 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3456e03-606e-3b0a-985f-d255e779c319 | -14.10166 | -59.45691 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ea12b37-8201-3db0-8829-8a85527ba275 | -12.80076 | -54.86716 | 2026-06-16 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fefb5cb-2794-36a7-86fa-4d4376d8d84b | -12.90584 | -54.22271 | 2026-06-16 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90bcb091-6a40-325e-90ad-6847f21351cb | -11.91444 | -57.0408 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 743846c1-6540-321d-8d56-0154e584dc57 | -12.05975 | -58.03851 | 2026-06-16 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68e8497e-20a9-3805-a082-8d7d0286fb60 | -11.47954 | -57.11136 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b68212ef-9224-313d-9225-bcb1a0705d36 | -13.65946 | -60.54325 | 2026-06-16 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cf7a74a-654e-37a4-bfac-c2e92fc5091c | -11.90191 | -57.78436 | 2026-06-16 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a45c42e0-2681-3095-af85-cfdf0a9504d4 | -12.91062 | -54.22338 | 2026-06-16 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06661d1d-d9e5-3cd9-b5f6-80b03fe5c40a | -11.48271 | -57.1168 | 2026-06-16 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9297eda0-ed98-3bce-a6cb-b6c4d728d8e7 | -14.10927 | -59.45396 | 2026-06-16 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac0c979d-0623-3c9e-9e57-841f3761916e | -7.81072 | -61.47252 | 2026-06-16 05:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea78a15c-174b-3433-a24d-e2f71b6fcf21 | -11.47902 | -57.11112 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 533a6424-f8e4-353e-b41f-8a09145b3f33 | -14.09881 | -59.45445 | 2026-06-16 05:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 990fac69-99d7-3d05-a981-1325fbf747d9 | -11.48544 | -57.10904 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 12268b28-08e7-3242-b864-0e9fe3918dc7 | -12.80169 | -54.87039 | 2026-06-16 05:59:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd324e69-3d78-30c3-beeb-9440bad30000 | -10.15054 | -56.6073 | 2026-06-16 05:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3b57e6f2-bf02-3a66-a328-1e6f174d139a | -12.91835 | -54.22115 | 2026-06-16 05:59:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ca0a5a5-83cc-3625-b404-e2004ce14a9c | -11.91385 | -55.91353 | 2026-06-16 05:59:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb698972-687c-315f-a3ed-65495ba553e6 | -9.94605 | -65.01035 | 2026-06-16 05:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c16757b-6011-3497-b516-6e0e82a01645 | -11.8988 | -57.78824 | 2026-06-16 05:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bcf55cd-18cf-38bf-b826-b88e3958101d | -14.10921 | -59.45932 | 2026-06-16 05:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 433a3b03-f112-32bd-b7d7-f6d1be735b82 | -10.15694 | -56.6001 | 2026-06-16 05:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16040ecd-b671-3612-a527-4c91fe832a7f | -11.47959 | -57.10657 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42eb35eb-9a36-339a-82ae-41db9aa85fd5 | -10.57679 | -57.31876 | 2026-06-16 05:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29223c97-7ec6-3bf7-9445-94bfade96df2 | -10.57083 | -57.31812 | 2026-06-16 05:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5eaae941-3e52-3689-9a38-7e01fb2abf5b | -11.4788 | -57.11298 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37544858-b163-37e6-8193-8e8a67f0be5c | -11.59071 | -55.34258 | 2026-06-16 05:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c990bac8-5f2e-35ac-a07f-852f8d3d573c | -11.58393 | -55.34173 | 2026-06-16 05:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 04c29007-e1ab-3842-96cc-54ea4209eea6 | -11.58907 | -55.34008 | 2026-06-16 05:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 472f819d-93a9-3e28-8a71-ba9bb266a609 | -10.15637 | -56.60487 | 2026-06-16 05:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8097be7e-37c7-3dd5-87ed-7bd2e12384a7 | -12.9095 | -54.23042 | 2026-06-16 05:59:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dcf919ed-d766-3d22-8447-deb077fb23bd | -10.15732 | -56.60336 | 2026-06-16 05:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e17e01c3-16d8-3e5f-b57e-4b159915a356 | -10.71676 | -56.25002 | 2026-06-16 05:59:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3fe431a0-1f91-39ba-bcca-cebc17e65421 | -11.58835 | -55.34612 | 2026-06-16 05:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 241e912a-0e84-38c5-8eef-78d7a416051b | -10.90241 | -54.13478 | 2026-06-16 05:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6138a423-ab19-337d-a634-2c0831b41974 | -11.47774 | -57.12199 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4108246d-445b-37e8-b696-024036caa1ac | -11.78994 | -56.99997 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4df8f3e2-e056-3cae-b1ea-e201c66fd3bd | -14.10963 | -59.45585 | 2026-06-16 05:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09ede2f0-3c97-3c84-9c77-87152c880bd9 | -11.59586 | -55.34087 | 2026-06-16 05:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93807239-57b7-390e-8e6a-a46ff9851967 | -10.71041 | -56.24913 | 2026-06-16 05:59:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5efb149e-a509-3c9a-b038-87387a729685 | -11.47789 | -57.12014 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| edad9229-4c29-3145-8172-660bbd2e4773 | -11.59819 | -55.33731 | 2026-06-16 05:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d42881b-e272-37ce-b103-d09700ba20fb | -14.10382 | -59.45852 | 2026-06-16 05:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13c3d8c7-9740-3f75-bcc0-08bf64e30643 | -11.79045 | -56.99889 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63195241-e184-3f77-954c-51a05c75d793 | -14.1034 | -59.46199 | 2026-06-16 05:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c750c687-c2d4-337c-b1e6-6c5fa2aa05c8 | -12.91763 | -54.22375 | 2026-06-16 05:59:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9a43a14-ffd9-3184-a8c7-1c2dce853da8 | -10.15019 | -56.60406 | 2026-06-16 05:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 950d5759-acad-32e7-bba2-262b086d31da | -10.15077 | -56.59926 | 2026-06-16 05:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 931f5fc0-1c74-34d2-a550-a7b11eca7dbe | -11.91172 | -55.9191 | 2026-06-16 05:59:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 674c1fa8-3b45-3ce3-92e1-5a789d0bc5ae | -11.5914 | -55.33649 | 2026-06-16 05:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b96c76d-161b-3a5c-8f1f-435544eeacb5 | -14.11503 | -59.45666 | 2026-06-16 05:59:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7302fe4b-93cf-35e5-8d1f-49f6d702a301 | -10.71813 | -56.25071 | 2026-06-16 05:59:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f78e25b3-696b-3e0d-accf-a82162252410 | -10.14994 | -56.61195 | 2026-06-16 05:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 68544db8-fe33-336f-abc5-99088cd3af84 | -11.48512 | -57.11176 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 561b115c-5800-3480-bc33-5ca882221a05 | -12.92568 | -54.22214 | 2026-06-16 05:59:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1adb8ae-1a96-3a8e-945d-2265d0319fab | -11.47933 | -57.10842 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0e6fdb9-eb76-3d64-b399-04b58e6f1129 | -11.78941 | -57.00461 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61a25167-acbc-37a3-a041-c9486fa7f531 | -11.91319 | -55.91919 | 2026-06-16 05:59:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59a42f2c-b502-34c5-a3bb-78b8d43123c1 | -12.80246 | -54.86357 | 2026-06-16 05:59:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fee281fc-4420-3c87-bf2a-23416f7c9520 | -10.71176 | -56.24989 | 2026-06-16 05:59:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5402c3a-fb25-3e31-86b7-a9e116b9ed12 | -10.15113 | -56.6026 | 2026-06-16 05:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3504ad6b-6362-3457-8554-0efa4d7d7fea | -11.79101 | -56.99422 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc8d1262-6c15-3e73-8aeb-4e24ca267c70 | -12.91681 | -54.23149 | 2026-06-16 05:59:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a3ad6bb8-0355-3c8a-87a4-bd4601bf95aa | -11.78988 | -57.00352 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4899a457-f267-3b4b-897f-435a91215d40 | -11.58156 | -55.34529 | 2026-06-16 05:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3360071-a884-3b38-8e74-1c6bb3107311 | -12.91757 | -54.22895 | 2026-06-16 05:59:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70df278c-7565-3fdd-aa4b-4a660c61214a | -11.47846 | -57.11565 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 33ee3352-5bc5-3029-8dae-ee678dae75e7 | -11.91542 | -57.03875 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12ac719f-add1-3538-baeb-e0dac441471d | -11.91235 | -55.91343 | 2026-06-16 05:59:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03c17eb0-a7eb-3287-a48e-c10232461f24 | -10.14963 | -56.60874 | 2026-06-16 05:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ea016e6c-9b30-3b32-ab80-a365f5a8f1f8 | -11.79048 | -56.9953 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f65da03a-3c01-3178-99dd-706efc84a200 | -11.91488 | -57.04344 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c216f1ec-e78e-30a7-a417-f80ed017293c | -11.4857 | -57.10715 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README15.md)
