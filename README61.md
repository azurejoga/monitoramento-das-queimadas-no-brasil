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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06d5337f-7b20-34c9-9719-77b6f844ee6d | -4.31027 | -48.09382 | 2025-08-23 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df800ed1-32c5-3d13-867b-3d0481441566 | -2.91851 | -48.30649 | 2025-08-23 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e308dff8-22d1-37b1-8123-9dd14acf3085 | -2.55154 | -47.71329 | 2025-08-23 05:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 951c7ea9-4f22-3266-b805-25634ca21499 | -2.55794 | -47.71017 | 2025-08-23 05:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9f89d1e-93a2-38c8-979a-2f6a07c2ab34 | -4.22354 | -47.21339 | 2025-08-23 05:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfab9d40-d2e4-3cfa-aec7-01c7f74c1dc6 | -4.34204 | -46.4668 | 2025-08-23 05:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3e6510c2-b672-3541-867e-b8edb5dd50f9 | -2.29539 | -47.98884 | 2025-08-23 05:18:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 093623d4-452f-34da-b35d-f6c54b52c892 | -9.9495 | -60.1754 | 2025-08-23 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| e8552156-f9f1-3644-9fd1-871944f214bd | -17.5979 | -46.5715 | 2025-08-23 05:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 52e090eb-c393-359e-91bf-c6c2fdfd9d18 | -5.7429 | -57.6009 | 2025-08-23 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 03654352-9800-3c4e-87c4-082dc338b01f | -6.6044 | -44.5624 | 2025-08-23 05:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 723859c1-16f8-357d-b468-dee8bab2384b | -9.9493 | -60.1947 | 2025-08-23 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 328.2 |
| d0f78305-1525-34d5-9ff0-693856095914 | -7.0164 | -44.6413 | 2025-08-23 05:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 56b1ef55-a1ae-367e-9e87-b9ccc801a8c2 | -9.9492 | -60.2141 | 2025-08-23 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 82f11ffc-6972-3e8e-a630-c76723ea01e2 | -17.5785 | -46.5523 | 2025-08-23 05:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 676d1d93-8640-3cf9-be0a-94a47757ee7e | -12.9921 | -45.2252 | 2025-08-23 05:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 97e95745-482e-35f3-a9a7-282669346a48 | -9.968 | -60.1937 | 2025-08-23 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 151.7 |
| cc8f2afc-56b2-3d16-b42c-fa51762ed5a0 | -5.7615 | -57.5807 | 2025-08-23 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 16541004-564d-3960-97b5-502bb5dc710a | -5.7431 | -57.5814 | 2025-08-23 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b29abc3b-fc11-3c20-91ae-39cdaadbd79d | -20.4042 | -45.592 | 2025-08-23 05:20:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 65.3 |
| c7e93913-d9bd-3c26-8769-b251863dd8e8 | -9.9681 | -60.1743 | 2025-08-23 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| e00c49c9-520f-30b6-b743-8bdd69aa1567 | -17.5985 | -46.5481 | 2025-08-23 05:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 59.4 |
| c3912b67-da5a-331f-8e87-87d0bad7c44e | -5.7614 | -57.6002 | 2025-08-23 05:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ef6511c9-2710-3f77-ae43-54fee6240b2b | -14.36475 | -52.05413 | 2025-08-23 05:21:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7119d6ea-595e-37af-a854-28489ab3baf3 | -9.21146 | -60.78732 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64fc5ce9-1df0-3f79-9638-ce1c5a81c15a | -13.18843 | -59.17041 | 2025-08-23 05:21:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08a2cb19-76d8-372c-acfb-1e3c74c71e82 | -7.03126 | -59.91301 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f816da7e-e210-3a78-9d90-fcd95cbe91a2 | -9.60082 | -55.35167 | 2025-08-23 05:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56cf5da0-af72-3c6e-b9d1-1e29365d08b1 | -9.6015 | -55.34692 | 2025-08-23 05:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4242478-15c5-3ec7-bc7e-1d285bcc26d4 | -9.20446 | -59.45561 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c05caf5d-4a0a-3b22-98ff-f74e474b355b | -14.65686 | -56.59008 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0bd179c8-0b1d-3444-9e29-4f392f7850f0 | -7.81254 | -63.56572 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e56b9183-af44-379d-8e5f-6f7530880570 | -9.24935 | -59.62034 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cc66ba9-da73-3bc3-8519-851beae1d3cd | -7.0575 | -59.82645 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47bac7c7-488a-38f0-951d-82a6b0d934f5 | -13.46859 | -47.03079 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 671b9fb3-cfa4-34da-8c8f-45f4a258dd66 | -9.51694 | -60.55641 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13e52422-5755-3f7d-8d7b-371c02a81451 | -9.44812 | -47.65471 | 2025-08-23 05:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 514cb3e4-9110-3bb0-94a2-61fefd85e6b9 | -7.80865 | -63.56505 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ad8b2c5-cd46-3d25-a036-bd372c821ad5 | -14.46207 | -55.93028 | 2025-08-23 05:21:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eb7db2f-c79e-3d97-acbc-59cca29c4d90 | -14.66161 | -54.91462 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2463ca77-9170-3d93-a75d-be089905b3a3 | -13.02301 | -56.83719 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f61b18e-706e-305e-8408-fd79e25a446d | -14.47046 | -56.48621 | 2025-08-23 05:21:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed4db023-501a-347b-9c2c-1af837eea86c | -14.66887 | -56.58765 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a96f481-69b9-3350-8b15-0dcbc623b375 | -9.18404 | -59.62785 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a96e5649-9890-3576-8ed7-2d9eedefb64a | -9.22994 | -59.76419 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be52df8a-7adb-3869-89fe-0b3848614c46 | -14.61924 | -54.84341 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3f09a68-bb65-3fe2-9e20-71be098e4910 | -8.61723 | -62.60836 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ed76cb0-b778-38c0-9ff7-973bf3cd9530 | -14.37023 | -52.05178 | 2025-08-23 05:21:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9601e39-5e9a-3112-b5af-1798dae41b3c | -9.10695 | -61.42928 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6893ae8-caec-3d96-a088-5b96333aced4 | -9.18624 | -59.59238 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c949289-7967-3eb8-a4cd-80939a3189ec | -8.65963 | -51.27855 | 2025-08-23 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1dd3cde-23d2-3af8-a145-cfd938980034 | -13.02921 | -56.81998 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f86a8f5-ebd0-3771-a5cc-11f851bd330f | -9.19955 | -59.61601 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c235958-0a89-3259-841c-ce51e1b9578c | -8.8977 | -62.42726 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4907578b-71c0-3ed3-8da6-26a619343435 | -13.16532 | -46.92463 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 362d8195-4287-31f1-83a9-952853dfa840 | -13.36108 | -54.40421 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a2ffd5f-bd3f-337b-ae42-2007503f0f61 | -11.18975 | -55.02504 | 2025-08-23 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9df52639-f09d-369f-bc9a-1ef4757a95cf | -7.81028 | -63.55529 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57ed2ace-bfd7-31bb-b279-308d1bd135d9 | -12.70713 | -48.11147 | 2025-08-23 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1b0fc1dc-dd78-3905-8bd4-a629d5151016 | -14.94166 | -48.00653 | 2025-08-23 05:21:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc3bba01-5d11-3778-aedc-e703f635b914 | -9.52365 | -60.5575 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5089ac8c-6973-3fae-8513-6bf5d512e516 | -7.30638 | -59.62479 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a59f43bf-54ed-3562-9e3a-f57b60359059 | -14.33612 | -58.58902 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e632854d-4f05-3da2-be3f-cd4d66bf2e66 | -12.58513 | -60.35023 | 2025-08-23 05:21:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 890bd2c6-93a4-3784-8c1a-fa1c3da49fed | -10.4206 | -64.42133 | 2025-08-23 05:21:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abc6acac-f52c-36ce-b62c-467389622f40 | -13.43243 | -57.1721 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccddcd38-893d-33eb-b31a-2ad30acfede5 | -9.21165 | -59.45318 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65b9aae0-10ca-3404-96b3-7b3adfec3693 | -14.46904 | -56.47913 | 2025-08-23 05:21:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 125098b6-67af-328b-bf47-f27ff6fa8eeb | -13.48226 | -47.03428 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8916605a-9860-3535-8bce-876e33e16062 | -7.43154 | -60.62494 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5e0d4b4-b262-3ac3-8ece-3eff4688c720 | -13.48894 | -47.03321 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4361b4af-bdbc-397e-b409-b18e67b92d36 | -9.1519 | -59.59404 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1a931cb-9c6c-312c-b50b-e2daf83bf16b | -9.65267 | -59.63866 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ccb8d10-8f4e-3e4d-8f40-531dd2cca995 | -9.44553 | -47.65837 | 2025-08-23 05:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 048e1852-e848-31bf-8d61-bbd561a50d33 | -9.93102 | -65.00735 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cbba65f-1312-308d-a444-9690b5a9b190 | -9.51373 | -60.51195 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2b3db9a-dad6-3bcc-8964-2a6d6925a54b | -13.03948 | -46.32141 | 2025-08-23 05:21:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8724b451-d477-3a89-b49d-505766b701e1 | -13.39149 | -46.34047 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 782bec84-49f1-39b0-a3d4-876f2c5c15a1 | -14.35799 | -53.12221 | 2025-08-23 05:21:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9dbddf06-e9d1-3027-86af-51d291a3566e | -13.35966 | -54.40166 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cd50a91-5dd0-3206-8f45-81165c21882b | -14.6489 | -54.91294 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1ada413-49d0-3ae9-b9b3-942cb33a866f | -14.65154 | -54.92547 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e875f539-9b38-3514-9934-e651352eded6 | -9.96165 | -60.18472 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e6d0682b-cc67-39d6-8254-c3e6f418ce29 | -14.29525 | -58.55495 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d38de73-04ed-34cd-8929-0da9b278eea8 | -9.84601 | -64.29257 | 2025-08-23 05:21:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08b80c2d-df16-3293-ac38-f3b088f5a6b0 | -12.58457 | -60.35377 | 2025-08-23 05:21:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2b25599-c6ee-3a49-ba9c-6af56db78274 | -14.61385 | -54.81831 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86329a20-00ad-3878-b103-eae1306ab5b3 | -9.51751 | -60.55285 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43d516c4-c792-36c8-9e92-0aaf2eae7039 | -9.16907 | -59.59321 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffd21fd2-3d00-381a-bb68-6074841a9024 | -9.17185 | -59.61873 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3529cafc-7eea-3174-95f2-e00ed4bb8d9b | -9.19346 | -59.63295 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1236af49-e56b-3f39-a860-4506743d4b0f | -9.1868 | -59.58889 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44fc90a1-0548-33c8-b649-fe3666ccb069 | -12.77619 | -48.70803 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 632f93e4-8b9b-3f18-ae4f-86a85fd2d84d | -8.8999 | -62.43615 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca4868f8-da9c-3a7e-be63-f00216bd6491 | -12.30336 | -49.9992 | 2025-08-23 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70e2b636-8f17-3c53-a3f2-ba2865c48c5c | -15.22898 | -53.8577 | 2025-08-23 05:21:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa29b8a9-2af5-3410-a562-c67264f4f8f0 | -15.0324 | -54.89376 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2dd6aefd-0567-384e-af62-fc6429da26f5 | -11.18827 | -55.0355 | 2025-08-23 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92d5d8b9-70df-3b2b-8560-3443dd0c9dce | -7.31806 | -59.61589 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea10d080-df0b-3f29-a701-7e69cc3cf2b9 | -9.22616 | -59.74929 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README62.md)
