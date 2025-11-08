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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29df3648-fd21-3057-8d03-bc88b6194896 | -4.5295 | -45.603901 | 2025-11-08 00:14:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1be91722-a1b0-3c97-a567-af6243a5c6c6 | -6.2542 | -44.148499 | 2025-11-08 00:14:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4859a2ca-46fa-3820-a13a-4c147d60525b | -3.686 | -52.119999 | 2025-11-08 00:14:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b777cf6e-4b23-387b-9418-ed62166e9e94 | -3.0905 | -50.309502 | 2025-11-08 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 822384d6-daf3-3bbf-879f-90e14e29b29e | -5.8369 | -43.396999 | 2025-11-08 00:14:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afaaf3b3-b44b-3d4b-af97-a50e421ef57c | -4.4668 | -43.2127 | 2025-11-08 00:14:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fecdb3cd-2e65-3e4d-a042-7c24ed454dc0 | -7.5313 | -47.374298 | 2025-11-08 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae0a1761-28bf-3675-9c8a-63937750aa76 | -4.461 | -45.312302 | 2025-11-08 00:14:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5309798-9d5b-3f69-ae4a-910ba2aa1a03 | -4.9701 | -44.808998 | 2025-11-08 00:14:00 | METOP-B | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f34ab51-5fa5-383d-806d-b9723daae623 | -6.2572 | -44.1609 | 2025-11-08 00:14:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe1c48e4-e6ae-3109-8f41-500520d3c9da | -4.4437 | -43.202 | 2025-11-08 00:14:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19612365-6f23-3b51-9dd0-fa2e9de61b06 | -6.6519 | -39.137699 | 2025-11-08 00:14:00 | METOP-B | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 976d166a-15aa-3a19-9a45-b8a8d8877fa0 | -9.1609 | -51.2901 | 2025-11-08 00:14:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78ac0acb-7692-36bd-86ab-f18e77e2d99f | -4.349 | -46.8148 | 2025-11-08 00:14:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31654a4d-cf63-3c85-958a-43d2a84ad981 | -7.4601 | -46.626499 | 2025-11-08 00:14:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ef626e7-329b-3355-bde5-c84e1c10b963 | -4.408 | -44.347 | 2025-11-08 00:14:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 921bbdff-98d9-368d-8b8d-40da332fe7c0 | -2.823 | -49.814201 | 2025-11-08 00:14:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f26ebc91-83a4-3442-b91d-d50b89f613cb | -8.2153 | -47.387402 | 2025-11-08 00:14:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ba577dc-872c-35c5-9c7c-088593ff8cc3 | -6.0076 | -49.132702 | 2025-11-08 00:14:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58a85bab-c7db-37f9-8605-7d0508056f5a | -10.3563 | -47.319302 | 2025-11-08 00:14:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 590024af-cd71-353b-9da8-1f60424e942a | -4.4473 | -43.2173 | 2025-11-08 00:14:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ad82a3c-835a-3ebb-a57e-ff61f3e8277a | -4.3288 | -44.707901 | 2025-11-08 00:14:00 | METOP-B | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e9f9f23-862b-3df2-b336-fd0dd7e2bb8b | -14.6721 | -51.8759 | 2025-11-08 00:14:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a88ae69-0121-3151-a6c0-92e63eb9532e | -5.4406 | -47.832298 | 2025-11-08 00:14:00 | METOP-B | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 517d062f-3c4f-3c52-8ef4-923f4fa54abd | -3.4245 | -43.145199 | 2025-11-08 00:14:00 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e61e1f05-026c-381c-9ed6-e43fab4ca5a6 | -4.6867 | -46.407101 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a37090e8-143e-396b-80e8-fc37aa4af70d | -7.7849 | -48.517799 | 2025-11-08 00:14:00 | METOP-B | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9750cda7-66a0-3712-8c78-ef4e789f6313 | -5.4424 | -47.840199 | 2025-11-08 00:14:00 | METOP-B | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebf5e379-6e85-3e69-880d-ca0ccd0ed66e | -4.9675 | -49.589199 | 2025-11-08 00:14:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eedb035-c434-3aab-b886-0d403e40be6d | -4.394 | -42.310799 | 2025-11-08 00:14:00 | METOP-B | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e5d46fe2-6315-382f-8262-8b1ae6c0707e | -9.1074 | -48.890301 | 2025-11-08 00:14:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7be5bb2c-be6c-31a4-8f2d-d38ef8cb6afb | -5.6631 | -40.8321 | 2025-11-08 00:14:00 | METOP-B | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c8208361-3eb0-3c30-8b59-0e0de7860b22 | -7.3149 | -47.375 | 2025-11-08 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd86226d-ae00-3653-a70b-5c3c1e3e2658 | -4.2714 | -46.393299 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4eb1f618-682a-3a8e-896b-e95019020217 | -4.8201 | -45.263199 | 2025-11-08 00:14:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fe3be4a-ed53-3ad0-85db-7b4f39338e3c | -3.6781 | -52.084801 | 2025-11-08 00:14:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 255cd081-716e-3824-a235-4bea00e74cc4 | -10.1308 | -46.528301 | 2025-11-08 00:14:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d03c6ec-0326-32e4-aa7d-d818aeeb9b6f | -15.3319 | -50.188702 | 2025-11-08 00:14:00 | METOP-B | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1600627f-4ade-37d3-870d-72745f8f13a9 | -8.3214 | -46.2514 | 2025-11-08 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24b50441-d181-3584-a6dc-9f2ab53d7cf7 | -4.3237 | -45.5168 | 2025-11-08 00:14:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73d0a9c5-0b59-38f9-afe6-11103f951630 | -8.0018 | -38.494801 | 2025-11-08 00:14:00 | METOP-B | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 9739dafb-cc63-3085-8952-30923bc3ac59 | -4.688 | -45.840199 | 2025-11-08 00:14:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2ae1a74-7744-362b-98d1-982420a1852f | -4.8275 | -45.601002 | 2025-11-08 00:14:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 682ebc9e-796c-3ea3-bea8-d3b3a98ddf5b | -5.4339 | -44.6376 | 2025-11-08 00:14:00 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb5e1f3c-7f19-3d3a-8851-7d2e44ec7c90 | -4.2853 | -45.879902 | 2025-11-08 00:14:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 25dc0eba-6d7f-3887-b83f-c6a2fd74010c | -4.087 | -44.9911 | 2025-11-08 00:14:00 | METOP-B | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d3e26061-38c0-37ba-b389-f4887ad79991 | -4.4208 | -44.357498 | 2025-11-08 00:14:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 141da3b8-683b-3b17-aa76-29ca7ee815d2 | -4.2976 | -46.417301 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc89580a-0ebf-351c-9fe3-b49417d41c59 | -13.9359 | -50.047401 | 2025-11-08 00:14:00 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dfe2557e-23cd-3a2f-915e-ec47397951ef | -7.0336 | -46.9646 | 2025-11-08 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 243acc86-4bab-383f-a524-e14979d05846 | -4.3335 | -45.5145 | 2025-11-08 00:14:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b207120e-68b1-3004-8526-ba9db1aa1fe5 | -8.0114 | -38.492199 | 2025-11-08 00:14:00 | METOP-B | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 31f8cb25-a24e-36aa-bf21-2f9f1d0768f4 | -4.4636 | -45.323299 | 2025-11-08 00:14:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 845aabf9-d637-358c-baf7-4bf208986ad2 | -4.3855 | -45.341499 | 2025-11-08 00:14:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c3578fd2-6c19-346a-b39a-0fa512dcb14c | -9.4956 | -47.346401 | 2025-11-08 00:14:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d05c409a-3dea-318d-bfd6-2f699ec1de39 | -3.5097 | -49.931999 | 2025-11-08 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71e6c27e-09e6-3c04-bed4-4336aa9e6df4 | -4.4534 | -43.199699 | 2025-11-08 00:14:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55286473-74fa-3c09-94f6-ba55e09b0c33 | -3.24 | -48.752499 | 2025-11-08 00:14:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c593ee6a-5565-3d05-a36a-d0fb335c5c34 | -9.1413 | -51.294498 | 2025-11-08 00:14:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8849e45f-612a-388d-88b8-b3c8591df173 | -19.9035 | -57.260201 | 2025-11-08 00:14:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 69214f90-9f58-33b2-be31-7dec6f04baf9 | -4.3757 | -45.3437 | 2025-11-08 00:14:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 496ef2a8-b62e-3199-ae0f-e6fa49fda393 | -4.3567 | -46.8036 | 2025-11-08 00:14:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e158ba3-8f61-3308-b187-46e398da1cfa | -7.0355 | -46.9729 | 2025-11-08 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94d1c541-0c7e-3036-91d1-96f06b7dec6e | -17.8752 | -52.3736 | 2025-11-08 00:14:00 | METOP-B | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 63da02e5-30a9-3aa6-b66b-40dba9cfebb2 | -6.6615 | -39.135201 | 2025-11-08 00:14:00 | METOP-B | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9f6c7d2b-fcd8-3e09-887c-30c0f21afc1b | -3.0936 | -50.3232 | 2025-11-08 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c25114c-a515-3249-a1cf-09472d6228a7 | -4.3907 | -45.363499 | 2025-11-08 00:14:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8743270-ce06-3c45-8123-955ae1b3d563 | -10.366 | -49.857899 | 2025-11-08 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fd50af7-162f-3ef0-816b-23231cb740a1 | -8.0696 | -47.1157 | 2025-11-08 00:14:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31dea6d8-17aa-3123-a768-7e86d7ffce12 | -3.4113 | -52.180901 | 2025-11-08 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c52b504-3ebc-393f-af35-1a481976edf9 | -2.8246 | -49.821201 | 2025-11-08 00:14:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48434218-40cc-377e-8c45-71ad3666fd31 | -10.3676 | -49.864899 | 2025-11-08 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7aa8527f-b31f-399d-9a58-6fa2e406a0ef | -3.4283 | -43.161201 | 2025-11-08 00:14:00 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3abef8f5-d811-3568-b0f7-03b8bfe021d3 | -3.3596 | -49.500301 | 2025-11-08 00:14:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 707de7f7-faa6-3432-b131-d0cccac12913 | -4.457 | -43.215 | 2025-11-08 00:14:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f37c825b-911d-3a62-8874-956f6d2f19c0 | -13.0491 | -50.27 | 2025-11-08 00:14:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 79d2bfb5-7d64-3cba-88bf-033157a42eca | -3.3612 | -49.507401 | 2025-11-08 00:14:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52cf2690-ef80-39b4-be08-bac57bf6d6de | -5.9696 | -44.164001 | 2025-11-08 00:14:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25da0856-9e81-3390-b613-8f04e1da22ad | -4.6401 | -46.870201 | 2025-11-08 00:14:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4203f5e6-eb97-3069-ac2e-6f57ef19e47e | -15.1863 | -49.510799 | 2025-11-08 00:14:00 | METOP-B | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b41eaeee-7bfb-3256-8e3e-e77a1a1c0d93 | -4.411 | -44.359798 | 2025-11-08 00:14:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 110e6b46-3c44-32d3-b6c1-ad85297d83fd | -4.2345 | -51.218201 | 2025-11-08 00:14:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d5a5920-3a90-3d68-9e52-d13aed89f853 | -16.1322 | -56.163399 | 2025-11-08 00:14:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e73296d-ca2d-3bc8-a6da-a244b3c07c4e | -13.0589 | -50.267799 | 2025-11-08 00:14:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 909ab74a-bd3f-312f-bda7-50fe7e562767 | -4.6703 | -46.3811 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c1c0ab31-6e4c-33ca-b5db-2315a5209f59 | -3.0352 | -50.2929 | 2025-11-08 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92b00c9d-4e6d-3375-a7fa-087eabbd1a63 | -6.006 | -49.125599 | 2025-11-08 00:14:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3fb6866-eac2-3a8b-9950-aa75b0a9797a | -4.3982 | -42.3284 | 2025-11-08 00:14:00 | METOP-B | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 73f0c61e-4ce4-30a2-b224-467636a9ee79 | -5.4899 | -47.067001 | 2025-11-08 00:14:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36f6fdc8-18dd-3fd7-a8d6-0bdb0d473ff6 | -14.4875 | -52.120399 | 2025-11-08 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 305a3b32-74f3-3457-9cf7-5b6f21c72607 | -7.313 | -47.3671 | 2025-11-08 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f00a4d60-ba07-3bba-84f3-58e13f443996 | -4.6801 | -46.378899 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8622b40-1185-3deb-b7f2-cee26ec093bc | -3.3141 | -50.295601 | 2025-11-08 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa700e60-c12f-3d5d-9275-97e3b12a9caa | -4.4497 | -43.184399 | 2025-11-08 00:14:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0a0b773-30e6-3cc8-8a31-4f02618e215e | -19.476 | -53.915501 | 2025-11-08 00:14:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a2881655-9e66-3917-acde-4b0e2197b6db | -3.0289 | -50.2654 | 2025-11-08 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d56095a5-bfa0-3cfe-b2d4-6a67abfe7228 | -4.4629 | -45.495701 | 2025-11-08 00:14:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4967318-2084-3012-acaf-1879308a83bf | -4.6845 | -46.397701 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f5878ec2-bd68-30dd-ab35-4d05ba5ea251 | -4.2736 | -46.402802 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90805d67-a5a7-3225-af2a-df8e20129eb0 | -4.2904 | -45.681702 | 2025-11-08 00:14:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
