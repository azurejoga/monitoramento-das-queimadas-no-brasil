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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8812475b-e071-3ab3-96a0-c48ecb48a632 | -16.30593 | -45.68678 | 2025-09-04 05:55:00 | AQUA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| de44a9b2-614a-3cbc-bcbf-0971656c488c | -12.95794 | -48.06605 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 837877f6-6624-34a7-983b-f444d1c7e484 | -11.58253 | -52.15879 | 2025-09-04 05:55:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 54d696b7-a4e4-3641-bad6-89f76bd7c578 | -12.90593 | -48.04173 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 04ccf6b5-272f-33ad-85f3-9e2313353266 | -10.42543 | -50.37743 | 2025-09-04 05:55:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ffce3c42-9fd4-3512-8559-1d04214a857f | -15.18028 | -52.34769 | 2025-09-04 05:55:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c156e8f0-8df3-36e3-a058-31495d948d51 | -15.75925 | -49.97827 | 2025-09-04 05:55:00 | AQUA_M-M | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 41.0 |
| e55575ee-595d-3999-ad12-5aac436d7415 | -12.46723 | -48.07846 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 71cedb3c-e149-3f72-93b4-246035cc7178 | -13.84801 | -47.98354 | 2025-09-04 05:55:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4009ac44-69cb-3a40-b6f2-631e727e8b99 | -13.84937 | -47.97452 | 2025-09-04 05:55:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 24247488-7e6f-3246-a25e-e0333bbcc777 | -12.24145 | -50.14495 | 2025-09-04 05:55:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f3e16c42-524c-3a26-8f56-166694f37b6b | -13.74705 | -46.94091 | 2025-09-04 05:55:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 367b5eaf-60d3-3e68-bec0-fa055daf8d1b | -10.49278 | -46.76722 | 2025-09-04 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 414ab19c-1472-3300-9156-9afa57f0f847 | -11.91289 | -46.65441 | 2025-09-04 05:55:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 54227b06-e711-31ca-bf0a-37b3105e103e | -16.30444 | -45.69738 | 2025-09-04 05:55:00 | AQUA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 09117cde-343c-37e3-924d-703b3dcccfa8 | -11.73868 | -47.75279 | 2025-09-04 05:55:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dc9f6782-0233-3ece-8457-8306aba32d4e | -11.66789 | -57.35118 | 2025-09-04 05:55:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 42142261-8553-3a96-be85-dce4ac3b0eac | -11.72986 | -47.75143 | 2025-09-04 05:55:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| f637edf1-9f14-3fc4-a0f3-3065e031d5f3 | -15.02938 | -48.1114 | 2025-09-04 05:55:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 50b7408e-a2c5-3209-af4a-b8a9f74dc58c | -13.57882 | -48.12312 | 2025-09-04 05:55:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 2059dc4b-140c-39da-93d0-3267b22ae270 | -9.72253 | -48.30487 | 2025-09-04 05:55:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 027b5878-779c-359b-ab65-29711afb9caf | -11.59896 | -47.77053 | 2025-09-04 05:55:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 38ef5ca2-54d6-34a1-b334-8a8e72f6593e | -14.60168 | -48.01913 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f6d6ca4-9814-3cfd-bd17-6ad38377711d | -12.94911 | -48.06466 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3dac72a1-d5fe-31a0-b51d-472f60e4abdc | -16.68107 | -40.02262 | 2025-09-04 05:55:00 | AQUA_M-M | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 56.0 |
| 90e172f0-bcbf-3bd9-a0bd-eb3e9f223a18 | -10.99846 | -45.91166 | 2025-09-04 05:55:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 490bf88a-f3c3-3671-9750-cdf5ac0bd6c4 | -14.53989 | -48.05848 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9f257938-fdf6-3e05-9948-21c45a83e85e | -16.31053 | -45.69297 | 2025-09-04 05:55:00 | AQUA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5495cd14-6fed-3c96-81c0-a837127dca55 | -17.17476 | -46.2451 | 2025-09-04 05:55:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c79350a5-3521-33fd-a7cf-3105c372661b | -14.90788 | -49.61908 | 2025-09-04 05:55:00 | AQUA_M-M | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 59fe4dd5-f536-36ee-8109-1238ce607a79 | -17.17334 | -46.25539 | 2025-09-04 05:55:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2313f0c6-404d-39e8-8124-0b8865ada634 | -11.09494 | -45.12214 | 2025-09-04 05:55:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d2a8138e-183b-34fe-a683-14cdb354fa7b | -14.56491 | -48.07159 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e61fee02-6f01-36e3-8d71-c64e6ef6af9b | -11.65125 | -54.5113 | 2025-09-04 05:55:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 52f45c79-aacd-31d9-95a1-c8fb504545f6 | -11.63586 | -52.18961 | 2025-09-04 05:55:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c406284d-da1b-3454-ae93-0f8efa4c5820 | -14.53852 | -48.06751 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e699d22b-1003-36d5-b728-1f797ac89cf5 | -9.61162 | -47.03217 | 2025-09-04 05:55:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 7420f18b-8056-37d9-a39b-9a454f72cf54 | -14.60031 | -48.02817 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d2de225f-6b01-32ff-a7ca-bcd20ca2e9ab | -11.85136 | -51.4529 | 2025-09-04 05:55:00 | AQUA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b1d46cb2-7010-36ed-b353-fd40aaa3828c | -15.01801 | -50.02711 | 2025-09-04 05:55:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0d39d7e0-a6e2-3639-b858-586603e9687d | -12.49514 | -48.07364 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8fe7b3ea-a4a1-31a3-bdf7-c787f9f4cafb | -15.53128 | -48.3394 | 2025-09-04 05:55:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d8834893-ada5-3de4-bd51-814eead41956 | -15.30679 | -52.76371 | 2025-09-04 05:55:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7086d96f-5547-3582-9fff-4d18585e0318 | -11.57891 | -52.11111 | 2025-09-04 05:55:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| ee3e7511-edf8-3134-bb43-c7275848b47c | -15.55274 | -48.39507 | 2025-09-04 05:55:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0caafe01-03e9-3e97-b837-97b736b530d9 | -15.55135 | -48.40416 | 2025-09-04 05:55:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2784f785-3254-38b3-a168-1f398304c8f4 | -15.02731 | -50.02847 | 2025-09-04 05:55:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 17b6fe90-f55a-373b-aa4b-4c45711bf668 | -11.63328 | -52.20486 | 2025-09-04 05:55:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| dfeb84c2-4202-31b3-a9a7-307b0f61f1be | -15.00486 | -50.07077 | 2025-09-04 05:55:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a0602e64-ffc4-3a91-bf9a-fc19be949440 | -14.59289 | -48.01774 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| eb18016e-50a8-3b57-8f7b-08eae222e6db | -11.0374 | -45.1382 | 2025-09-04 05:55:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b75e0121-3588-34c2-a919-09c13869a6dd | -13.86021 | -47.97367 | 2025-09-04 05:55:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| feac0ac7-e7ee-3e3b-8e42-b00f1153f82c | -12.46584 | -48.08754 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f311a9b8-ba8a-3866-8fcc-04cd9df6f0c4 | -11.248 | -44.95893 | 2025-09-04 05:55:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7fe07235-18d3-3c8b-a97b-6815bbc25fb0 | -12.49654 | -48.06453 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 64cfeba9-6844-3a40-832f-e27d76df88c9 | -13.10452 | -57.09412 | 2025-09-04 05:55:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| fde83a6e-021f-3fb1-bbed-7613895bd907 | -14.55611 | -48.07026 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 37f733ca-10a5-3bb9-bb4b-961401fdf1eb | -12.86459 | -48.01672 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 349f6f0f-9880-3b33-aebb-c8e94f9f5114 | -18.20426 | -49.7179 | 2025-09-04 05:55:00 | AQUA_M-M | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f99942da-507d-32f6-bb14-5ce0331f3b1c | -12.47607 | -48.07989 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0d2aa07c-8e5d-3e10-b634-4174fa5663a1 | -9.60283 | -47.03084 | 2025-09-04 05:55:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6fa6e67c-7fc7-31b7-884c-a63824b92d88 | -14.20264 | -48.08239 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 28255029-50ca-3a8f-9d80-73623bb68609 | -13.28402 | -46.81501 | 2025-09-04 05:55:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| faad5a30-8d3b-376f-8014-79aabb35eae8 | -11.59758 | -47.77954 | 2025-09-04 05:55:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 598d4165-df21-3938-826f-0e113b0338c4 | -9.62041 | -47.03349 | 2025-09-04 05:55:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8a8c7df5-fd68-3418-953c-2275b0662c26 | -15.57461 | -50.31495 | 2025-09-04 05:55:00 | AQUA_M-M | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cbfdfee8-55bd-353c-8a34-a8da9a5c50ee | -15.627 | -51.25543 | 2025-09-04 05:55:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cd3ba9eb-b8fe-32cc-a63e-8236ed4afef0 | -10.96672 | -49.75392 | 2025-09-04 05:55:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 1fea8d6a-b980-3276-97ec-9ce7670ba286 | -14.59153 | -48.02677 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7cc2ad19-c57b-3feb-b250-96aea2216343 | -10.10873 | -46.24245 | 2025-09-04 05:55:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 55abc95d-5180-3925-bd0c-73fcfcbc7c40 | -9.61028 | -47.04103 | 2025-09-04 05:55:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5a48a402-56a3-3617-a896-9907993f6d17 | -15.56154 | -48.39644 | 2025-09-04 05:55:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4f66bc54-9c42-3333-8f24-94e05f130dfd | -14.56796 | -49.13898 | 2025-09-04 05:55:00 | AQUA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5aa4ac31-77c7-3a03-a241-6b51ac98cfa4 | -14.59425 | -48.00875 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d1bd0c22-428e-38f2-9527-90c3b1854fe1 | -9.47873 | -47.60684 | 2025-09-04 05:55:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 656903d0-b3a4-3dd8-a6fe-b02871959f2d | -9.7211 | -48.31417 | 2025-09-04 05:55:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 96c9e3b2-e425-3dc9-ac22-daff75684fda | -14.54125 | -48.04944 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bca1897b-0f32-3447-a32c-a735cbbb240d | -11.0544 | -45.40292 | 2025-09-04 05:55:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d03c7834-70ae-3ec6-8a14-1af2f60e55ca | -10.98475 | -46.82412 | 2025-09-04 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9aa07926-58a0-34ed-8340-9fdae275ca3d | -12.90455 | -48.05085 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ffd46d72-cff7-3fca-9d82-663a886e40bd | -10.42731 | -50.36552 | 2025-09-04 05:55:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8b65bffb-23e9-3dfe-9176-c1fee97c501f | -10.98209 | -46.84186 | 2025-09-04 05:55:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3a3660f3-cb32-3b1a-9684-7c908a8c0bdb | -15.78608 | -48.19352 | 2025-09-04 05:55:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 95e838d4-db84-3df6-b742-50cebafecf2f | -12.50539 | -48.06583 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 28bb4749-ea0b-3935-bc4f-eab11bcf5315 | -18.20279 | -49.7274 | 2025-09-04 05:55:00 | AQUA_M-M | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0d539e33-48f3-30db-a4e0-699bad89b110 | -15.76081 | -49.96835 | 2025-09-04 05:55:00 | AQUA_M-M | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 0b0b5649-df43-344f-b418-cc080f8de8fa | -10.64613 | -44.83437 | 2025-09-04 05:55:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e68309a2-b32d-37a3-86d9-f06838c81736 | -11.61662 | -47.77323 | 2025-09-04 05:55:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d6528c7e-31ea-30a8-9b7c-521acd8f2363 | -12.45838 | -48.0771 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 62d1789a-2a1f-3819-982c-2e1529e04a87 | -13.7382 | -46.9396 | 2025-09-04 05:55:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4dd8d3a1-2741-3bac-a9a3-03ec71e63075 | -15.03075 | -48.10236 | 2025-09-04 05:55:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 25177771-7084-3a5e-b207-babef7b574da | -11.05392 | -45.14621 | 2025-09-04 05:55:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| dda5a5a7-86b8-3a5e-9f62-838b49ac8ffc | -12.457 | -48.08613 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 7a2b5901-1406-3387-a401-87223c9fbf0a | -20.1005 | -50.00671 | 2025-09-04 05:57:00 | AQUA_M-M | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| ea955ef8-c1c1-33d8-82b1-f3c3a4d57431 | -22.64896 | -43.68616 | 2025-09-04 05:57:00 | AQUA_M-M | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 34.9 |
| 9cb801ed-91b2-3d61-9979-32f7c8f0076c | -22.28054 | -52.04323 | 2025-09-04 05:57:00 | AQUA_M-M | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 15c99400-192c-334c-8032-73ab15c1b2a7 | -22.66088 | -43.68861 | 2025-09-04 05:57:00 | AQUA_M-M | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 45.3 |
| 10dc32ac-632f-3a1a-847e-19363955387f | -20.10197 | -49.9972 | 2025-09-04 05:57:00 | AQUA_M-M | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ad86661f-5b98-3acd-9212-e9bacd49d58f | -22.46397 | -47.54807 | 2025-09-04 05:57:00 | AQUA_M-M | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 627c80a0-dc4f-31ea-af99-d0ed1568b69d | -20.28882 | -46.70546 | 2025-09-04 05:57:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |


[Clique aqui para ver as próximas entradas](README94.md)
