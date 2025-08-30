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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e79b0c73-9cfb-3df9-8d96-1f8035589ed0 | -16.40967 | -45.65498 | 2025-08-30 04:51:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e834123a-895a-3f60-81ff-f31d67209271 | -13.36589 | -47.0116 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fffbd59c-8d1c-3555-9f96-c7ebb9a838f9 | -14.34618 | -53.30027 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a03273b1-986a-3fbf-9431-b7c091819550 | -13.67922 | -46.87902 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c64523f8-b6c2-3201-a0c9-76d5c73698da | -13.96751 | -46.33107 | 2025-08-30 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2020178a-421b-3ec6-a65c-f7ab92b54143 | -14.00696 | -44.5815 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 422a636c-136e-3279-9559-048851e1a18e | -13.38304 | -47.01014 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ea4fb9a9-5ab5-33fa-bfae-c1ac5ef02270 | -13.57021 | -46.92086 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04ea5173-ded2-3d90-b71e-e31e287465f1 | -13.35627 | -54.38335 | 2025-08-30 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 256bccb9-4b32-3add-8487-bd89c5b35b18 | -13.36487 | -47.01933 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 65fc5d91-178b-3ee9-a693-9ef6b8354df3 | -9.78295 | -64.24315 | 2025-08-30 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e60bc84f-c634-3530-81bc-c51c7011bd0d | -15.08088 | -48.63148 | 2025-08-30 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c911609d-9372-3e2b-81f9-372089019448 | -12.02306 | -57.08708 | 2025-08-30 04:51:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 253b7049-60a2-3442-b26c-cf6424de7f5e | -13.57602 | -46.90974 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60a68669-4e1a-38f1-bd98-bba22606b09c | -13.36521 | -46.98456 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d6f369cf-2413-3d4f-8644-9c579f135f5a | -13.57072 | -46.91711 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66ecb3f4-0e58-3c47-8485-5a5db800a3c2 | -13.58662 | -46.89498 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22b66da7-0bd5-3260-b9ab-f0a23fef19d2 | -14.325 | -51.88409 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87e572ec-2a1f-3720-b37c-2acaba23e6d1 | -17.91477 | -46.84057 | 2025-08-30 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a34ba0c-371a-3125-8d56-fa141a12b11e | -14.23906 | -48.06323 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0dbfb33b-b77b-3c61-a2b4-517476d0dc43 | -14.00495 | -44.59814 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b59b8ed3-eced-3fc8-8a3e-bf230ef8e065 | -15.08153 | -48.62673 | 2025-08-30 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e0e7d13-076c-3d32-967f-e0f17405d194 | -11.39508 | -63.25898 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0d42e56-f963-392b-8e5c-a6abccb90433 | -14.31763 | -53.09359 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd532b1b-60e1-3dc0-9cca-3fe8b19fd669 | -12.93998 | -48.12836 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8c07bc25-5ad1-393f-bf32-a5300c313b5e | -13.36688 | -47.00407 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df812df3-f567-3f7e-bce0-ce78c5b6b938 | -14.10774 | -51.77936 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6afeca92-a7d5-370c-97de-a200a08ed553 | -12.89478 | -48.88576 | 2025-08-30 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 367c65c6-8aed-3f31-9395-af2e545c3a0f | -13.55757 | -46.95077 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cdf8620-ba04-35c4-87f2-d406525336b4 | -13.49554 | -46.84176 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e402b2af-ff3e-36c8-b87a-a33df4674cf8 | -14.50704 | -52.99311 | 2025-08-30 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0efbf9a-ef05-3e8e-be9e-1aa9d07fd195 | -13.37787 | -47.01714 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87dc0a2c-2b07-3b7f-b72d-2e65bcf861f4 | -13.64043 | -48.15898 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abe2d71d-8af4-3f53-9472-2418a0ce58d6 | -12.9361 | -48.12794 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| af264c5f-2d73-3a09-9f6f-be94a0eb42a9 | -14.02525 | -44.55519 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 32187d86-f592-3735-be3c-e33b1cb3d6ca | -13.42551 | -46.94717 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19816df7-a9b1-37dd-8985-a279e447456d | -16.53359 | -55.04122 | 2025-08-30 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4408a421-b853-3aef-ae13-89534b6bfdaa | -14.01086 | -44.58578 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19bf0d00-88e5-3398-a146-a196dc5d935b | -13.36683 | -46.9937 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 15717d85-af29-3302-be50-1bf3e3468a13 | -13.57124 | -46.91333 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f222d925-84cb-3e7c-9a15-92e2d3a72f3b | -15.20489 | -56.06495 | 2025-08-30 04:51:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f30b47b2-f2d4-3fb1-b834-70046fb87b74 | -13.36896 | -46.9784 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b98f233-008e-398e-ad4e-3acc142b3fe3 | -13.38451 | -46.99917 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 483c2698-0e96-33f0-886c-e4a8da24372c | -13.66089 | -46.91921 | 2025-08-30 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62a71c58-d6a1-3f80-8433-54ff65e0b580 | -14.34119 | -51.89042 | 2025-08-30 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 488dc961-f5e4-3a88-b4e9-451d67234f83 | -13.35384 | -46.87151 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8055e7d7-332b-3f57-81fb-f94ebdb89ab4 | -13.40713 | -46.95715 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21505bee-242d-3d58-9022-3fde54323e72 | -12.60939 | -57.01874 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 174375bb-6c81-3661-bf7e-1dab4346ec41 | -13.36786 | -46.9863 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2b457fd5-0a96-3960-9a78-8b6450e01f56 | -13.10344 | -57.13031 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15c6c6a6-f280-3e0e-ae19-c9d4d1726932 | -13.36423 | -47.01236 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2ce5148-1bc5-32fa-a664-24a666a9601a | -14.59508 | -54.5453 | 2025-08-30 04:51:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4fcfa31c-cf70-3482-97d4-0a039809ecdd | -15.21934 | -53.80543 | 2025-08-30 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 813374b6-907a-34f0-9b17-3205af47a8e3 | -12.42648 | -63.91616 | 2025-08-30 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e74e074-2981-31c5-93ab-cb9993d2c668 | -15.02319 | -49.2458 | 2025-08-30 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1205e017-8c4f-361e-bef3-f11b7747674c | -14.0063 | -44.58701 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8dd0ee05-5252-3566-a076-133edfa9791b | -13.62827 | -48.18851 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b14d0d7e-901b-3dc7-ac00-78cf380ff594 | -13.36882 | -46.98942 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0dcfe94f-76dc-396e-bcc1-edeee8fac651 | -13.62484 | -48.25008 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6b44659-fb25-3a59-8e36-c9e15e8158d4 | -13.38593 | -46.9565 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bfc3c218-d3e2-3979-9dcf-f70d38ee80b6 | -13.40774 | -46.95257 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 271d5f28-f7b9-3ef9-a6cf-354aa117fe6e | -14.02298 | -44.49057 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23817bb1-f81c-3d40-ba0b-719d1b8b9ffb | -13.43386 | -46.94839 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62f08f76-5456-37a0-b9b3-1d7184b64bfd | -9.78066 | -64.25444 | 2025-08-30 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ebf3d51-cae7-330e-b54f-560289f8e663 | -14.37979 | -47.85212 | 2025-08-30 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cce8adbd-f929-3ed9-bb78-b46d2f154cc9 | -13.3727 | -47.02414 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4df17346-74aa-3ca8-90b1-5ab11b58362e | -11.33809 | -63.29468 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc994c6c-7294-3913-9008-248448146fd8 | -12.71608 | -48.1902 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65b14067-d47a-3fc3-91be-fe9780abe3cb | -14.6273 | -48.07106 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9c0f4e5-5b5b-387d-843f-6932213fc338 | -13.56392 | -46.9356 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac80ce31-a0ff-3029-acef-f6e4b1a9455c | -14.62669 | -48.07562 | 2025-08-30 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 08bac465-a427-3863-9450-bee5abcc739a | -17.24826 | -44.4696 | 2025-08-30 04:51:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b728eb6-571b-371b-aa29-48f7f5034d53 | -13.19712 | -45.2916 | 2025-08-30 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be92aca0-03cd-35d6-a87e-23e645d9f3d7 | -13.46802 | -46.94794 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f44e2a6-791d-32c3-a45d-57fec418627b | -13.35598 | -51.77043 | 2025-08-30 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 440f0b3c-62fc-3dc7-8e8c-e7b20fdc7d95 | -13.47535 | -46.95661 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54efec39-31f2-3aa8-bb57-751317faff4c | -13.36834 | -46.99305 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 42e1ef13-97ff-3aaf-815e-e4de58e25866 | -12.8531 | -48.1781 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 771358a5-c6be-3833-9203-1b7de5900a16 | -12.85061 | -48.16801 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c479753-d2f6-30de-92a2-5088a9042c39 | -12.82916 | -48.0975 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6abe907a-5233-3c7e-ab43-cf528f47df24 | -12.92953 | -56.97937 | 2025-08-30 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5733de9-8a44-374d-9357-c3b325f6c5a4 | -14.02164 | -44.54345 | 2025-08-30 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e880ec5a-2b0f-3c31-a6be-fd263bb0bc5f | -13.39829 | -46.95955 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c069064c-289f-3cfe-a318-7e2c6eb69b19 | -12.9235 | -46.35612 | 2025-08-30 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e91bf9a-0a23-3faa-a31a-7ad3a638be02 | -12.65651 | -48.18424 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0525f62b-b29a-32f0-a7dd-9290891c6e6b | -15.31029 | -46.09093 | 2025-08-30 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0ffb4d4-6a1e-3aed-b5f0-8e25a0c1c9f9 | -12.83369 | -48.09325 | 2025-08-30 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a627983a-405f-32fd-b0c8-b3c7ed850c6a | -12.90027 | -48.9002 | 2025-08-30 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9684b95d-9051-3772-afd7-3abe48163fd0 | -16.58094 | -54.64971 | 2025-08-30 04:51:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 610c2024-ff7e-3fa1-b29d-d0335594051b | -15.7649 | -47.7681 | 2025-08-30 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7660839b-49fc-3454-bc64-7ba9eadc3ac0 | -9.76104 | -65.08622 | 2025-08-30 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2f7524a-6ac4-3ac2-83ac-99ff12be7e56 | -13.36547 | -46.88031 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61f5b275-bdfa-3c93-81d2-db66dd63148c | -13.44216 | -46.95004 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c42db0a1-e47a-3502-b927-d066264ebd38 | -13.62302 | -48.25279 | 2025-08-30 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e327a452-09e0-38c4-80f3-220ebeb71baf | -15.6681 | -52.76643 | 2025-08-30 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0638688-dbb5-371c-9db0-8f0b79004663 | -13.41167 | -47.01809 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29d7c414-61f8-31f9-a4f1-02ed32b95c3d | -13.45669 | -46.96843 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1683aa5f-c474-330d-93c6-20a187376eb7 | -14.99362 | -46.69912 | 2025-08-30 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4fbac47-1d12-3c9d-817e-9a01ef793da7 | -11.39596 | -63.25445 | 2025-08-30 04:51:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83eaaf3c-de1c-36c7-942b-d7085033f233 | -13.40512 | -46.84385 | 2025-08-30 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README60.md)
