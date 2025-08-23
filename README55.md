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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81c26292-c2b2-332c-a540-02ce2d4c3f72 | -14.29608 | -58.52355 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e97beef8-75dc-319f-a156-21364716c204 | -12.3124 | -49.98808 | 2025-08-23 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 210ccf05-e7a4-3551-8b07-6fef5e533504 | -13.04733 | -46.33095 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7968084e-c382-3746-89d6-3e8c1c162b05 | -9.50765 | -60.51695 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c9537d3-52fe-353e-bfc7-9195d27e5765 | -14.78984 | -45.49615 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 056f4473-87d5-3847-b327-11514c3a2baa | -13.16793 | -46.92406 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 86c1a574-2147-3de7-b593-a3be09dafd0b | -14.82556 | -47.95263 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e7876d9c-63dd-3b25-aab1-8192f3447216 | -13.39098 | -46.25415 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44b4188d-e7c9-3c1e-8f81-26904ee579ef | -11.19598 | -55.03227 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02b8c03e-f749-346b-af0e-7f60988a44d2 | -10.46587 | -59.13401 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d15954f7-2198-3902-8982-2292199fe0b5 | -11.19322 | -55.02813 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c669ed5-6e31-3e37-8b5e-e21d68ebd156 | -14.65196 | -54.90998 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cf075f5-9e6a-3acd-b159-0283d8720e6f | -15.55108 | -55.01153 | 2025-08-23 04:53:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1f7d0d9-e6b7-3289-b28e-1df9f6e3f5e4 | -14.67321 | -54.92785 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5a9eb95b-705f-3ce0-b67c-f772132de876 | -13.36963 | -47.498 | 2025-08-23 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7cf0196-c2fe-3c20-a506-a16f86b6445d | -15.18668 | -48.11241 | 2025-08-23 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 500986e9-2e5e-3f95-b81e-447b57010d24 | -11.35627 | -55.38955 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0b8c729-5ddd-304f-87c8-52721f542a18 | -9.96303 | -60.19374 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d32d031a-1efc-3645-8243-2f19f6fe56eb | -12.58282 | -60.34842 | 2025-08-23 04:53:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 859b311f-f109-346a-a8ac-20b104ef557f | -13.16856 | -46.91916 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 43e2bfaa-f435-3107-b70d-aeb042d587c3 | -15.03257 | -56.37955 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f4c23cf-297e-3890-a6e2-b76942ecede3 | -14.6152 | -54.82011 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc0ed4bc-4898-311a-b791-1fb2aa20c31a | -12.49158 | -53.80639 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a03c3a95-a911-3303-bcc9-9d168d1ec455 | -9.95653 | -60.17896 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| bb2ffd0d-b0d3-3932-9578-af3351239303 | -12.78769 | -48.72002 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6327625e-4ef3-3252-a8f8-c1890a18e5ce | -15.71498 | -41.92902 | 2025-08-23 04:53:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4f5c354f-b272-3cb3-b671-8a7065e563e4 | -14.62344 | -54.83239 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5351a872-93ed-32bc-879c-afbd1da79b09 | -13.38605 | -46.21414 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 70d63c35-1985-3480-9f9b-11b986f83d00 | -9.52005 | -60.55355 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f0c11b7-be9f-3e3a-bc39-5a191e521caf | -13.37754 | -46.21263 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 09e9df95-0a69-3e2f-ae0a-124c0ce51dd0 | -15.35442 | -49.50428 | 2025-08-23 04:53:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 601394bd-c1c8-302d-859c-83adcb7b4298 | -15.71357 | -48.23131 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28ceab33-6cf2-367c-b566-4efd26a3a102 | -13.37799 | -54.4022 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88b79bca-625c-3096-b285-f0b0a3c1b119 | -14.72824 | -55.41658 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 011eb62f-1eac-3e8c-9d9e-b74ae3fc31ae | -8.89776 | -62.42669 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21c0cf38-73b2-3c62-b12e-395f63bf862a | -8.89079 | -62.4329 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c161700-7946-3917-9465-394acf93b1a9 | -11.54922 | -54.39528 | 2025-08-23 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddca91f8-dd2d-3665-9948-6ddb07fcdba7 | -13.49253 | -47.03519 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d979ea0-c772-3053-a960-6cd27dd2b96b | -11.19483 | -55.03946 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90f6f272-ad97-3025-877e-3264490769e7 | -15.35488 | -49.50071 | 2025-08-23 04:53:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccb10c9b-f811-3550-b523-298441c1707e | -9.52052 | -60.52416 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5068617c-43c0-3943-9ab5-23d4a4428335 | -14.80491 | -56.00279 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23e740e1-1d38-3da9-8770-5d49dc7f1db9 | -11.32901 | -55.22471 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94545153-63a4-3330-9e4a-247cf052a4ad | -12.30859 | -49.98752 | 2025-08-23 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48e7e995-4299-313d-8f17-55459d1557bc | -9.24521 | -60.47889 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e84d8a16-1962-3556-9096-88d729616cbc | -14.27801 | -58.53105 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68310249-0074-385a-a024-53dbe0506fb3 | -9.9441 | -60.17833 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3dc04228-745b-3143-b49e-b44c2f8611b7 | -8.69861 | -62.88114 | 2025-08-23 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bd4e5f4-f64c-3eb5-87b9-360a928f006d | -9.24063 | -60.47813 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2f34951c-53a0-39b2-93f9-fe29b1d14b8e | -13.3782 | -46.20708 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8757d98f-4ad7-3a6f-a666-23f765f3f7b8 | -13.0303 | -56.87521 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de4d3bd8-6aa9-371f-a5f6-bfdfabc3f905 | -12.50594 | -53.82315 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08764edd-4a75-38e8-b470-f90eb4f0d2df | -14.33289 | -58.57764 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ba4a7f7-0967-3235-bba6-66a54b51f000 | -10.8649 | -50.82896 | 2025-08-23 04:53:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50dc385e-a236-3462-82e4-f583b40da7d5 | -13.04445 | -46.33049 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92a27ea3-ddde-3906-b009-83b1333e0941 | -13.02571 | -56.83042 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42359e98-5099-3f3f-bf94-57f5b82ca3d8 | -14.90947 | -47.9941 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92a09963-38f6-3ef9-8b13-f56fcb0fe818 | -14.65748 | -56.61 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e31a630-2dff-3d63-b5b5-a70556d11ce8 | -9.95297 | -60.17994 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 97bf6461-fbf5-39c1-8667-b075efe8fd72 | -12.4927 | -53.82103 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e19996de-4426-37ee-8674-fa8a452e47ca | -19.97069 | -47.51877 | 2025-08-23 04:55:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 767272fc-5c9c-322f-a960-4726de9c62cd | -17.08204 | -53.37982 | 2025-08-23 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2566031-d479-36d3-99b0-61441d94c28b | -19.96927 | -47.51886 | 2025-08-23 04:55:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2997d811-6364-3c6f-a2f2-ba69829f9f69 | -22.53318 | -43.72802 | 2025-08-23 04:55:00 | NOAA-21 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b83c5543-91c7-363f-a553-7a012a73dc7e | -21.43435 | -52.69026 | 2025-08-23 04:55:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8455b595-6ee9-3d2e-b2b5-7b7a47b3b526 | -17.58558 | -46.56431 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6bf25ccb-fdaf-3975-8012-d6711b1f5484 | -17.59523 | -49.42372 | 2025-08-23 04:55:00 | NOAA-21 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4481d2ff-465a-3cbd-8e8f-773aa995628c | -22.3053 | -43.17773 | 2025-08-23 04:55:00 | NOAA-21 | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c3e9e05a-ccaf-345c-89ba-f5f96cef5a06 | -23.49315 | -47.62822 | 2025-08-23 04:55:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4654d784-f86d-3536-b61a-4c518548fef0 | -22.17416 | -43.28765 | 2025-08-23 04:55:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5d3d7f97-b795-39d5-a639-d50c76de92b8 | -22.42648 | -44.49712 | 2025-08-23 04:55:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 0fe6ff25-a1ad-3c66-8ba8-dcfca73e8fff | -22.64387 | -47.4533 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 90e0ddce-56a5-37fb-ad80-96756efc38e1 | -17.88811 | -51.76283 | 2025-08-23 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e076a5a5-0744-310e-8370-60b0cd215197 | -17.59651 | -46.55935 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b39369e-681e-3439-be88-314a561993df | -19.68184 | -43.86581 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c625b30-c822-3a6f-8fb4-68e306e27e64 | -22.19607 | -55.97878 | 2025-08-23 04:55:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 488e62df-94f3-3628-bf1c-8b209d70a25f | -22.64417 | -47.45008 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5dca94de-144e-3311-b023-a0b8bb45d42d | -17.5914 | -46.55869 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| f1ae314b-1116-32ad-9891-410a9f2d7a73 | -20.87686 | -54.99908 | 2025-08-23 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b6bced0-b2d4-396f-b0a8-5ca31d456082 | -23.25711 | -49.5045 | 2025-08-23 04:55:00 | NOAA-21 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 600b9969-a0a9-39f4-b5d1-56fd93291cbd | -21.44463 | -46.0004 | 2025-08-23 04:55:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 97943743-03c8-3390-8618-f4e59e31e891 | -22.62966 | -47.43841 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d1084b4-6b38-35ce-8d18-d16577943f02 | -17.8178 | -52.0851 | 2025-08-23 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b915f2d3-169a-325c-b1fb-0b8f24fa5aa4 | -22.66373 | -46.91257 | 2025-08-23 04:55:00 | NOAA-21 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 390ae45b-b545-3593-a509-2f290dd4da73 | -19.97635 | -47.51261 | 2025-08-23 04:55:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46439b60-7ade-3544-94a7-bba6fb69bc4a | -17.57799 | -48.74842 | 2025-08-23 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc06faa5-6c14-3b78-8f2b-b5327717cdfe | -22.66305 | -46.9196 | 2025-08-23 04:55:00 | NOAA-21 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 455143bc-23c5-3dc6-acaf-b25fed6423e9 | -22.66859 | -53.37663 | 2025-08-23 04:55:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd64492a-f78f-322c-9221-dfc99dbccbb1 | -17.60057 | -46.56931 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8b62c573-d6e1-3985-b6b5-052212be8238 | -19.96006 | -47.51145 | 2025-08-23 04:55:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8792e16d-0925-3eee-bf77-4e534378009c | -22.63267 | -47.43981 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c9054aa-fa81-37f3-bac7-45eee399509c | -22.64964 | -47.44734 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7b1d0958-0890-3656-b5b1-950fe8fdd01b | -17.58628 | -46.55805 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 20.7 |
| ef31a124-8920-3a39-9f44-710008e6990d | -20.44551 | -42.12931 | 2025-08-23 04:55:00 | NOAA-21 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 5de9b725-d6f3-3f5e-8104-050ffac1c75b | -22.62753 | -47.43919 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44219b4e-4e7e-360c-b283-319b0bf488d2 | -17.59722 | -46.55307 | 2025-08-23 04:55:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02360c60-7baa-32e0-948f-f996c26995b2 | -17.70544 | -48.51451 | 2025-08-23 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 663e29fa-6259-3b8b-b5a1-abce9225a8e5 | -17.57416 | -48.74312 | 2025-08-23 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f212289-f815-3f4e-ba05-c4f12c70a496 | -22.63481 | -47.439 | 2025-08-23 04:55:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d222bbce-2e03-353b-843b-172b150b030b | -20.87405 | -42.54827 | 2025-08-23 04:55:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |


[Clique aqui para ver as próximas entradas](README56.md)
