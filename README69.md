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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 216348f3-3607-35ed-bfad-7288e36fbc43 | -13.38777 | -51.75365 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 33111654-6907-3056-a7b9-6194dcdd5ecf | -15.65485 | -48.70216 | 2026-09-01 05:18:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21b76a25-457b-3eb7-9ddd-03bd9ca347c8 | -15.49279 | -56.00455 | 2026-09-01 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64c64fdc-c377-322d-80c4-012f0ab72dcb | -14.27793 | -52.89505 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c52d1e6-7b45-337b-ad53-da342140762e | -15.06237 | -47.99031 | 2026-09-01 05:18:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 832602e0-7239-3176-b727-1005b0763c5d | -11.28165 | -50.57122 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 75238a01-0b00-3dc6-acea-e2b20aef4811 | -14.72152 | -53.5933 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a6b9f4d-5ce6-3d6c-a129-ac36c5ea9a76 | -11.25064 | -50.56684 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c5674970-0077-3d74-9bb0-c13eac8f87dd | -14.50847 | -59.834 | 2026-09-01 05:18:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4faa9aa2-fa79-3c00-a124-694cd4642d03 | -9.005 | -65.42942 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64e3a6fb-7248-325d-ad7f-f96390d0d7d8 | -8.86745 | -66.77742 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9421d2c7-8f57-3f34-9a97-e61a16e8a7c1 | -11.30379 | -50.57436 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 21af4226-c43b-335e-903e-12eea7d55274 | -10.51095 | -57.44165 | 2026-09-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfc318ff-ec39-3dea-8929-e25725522f89 | -14.4018 | -52.50711 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5f5351f2-a4e0-3d78-829b-88a7e6f4b6a4 | -14.25882 | -52.88692 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f287d17-d760-3aae-85db-0e1e62fcd126 | -14.45936 | -52.51141 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e6cb66f-a7a6-3591-846f-690e0839f0f0 | -14.39305 | -52.4794 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ccd5446-7519-33ba-b3c5-baf4d88b179d | -15.83131 | -47.67694 | 2026-09-01 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f6b4cac-6a41-3ffe-b5f6-10ee6c69b228 | -15.64792 | -50.10635 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 967455ef-3f8e-3d2b-befb-0bef9cf7e23e | -11.29006 | -50.60797 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9faf4e78-0dda-39f9-8529-af03b4b61a24 | -10.51428 | -57.44218 | 2026-09-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c5f39046-2fb4-3c74-b843-ed282071602d | -14.46927 | -52.52306 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5bc9dcb8-b6f5-3b6f-8282-065594a4e37b | -11.63755 | -49.42406 | 2026-09-01 05:18:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28b3a4eb-dcf4-3546-89d6-fbcec795020c | -11.79326 | -47.67072 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a028a0f4-c081-3f57-b362-0b15e17649a0 | -11.67167 | -47.60857 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5563d52-81a8-3428-9588-565e8bb5405b | -15.63821 | -50.1049 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bba4de4e-c9f1-33b3-810d-84769221f427 | -16.04481 | -54.3805 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b88a2a37-87c1-3b94-b0c6-e3619087ab77 | -11.2754 | -50.58369 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da79c16a-740d-3de8-87d2-e03fdf17d094 | -11.65494 | -47.60945 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 69d286d1-64cb-3d61-81a3-87ca36b8c1d9 | -11.69397 | -54.54311 | 2026-09-01 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 783b392e-c7d1-331f-8df9-8774b558e592 | -15.01102 | -52.76255 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fe9dc1c-7d14-3ea2-9587-c1a85da57536 | -11.68574 | -54.54994 | 2026-09-01 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8577175e-5bcc-3af9-ab87-217782f5e697 | -8.71598 | -67.1115 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13a628f2-4c49-3461-bef1-80c56ea21c12 | -15.87134 | -56.47959 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0e486d5-83d1-300e-95ec-705b932c34f2 | -10.77174 | -54.04519 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b9484ba-fd54-3938-9c99-30bf90e10de2 | -14.46976 | -52.51934 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b7723e87-025c-3db2-87bd-d15aaac4c442 | -14.69028 | -53.59338 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06223a55-f73b-3dd4-acd4-86e9c2a247be | -14.4624 | -52.51939 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b37317ee-fc14-304d-9da0-4d88c3af841b | -14.46187 | -52.52318 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 05fb4a54-e8e4-3b83-ac4c-9bfab50b20a5 | -11.66582 | -47.61105 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce08a157-5483-3e69-b3c0-a0a618af3683 | -10.13775 | -68.58446 | 2026-09-01 05:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bec0309-c84f-3da8-9a65-96afbef1eb46 | -16.04488 | -54.39627 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b115a8e0-db37-34e4-99c2-c696702cc1a8 | -14.38615 | -52.53091 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a67134a-6104-3599-9266-493b51d5e52e | -9.4544 | -67.4621 | 2026-09-01 05:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5191b212-15ff-3c04-a806-3530062c2166 | -15.75048 | -56.1026 | 2026-09-01 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 6df42294-9f46-3051-b040-880cdea8efdd | -14.13468 | -52.80423 | 2026-09-01 05:18:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 728cccd1-8356-3fb6-960f-c40303387c64 | -15.39674 | -53.75698 | 2026-09-01 05:18:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acd2d53b-1fcd-35b3-ae75-322affa29051 | -8.59162 | -66.97328 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16e908ab-987d-3934-b888-67ef41b8aa8e | -14.71972 | -53.57841 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45625a88-f6c6-3823-8132-4250e13c482f | -9.02154 | -65.45731 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47b9efd7-1206-36f6-bc5e-9ad144088849 | -14.39316 | -52.50956 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d66a063-930e-325d-8bc7-6db96408a66f | -15.29932 | -53.18916 | 2026-09-01 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8370c7f3-641e-3877-b9ac-d64abc6098cb | -16.05161 | -54.38626 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 06969ff6-d7ef-30d6-a69b-b4fd094ba4a7 | -14.7312 | -53.58011 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18180284-2f38-352c-967e-3bf512dbbfb5 | -10.94628 | -61.65333 | 2026-09-01 05:18:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 651a4458-619e-3e79-849f-04a1a28a9145 | -11.67124 | -47.61194 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2091533e-9e04-3ebc-8702-17f337890408 | -15.59636 | -56.40989 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb78ccb6-796c-3298-a232-092916aaa8d9 | -9.32077 | -68.89045 | 2026-09-01 05:18:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 223539d4-8dc3-31dd-a27a-3562f7ad08ce | -15.837 | -47.67803 | 2026-09-01 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d1f82ae-8386-35d7-8334-0a07c721758b | -16.04422 | -54.40086 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 076d6126-f38e-3146-8af5-e5a9140309e5 | -15.50656 | -56.00675 | 2026-09-01 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3eb6d8c-c20e-3e06-b5f2-e2d4c7e035ae | -15.62362 | -56.39114 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae866bb6-3b70-3f55-8090-affd3418dbad | -15.64031 | -50.10736 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e7e17d1a-092d-3843-9a3c-2fb7f9d341bc | -10.75643 | -54.00107 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14243ca2-ccbc-3a6a-a81b-ee573afce1e7 | -15.65525 | -48.69872 | 2026-09-01 05:18:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a427b736-b1f8-3943-a37c-38a2eb395dc4 | -11.24768 | -54.0065 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a5664bd-6bd3-33fc-a3a2-074280acf9f3 | -16.04789 | -54.38572 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3669f477-dcaa-3906-bacd-85194fe15d2d | -11.2036 | -55.10632 | 2026-09-01 05:18:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 257d4c19-232e-3982-b51d-3f7b0b8f18ef | -16.54066 | -49.56754 | 2026-09-01 05:18:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cadf194-ce29-39c9-aeb0-d38a79683858 | -15.8685 | -56.4753 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8b69063-1c93-31ab-a2ba-be2ebba11c56 | -15.84716 | -47.69122 | 2026-09-01 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47a50949-c1a5-367d-b0b2-181fa28379e1 | -9.08153 | -65.48535 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3670dc2a-dc7d-39cd-b12a-afdf4ec01415 | -11.04221 | -57.21394 | 2026-09-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7736977-6f22-33fc-9522-cad38f434d36 | -13.47901 | -57.05938 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16cc8f99-a383-3d03-bd2e-9f5cac403b67 | -10.75035 | -54.04189 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8220cb5d-11d4-38b4-903e-d2b8cb6e6b47 | -14.47109 | -52.51665 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d8da090-369a-3f46-9068-cefa51c77ef1 | -14.43541 | -52.50425 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a948d34e-7ee3-37f8-a0d8-6b8c9e038b32 | -8.86351 | -66.77093 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e07e187-7566-3f66-aa4b-23ba59190089 | -11.49915 | -60.58696 | 2026-09-01 05:18:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b2d2d41-ff3c-3729-b9a5-96ffa3c1df20 | -9.02214 | -65.45407 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4608be90-9fe7-310c-810a-9b23ea323d32 | -15.64926 | -50.09573 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6e91f60f-3101-3a11-906b-bc530725b855 | -15.48763 | -56.01558 | 2026-09-01 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5fc2b66-99c8-372f-bc4a-c3f366dc7164 | -14.674 | -53.54169 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 19f183c7-40e4-3b47-aec4-dc13cd5de137 | -15.23177 | -56.353 | 2026-09-01 05:18:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76c3e55a-768d-3845-856f-34b58dec6649 | -15.25249 | -53.88767 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a15d8176-a626-3997-8816-6128acf656ba | -9.02275 | -65.45081 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c03f20d-83bb-329c-9261-a8ac3f171a6c | -8.87068 | -66.88927 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d0a226d8-9f82-37f7-b845-57a2202306d3 | -11.67256 | -47.60167 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09aba9e9-2a36-3c00-b1d0-f83fe45a827c | -14.45829 | -52.51906 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 97cb195c-ce75-3d75-9b20-b102f2c5d63d | -10.75383 | -54.06741 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 160b6c59-e75c-3ab3-bf23-382086b72a65 | -11.30633 | -50.57812 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 5fa5d9d5-e34b-3b2f-a296-a462ac84c02e | -15.75849 | -56.09612 | 2026-09-01 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 9d21f09f-ed74-30a1-a1ee-324636620c93 | -11.28608 | -50.57185 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 42001903-ea44-3a73-8ced-08cd672ced63 | -15.25481 | -53.84443 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 776fe767-79af-37cc-9d00-ffbeeb9e54e9 | -14.38848 | -52.48244 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b72508b-eb59-3523-a5e7-3bc57f52d921 | -11.2577 | -50.58119 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c56c7de9-0486-3339-a936-8dbe266b3772 | -9.0292 | -65.44532 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e317280-37ca-3272-bb27-14db8b1ff086 | -13.4696 | -57.03226 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c489dfa-fc7d-351d-a675-ee4e23241ff8 | -14.26928 | -52.89905 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5236db7b-1c09-3ea8-a204-585ea2fdb31c | -11.17501 | -55.09037 | 2026-09-01 05:18:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README70.md)
