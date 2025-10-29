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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54991e43-c591-309f-ae6f-3bcb2b64b5dd | -13.24382 | -44.11199 | 2025-10-29 03:55:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c8d8deed-f97c-3de2-8e47-bb0f3f46cfd5 | -13.27977 | -47.73112 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdaa02fc-2547-3367-975a-ffe4f8de936b | -12.56493 | -43.96006 | 2025-10-29 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c0e176d-bca8-3cc7-b56d-9989709edb29 | -13.1711 | -48.45203 | 2025-10-29 03:55:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0096ea80-452a-3188-bca7-28e15cba8ad7 | -15.64326 | -42.91231 | 2025-10-29 03:55:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b697393f-0be4-38cc-a484-69d19862c01b | -13.93549 | -48.43573 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3cdff901-b47a-3351-ada3-2dcc41503794 | -12.52786 | -47.55477 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 523f26a8-8d20-3781-89e4-f7ad2cc9c5c3 | -13.90848 | -48.46795 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec7f91f5-9c87-33bf-b14b-b391746b4e80 | -12.64432 | -44.24289 | 2025-10-29 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af7fb6db-b59d-3c4f-89c8-a5b0120ca6ed | -13.61082 | -46.49413 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5d17c15-c63b-3a2a-9ee8-de33a9d62d4a | -13.57419 | -49.59384 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7f5fb313-1ef4-3662-85ef-c9f54e1d3f38 | -13.5443 | -47.32296 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| feb5140f-05ca-31a3-9ab8-3d6d40b4f83c | -13.21339 | -47.0643 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1f50fafa-8a21-3a83-83fa-a91b7673c264 | -13.78983 | -43.252 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8b81a60c-b645-3b4f-9cad-200b0a818eae | -10.93123 | -43.76 | 2025-10-29 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b67a43d6-feb9-3d5e-95dd-10fa6d2214fd | -12.08284 | -48.00076 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f2d6ee5-d40c-361e-b119-cf4f6e10c21e | -9.29202 | -47.01574 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8dc78f7a-f6cd-3793-a323-bd8a786e30e1 | -12.40712 | -44.7046 | 2025-10-29 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18397b19-ee16-3ed2-876a-224c0385554c | -12.40347 | -46.78892 | 2025-10-29 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 446a4d8b-910c-34c2-ab47-ddb1cea62440 | -12.10522 | -44.59517 | 2025-10-29 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 320878c6-70ec-3bcc-a2d8-f7b99e501bbd | -13.61932 | -46.47226 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3ef099f-28eb-34fc-a7ff-33a6aff3ba57 | -16.11621 | -45.75095 | 2025-10-29 03:55:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 039e2e19-69e0-30c6-8f52-2a493f96337b | -13.63885 | -46.51168 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35fec9c3-f637-3a7f-8275-08341a9b7ece | -14.48705 | -43.94572 | 2025-10-29 03:55:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56fa0081-5879-3169-9426-55f25c7b5cfa | -14.23513 | -48.11722 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae178320-b2e1-3a09-b111-8917e9999308 | -12.20575 | -46.49608 | 2025-10-29 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 666214aa-872c-3813-9a6c-70dd84027130 | -13.04487 | -43.82124 | 2025-10-29 03:55:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8f684653-5e32-3aa2-a18c-b126a83b77a3 | -13.3255 | -47.43516 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27a4ca76-0284-3ebf-853f-6d2c222f945e | -10.45363 | -44.55042 | 2025-10-29 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2408eb87-b1cf-3918-bcc9-a719027862ef | -8.29401 | -49.314 | 2025-10-29 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d96257c3-cb67-3f69-91b1-f4146ece5709 | -10.22125 | -45.93863 | 2025-10-29 03:55:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4fc5788-1572-34ba-964f-26111e68d4e7 | -13.64241 | -46.51709 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0efb43c5-c7a6-320c-b554-ff3af4b408f5 | -13.58165 | -49.59393 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 497083fe-a345-36ea-b4c2-b93b8425b7f3 | -11.72504 | -44.67896 | 2025-10-29 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfa6a53e-4833-37b7-a558-4b2c8c0d184e | -15.63812 | -46.96911 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8700392-b047-3e8e-827d-3fced143fa63 | -13.31975 | -42.42082 | 2025-10-29 03:55:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 81bb3b4c-83ac-3e4b-a123-4459e95acd46 | -12.08394 | -47.99493 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13349329-ccb3-36dc-aa8d-2fc6f3e2e212 | -12.68837 | -48.43875 | 2025-10-29 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 381387b7-6ebd-3a77-8685-f874d3da129a | -13.43552 | -47.37573 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 456f0f3e-f3bf-3f0c-8a0c-4a3c84612cc9 | -13.2318 | -48.5629 | 2025-10-29 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b678bd37-b9ae-3995-9104-8ff1c0667ae9 | -9.75205 | -45.00624 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fa2cf88-e403-3540-8fd2-97edfa5a8759 | -14.42538 | -47.84695 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 875d2c9d-989b-3f99-b1a7-516d9c834d65 | -10.5458 | -44.59759 | 2025-10-29 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32c35749-03c5-3aa3-b8ce-806f9f5dfac4 | -12.01227 | -46.78351 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 52431530-0f62-32b3-a1e5-f83cb2c3a0f2 | -9.49531 | -47.00559 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8f0f7239-a6c2-3ecb-9c85-d135c9e1ed9e | -13.26642 | -47.72741 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f6e22e53-48ca-377b-80b1-2a0e78b6fdd5 | -10.94281 | -47.62803 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 595ab9cc-3ffb-3bc7-9f94-e07155f9288a | -13.57639 | -49.61155 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75a15b02-ea71-3439-9390-7165aa2599e8 | -14.83006 | -47.40646 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21cf80ad-ccd7-38f2-bb32-791a7f1421ae | -9.62188 | -46.86575 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39f69533-5a1d-3f03-ad31-c26685863672 | -9.23121 | -46.35498 | 2025-10-29 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2780a9e7-01f4-36fb-a007-753d6821c045 | -14.61835 | -45.0022 | 2025-10-29 03:55:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 508623a4-846f-3652-8a9b-dd1a709410bc | -14.98992 | -47.86856 | 2025-10-29 03:55:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d65b831b-4067-3669-a0f7-f0843434f603 | -11.06329 | -47.53651 | 2025-10-29 03:55:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c2cd1dd4-6282-3bda-8357-a754f2159d55 | -8.72167 | -50.01385 | 2025-10-29 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86f01877-9333-3923-94b0-c1d6a787976c | -10.53009 | -47.73756 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 356a57d7-b2c7-3aa6-a129-d1a893867521 | -12.20206 | -46.49797 | 2025-10-29 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f9e8dd6-67cd-3e68-89ed-a403ba55f5e8 | -13.69708 | -47.67019 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d35dc9ae-78d2-3799-88b1-2b920ac051a6 | -13.64681 | -46.51797 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a292f7e8-212e-35a1-b753-a048e7e91b63 | -14.07431 | -41.74649 | 2025-10-29 03:55:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9324c9fb-08ee-3eed-b96d-c618acc70a7a | -11.01029 | -47.56907 | 2025-10-29 03:55:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5693fa09-eed1-39b7-9ee0-93dec26014b3 | -12.87435 | -48.6314 | 2025-10-29 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 754341dc-f92f-36fa-a25c-ae6a7c3a91de | -10.52142 | -44.20333 | 2025-10-29 03:55:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d25129e1-1517-30c0-9672-d532cb9fdc92 | -11.15253 | -47.77876 | 2025-10-29 03:55:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a54ce2e-3aa5-3a0c-b176-d8862a51ec65 | -9.89851 | -44.89372 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a50f26bd-e1ca-3b88-8b94-7d486f92848e | -13.57104 | -49.61012 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abcfa802-1cda-3e62-9f01-26c22c8a50ec | -13.63426 | -47.01702 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fd87fd0-ad66-3190-b240-3396a6560fa8 | -15.1692 | -47.21667 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0572398-32f5-362e-9c88-9da7861ce0ff | -10.50702 | -47.7208 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6505ab1a-908a-33b8-a07a-7c8ec749dcda | -13.23249 | -48.55938 | 2025-10-29 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55cc6676-1bc6-3d62-8a1d-15f4e94285db | -13.93497 | -48.43842 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6314fcd3-d32a-39cc-9199-4d3ae14455dc | -13.63444 | -46.51083 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38210496-552a-39f9-9e3e-a34e569e4ad1 | -13.42631 | -47.37303 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1eff8295-ec41-3ce3-af58-bd70ddbcfbf9 | -13.33058 | -43.18585 | 2025-10-29 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d270d94e-a23b-351a-9b16-ac3e14357134 | -12.15498 | -47.69835 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 90b89ef6-dc5d-3e7a-9452-07101e026d71 | -12.40013 | -46.65079 | 2025-10-29 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4847dfb0-cb16-3e00-8a92-9b4edc12d175 | -13.35632 | -47.66877 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4bc3c4a-6853-38df-bede-689254fcc066 | -15.10294 | -43.83815 | 2025-10-29 03:55:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 0f04fdbb-45dd-30d0-abc8-b03792a76abd | -12.74928 | -45.16913 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72a98871-f5e7-3b33-91ca-d47a6753793c | -13.57867 | -49.59972 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b8bce649-0ecb-36e7-b042-903dbcdf5c4c | -11.06437 | -47.53077 | 2025-10-29 03:55:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1757c8b8-5192-3e88-8fdf-4ce7c54ada26 | -13.54076 | -47.13625 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41fc26e9-1940-33ed-b725-00fc9baaa320 | -13.68239 | -47.19106 | 2025-10-29 03:55:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c9f6f18-db19-34b5-bed1-274448052cae | -11.02616 | -47.84625 | 2025-10-29 03:55:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e3544fd-8356-35c1-8c53-3a7881c4fed2 | -15.16457 | -47.2165 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05a6f95e-2f22-3c99-ae74-1a1f7eb1feda | -14.98624 | -47.87009 | 2025-10-29 03:55:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f3bbd787-0350-34a7-aab0-19368e38e1be | -9.44767 | -46.90519 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c3eb1ace-5aa3-3b7a-ae31-8371518c97ee | -10.90102 | -45.10801 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 100902eb-ba10-304e-b1cb-9a6b407ae85b | -9.62673 | -46.86666 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c08ed3ca-1706-3c6e-9005-6bd2d6452ce1 | -12.07462 | -46.38767 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e69ed795-349a-308b-96af-67486d8cc5eb | -13.57785 | -49.60398 | 2025-10-29 03:55:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ce645dc-105e-3e88-b2dd-23b8994c69be | -12.29219 | -47.00985 | 2025-10-29 03:55:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64070e45-a31a-3877-a30a-56ba8b7fd616 | -9.49124 | -47.01199 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 80aa3e7b-c736-31d2-b307-29ca0de7771b | -10.51769 | -47.71966 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4425e488-da23-396c-b67b-df00eb7d2622 | -10.04046 | -47.14149 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f2c54aea-b9bb-30ad-9d17-9f07dc78ddad | -14.27942 | -47.31281 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3940aa4b-eabb-39b9-a5cd-0ae39fef60f3 | -12.3875 | -50.16602 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e28ddf8c-ba35-34e5-9ccd-d0e692a81b02 | -13.61641 | -47.59914 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef969305-2442-3a29-9625-96f26accf4db | -8.71831 | -47.991 | 2025-10-29 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8851d2c-72b7-38e0-882a-14564c235f07 | -15.16378 | -47.22062 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README17.md)
