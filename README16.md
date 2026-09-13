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
| 74209030-2c55-39dc-8f62-c39bff2affc4 | -7.63938 | -73.10332 | 2026-09-13 01:41:00 | TERRA_M-M | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ff39d692-ed6b-32f8-8a0a-dd1063b371ad | -10.58227 | -69.61327 | 2026-09-13 01:41:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3530e3cb-d5e3-3ac6-be61-102f4d20b110 | -6.863 | -55.5801 | 2026-09-13 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b66de1b6-d63c-312e-96ef-f2164fa8bd0a | -10.6829 | -54.1475 | 2026-09-13 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 388b11e8-5d0a-3133-ba22-ceb056eb0f19 | -6.8445 | -55.581 | 2026-09-13 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 813b07e3-2b81-3366-b88e-95078d2b6727 | -10.6827 | -54.1679 | 2026-09-13 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 175.4 |
| c2cfd868-58fe-3286-8f45-71eaee782269 | -8.5417 | -54.6985 | 2026-09-13 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4054c4ce-456c-34eb-bc54-0f7bfa44c4f4 | -6.6021 | -58.849 | 2026-09-13 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2bc38cbe-d0ae-3be7-bbb5-76c60bd42658 | -17.5154 | -40.1685 | 2026-09-13 01:50:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 68.9 |
| dda50102-df89-3b08-871b-1b76bbf8f71e | -2.6784 | -57.5504 | 2026-09-13 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 450a32e2-29a4-39ae-9f79-df0aa458b788 | -3.728 | -61.7555 | 2026-09-13 01:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 208ed210-5df4-3592-afb8-8a588eb53066 | -4.9296 | -45.8363 | 2026-09-13 01:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 50c0f9e8-a8a5-35bc-9d84-ccfa6201c59e | -6.1111 | -57.6645 | 2026-09-13 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 64ead0b6-f74a-3916-bc67-88a1e39d2da9 | -10.6413 | -46.1133 | 2026-09-13 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 5329f43f-2300-3190-a46b-9f21c2dcf2d0 | -2.9579 | -50.3988 | 2026-09-13 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| c9fd1856-40fa-3a91-8573-6ab4c36f8169 | -10.6417 | -46.0906 | 2026-09-13 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 409f06c1-ccb3-327b-b783-8cd2116b0131 | -2.6785 | -57.5115 | 2026-09-13 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 0eb97e89-f387-34f9-8f02-e928bc501514 | -9.8992 | -47.5874 | 2026-09-13 01:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 6fff6d4c-57e6-3c8d-a776-7addcfe2d1b8 | -10.6824 | -54.1884 | 2026-09-13 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 20824464-0bde-3d24-bede-92770aab865f | -6.0731 | -57.861 | 2026-09-13 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 180acd6b-d25e-392d-a21e-3027da64c4f9 | -2.6785 | -57.531 | 2026-09-13 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| f63965c1-92e9-3768-8b13-e66636e8b7d1 | -12.8543 | -44.386 | 2026-09-13 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 477cebc5-87ad-3c23-860b-40ef88966b17 | -2.6602 | -57.5313 | 2026-09-13 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| b0db7c4b-c002-31a3-9941-bca0691c30e8 | -10.7015 | -54.1663 | 2026-09-13 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 2047edd7-cdf2-3e47-81a3-521a1f036a00 | -13.616 | -47.8774 | 2026-09-13 01:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 9db504ef-d367-38a2-8e22-cd2b4f7a13b1 | -8.5415 | -54.7187 | 2026-09-13 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 39df4403-1082-36e2-bfe1-2acf11da5417 | -6.1111 | -57.6645 | 2026-09-13 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a49a08ef-364d-3e94-ae0d-1c35367f6f5d | -3.4058 | -59.2538 | 2026-09-13 02:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 2c6155fb-9320-3db0-938f-1c7ec0f6cac7 | -2.6785 | -57.5115 | 2026-09-13 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 1fc06356-cdc2-3713-b827-94394759e682 | -2.6602 | -57.5313 | 2026-09-13 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 6a103684-2385-301e-b69b-f49d3be83ad0 | -10.7018 | -54.1458 | 2026-09-13 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 60db8b26-04d5-32f0-be54-63b27a61ef15 | -6.6021 | -58.849 | 2026-09-13 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| cc6cfa15-3871-3bd3-918f-e79ed451f21b | -8.5417 | -54.6985 | 2026-09-13 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e4b403ca-7cb2-353b-a1a6-b444fead60af | -10.6413 | -46.1133 | 2026-09-13 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2f3bc70e-49ac-3ce6-9f3f-1974ec79fca2 | -2.9579 | -50.3988 | 2026-09-13 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 53134e57-5fb4-3be4-887f-809be7c1a3b1 | -6.863 | -55.5801 | 2026-09-13 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 306a179c-a3bf-36c5-bc03-e9dc3b225f27 | -13.616 | -47.8774 | 2026-09-13 02:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 5b34d4d1-fba8-32eb-b369-dd257812a6eb | -2.6784 | -57.5504 | 2026-09-13 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| dad4ce27-7ed5-3e42-859c-42beea82eb80 | -12.8543 | -44.386 | 2026-09-13 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 76e31d3f-c826-3997-b280-b60f3ce900cd | -10.6417 | -46.0906 | 2026-09-13 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 40762e7d-da03-32a6-b2a3-17755fac838d | -4.911 | -45.8374 | 2026-09-13 02:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 07eab223-6c6f-367f-8742-b8fc19fc1694 | -14.11 | -46.3523 | 2026-09-13 02:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 834b30c4-b7d3-3798-bc72-3cea547cecf1 | -4.9296 | -45.8363 | 2026-09-13 02:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 102.0 |
| d2b8cb90-76e6-3f9e-ac1f-068b73aeacbc | -10.6829 | -54.1475 | 2026-09-13 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| f1d196d3-86d4-3589-84e1-2f8b5ae166e5 | -10.7015 | -54.1663 | 2026-09-13 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 6389d8e9-4e4d-341f-bd81-71d1a2223746 | -2.6785 | -57.531 | 2026-09-13 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 695d4722-f64c-314c-b9a6-ae7aced4f77e | -10.6827 | -54.1679 | 2026-09-13 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 2304e5c5-79ca-399f-a9f1-875f4846c2d6 | -10.6226 | -46.0931 | 2026-09-13 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e6ba1266-ca8d-3b8d-883d-1a1b9b090dda | -10.6417 | -46.0906 | 2026-09-13 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 0dc272cb-be48-3aec-a4b3-9ad2c5b355ec | -6.0731 | -57.861 | 2026-09-13 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 05789ef8-0910-3ada-8d2c-4a084ed8ca06 | -10.6827 | -54.1679 | 2026-09-13 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 184.4 |
| a587581b-9ab5-3a5c-8e78-f375c8313311 | -10.2929 | -45.2932 | 2026-09-13 02:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 69a06f28-5bad-3ea6-9c7d-b20c0ef98624 | -10.6223 | -46.1157 | 2026-09-13 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 5683dae1-8f40-3899-9216-44846959fec0 | -10.6413 | -46.1133 | 2026-09-13 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| f267ba63-eaf6-376c-804e-64ed2fa0ba56 | -2.6602 | -57.5313 | 2026-09-13 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 261a5347-a63c-378e-9b21-35efb4661ada | -14.11 | -46.3523 | 2026-09-13 02:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 6469a3c1-04ad-3f8d-8481-ca0066d6742c | -12.8543 | -44.386 | 2026-09-13 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| f0068d97-6ec4-3d07-ac52-2fa4d7dd93f2 | -10.6824 | -54.1884 | 2026-09-13 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 386e843e-ad09-3385-a729-1005e1dd85e7 | -8.5417 | -54.6985 | 2026-09-13 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ed322397-5700-3a71-9f6e-ea592284f76f | -2.6784 | -57.5504 | 2026-09-13 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c3b1e4bf-d058-3720-8c6f-64aa011ac1a5 | -10.3123 | -45.2678 | 2026-09-13 02:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 54ca1dcc-270c-3ba7-a979-3215275b880d | -2.9579 | -50.3988 | 2026-09-13 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ea55f3b2-c8ab-36ba-abf1-f93824cf274a | -10.312 | -45.2907 | 2026-09-13 02:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 188.2 |
| a5a36386-c79c-360c-9b56-1213a2473b5a | -6.1111 | -57.6645 | 2026-09-13 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d4d4044f-01a7-36ea-ad51-4b7120587b1a | -2.6785 | -57.531 | 2026-09-13 02:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 2939939e-cec2-35f4-9cb0-212edc8ba521 | -8.5415 | -54.7187 | 2026-09-13 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 5f33420d-5100-3ff2-8db8-bc5d44375bbf | -10.6829 | -54.1475 | 2026-09-13 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 62cd0a69-0ec0-3663-936c-d963b67acfc2 | -3.3293 | -42.2893 | 2026-09-13 02:10:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 7762c716-65d4-3428-a0d5-c5e4f4cf8a0c | -6.6021 | -58.849 | 2026-09-13 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| da820a90-aa29-3a2d-80f5-2f8fc2d6b598 | -10.7015 | -54.1663 | 2026-09-13 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f9d297b9-c59f-3097-ab36-c9e2733a3deb | -6.863 | -55.5801 | 2026-09-13 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d33d1dd9-482f-352a-84ad-1b5ab9ebe264 | -8.5417 | -54.6985 | 2026-09-13 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 60e79a78-8c67-300a-8dc1-9a1b0362a079 | -10.3123 | -45.2678 | 2026-09-13 02:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| f566aad8-1ce2-3810-91c8-923aaf82b4ee | -10.312 | -45.2907 | 2026-09-13 02:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 314.7 |
| ef5971a3-45a3-366f-8ceb-d8681a545211 | -10.7015 | -54.1663 | 2026-09-13 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| ad54140a-1a6a-3236-bed8-2e19eecb8b38 | -10.6827 | -54.1679 | 2026-09-13 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 179.2 |
| 9e3be684-cf79-3d07-9be3-aacf455ce638 | -6.1111 | -57.6645 | 2026-09-13 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| cdafd82c-a762-38c0-95f6-e59e41745cdd | -6.0731 | -57.861 | 2026-09-13 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 70136e2b-9eb2-3645-a33c-f18098c21c9b | -3.728 | -61.7555 | 2026-09-13 02:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 46b3fc08-dbea-35ce-b1f8-353819d43ddd | -2.6785 | -57.531 | 2026-09-13 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| be3fc7b3-a3b6-3727-aedc-323a3c4812b4 | -2.6784 | -57.5504 | 2026-09-13 02:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a9f91746-3e92-3123-a7c1-72bab8a34c07 | -2.9579 | -50.3988 | 2026-09-13 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 9640cad6-9660-3e3a-81aa-a4d4390623b6 | -10.6829 | -54.1475 | 2026-09-13 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 8558afe3-8f56-3b1e-9be0-0f3fdde3f284 | -10.2929 | -45.2932 | 2026-09-13 02:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 007ced2e-0cae-3534-b0aa-2d65a96a6938 | -14.11 | -46.3523 | 2026-09-13 02:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 3acfeab1-4e43-37fc-9575-6280dda7108e | -6.6021 | -58.849 | 2026-09-13 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 43484508-63dc-33fa-83e7-5663fb476a9a | -3.4058 | -59.2538 | 2026-09-13 02:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 3ebdca3c-5485-354f-9172-7648cb34f0a6 | -6.863 | -55.5801 | 2026-09-13 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 4202b791-9a9e-333b-a3b7-a3493fbf9483 | -2.6784 | -57.5504 | 2026-09-13 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| b3f4ab28-7e7c-361e-be1e-68bb21f425e1 | -5.1254 | -55.9748 | 2026-09-13 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 3ec2e290-f99e-37d6-9a37-e78d91fd831f | -10.7015 | -54.1663 | 2026-09-13 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 642cfc4d-fcd3-3624-906f-3edaf6baf6fa | -8.5415 | -54.7187 | 2026-09-13 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d23e1c78-f4c0-39e3-bd1e-5ff36e1a5887 | -13.9909 | -54.0813 | 2026-09-13 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 82665136-dbc7-3040-89b9-d6c9cb1f673d | -10.331 | -45.2883 | 2026-09-13 02:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| a54a2973-3a7c-3ae8-b89b-288ec3b5f7bf | -13.9912 | -54.0605 | 2026-09-13 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e8a5a383-5b31-3b47-94de-8f67d5497b6e | -8.5417 | -54.6985 | 2026-09-13 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 658507db-f21d-3037-9d89-df7f65a7c0b1 | -10.3123 | -45.2678 | 2026-09-13 02:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| de2b7bc3-0378-3b57-a569-ebd528f6d31b | -6.0731 | -57.861 | 2026-09-13 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 5f5cabac-667a-3ee2-96c5-49e438ad70aa | -3.4058 | -59.2538 | 2026-09-13 02:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| fc0d4c9f-fe96-3f60-8d2b-b6ddefcc17f1 | -10.2929 | -45.2932 | 2026-09-13 02:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |


[Clique aqui para ver as próximas entradas](README17.md)
