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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d6d59f6-ddfd-31a9-ba21-ecf86f9d248a | -13.04812 | -48.00545 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c3a93e0-ad85-3222-824b-cda645c4d74b | -13.04471 | -48.00479 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48443a98-afaf-329c-b11c-7b3da701e09b | -12.4144 | -44.72221 | 2025-09-11 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70f064b4-f5a1-3f21-a059-42fea61d0d0b | -11.03297 | -47.6143 | 2025-09-11 04:23:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db89be7a-57f3-3718-90c4-598654413143 | -12.02918 | -47.6128 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 674f153a-6f05-3f20-9baa-004e9b0599b1 | -11.05978 | -51.3377 | 2025-09-11 04:23:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a447520d-d581-3f14-b46a-8135772b3887 | -11.42129 | -43.56704 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34903cb4-be58-36b2-846d-b68a43e2b37c | -10.39482 | -50.52125 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 545d6291-d78a-35ca-b3e3-00a50c83d762 | -9.80277 | -47.76513 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e24fc025-aed0-3e75-a81f-216eba926a7f | -11.46703 | -43.61761 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 803c3c99-3a1c-3441-ab89-d7942159fd2d | -12.47834 | -47.49327 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5f949eea-ca66-3456-8a04-df3bd3e6ef7a | -11.46923 | -43.69653 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9efadfb8-2ede-38f9-bfc4-c090b5537107 | -11.45373 | -43.58795 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbea4f85-61d0-3c87-b74f-5d22bf6e4f62 | -9.89172 | -51.88693 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf380388-d384-3870-bba4-b1f03143de03 | -15.25112 | -44.02769 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf1ebf73-9459-3fbc-af02-e9e0b10a25e5 | -10.66794 | -48.6238 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1116a405-ad87-351e-9e2c-2c13cc131596 | -9.06996 | -47.07745 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b740667f-7103-3295-8414-8580b47182dd | -10.57198 | -51.50297 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92be8534-a728-3d0f-b1e5-ea3d54fd8600 | -8.79498 | -48.09638 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2afcdab2-c6e9-3fb2-a567-1565427ee3e7 | -12.92255 | -54.76104 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c810c98-0bd1-315c-840e-feb6a5ca7225 | -9.72128 | -43.52179 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c96bd2d-6955-311b-b72e-64cb9fbde2ef | -11.37339 | -45.57909 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b1ec09c-d41f-3d11-b9b0-6c681dc90baf | -9.59035 | -48.063 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c05a4fc8-fbb5-3203-bf2c-3cc6e0936d1f | -12.02707 | -47.53982 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b50c141f-1ca3-3e46-9afd-e735b6202790 | -10.93907 | -46.817 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a81a31a-9ab0-3bd1-adcf-304789f48391 | -8.86926 | -49.55596 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 955f0799-f908-364a-a59e-6aceaed4f268 | -11.36016 | -46.5293 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3f406024-9396-30be-9a11-829bdafe9572 | -9.06808 | -50.49318 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 321b2ade-c477-34fe-89c2-2d95c4af61e6 | -10.15579 | -46.17294 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab0a8635-eebf-35f7-840a-bc4c32e4325a | -14.35766 | -47.29758 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2132a59d-018d-3240-b3a6-5b5e1fb2db4a | -9.0746 | -47.07055 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 546e20f8-ca41-38af-8036-f13634b21332 | -11.37444 | -43.51717 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 28f0a897-b67c-34e7-8795-52aa10986434 | -10.13881 | -47.43844 | 2025-09-11 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68cbf780-a101-3034-bbf1-bb045285e28e | -12.13583 | -44.85065 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15b7dd76-0365-3266-a0e0-5a3e5bce461f | -9.68179 | -43.5272 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10a2093c-ef49-3df0-9e99-43fd14ec74aa | -9.60959 | -48.07856 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f8df8714-542d-301d-9846-f6937932debb | -14.13871 | -45.41323 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc9fa39f-5bdc-3d98-a93d-f11591ac62d6 | -11.78672 | -47.32224 | 2025-09-11 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7392785-b67e-39ef-8902-c818e6252f21 | -12.96814 | -46.71668 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6bf17182-8175-3e06-aa18-c5c8df93adde | -10.74791 | -48.18375 | 2025-09-11 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18508492-03f2-333c-a5f5-cb074ecd08ee | -13.98413 | -48.2197 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9eeeb94-7330-3679-b34e-a4ed86a20062 | -9.8421 | -47.78778 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b20c7aea-b4cf-3673-9fb7-17957f5e6b01 | -11.4149 | -43.53821 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30ff0db7-f96e-3f51-a28d-887f2b0dde8d | -11.46299 | -43.59729 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f82428e2-f36e-3500-aa1d-68a95d962cf0 | -12.93497 | -54.75103 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc4c259b-cef7-3d26-9a00-26e2f4774e0b | -10.8925 | -47.25482 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4f7839b-3c89-3f0b-a54e-a889aa9a6eca | -14.14263 | -45.41013 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85286060-bed4-3461-b849-0a37bb866f50 | -12.21784 | -53.88609 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c04db66-1e99-3780-91cf-1a7dc2d6efde | -12.84748 | -52.96487 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04b953e4-61ad-3011-be0b-7077c1db7931 | -12.2392 | -47.33294 | 2025-09-11 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0f05115-6892-3625-9caf-34168bb4caf0 | -12.97274 | -48.03502 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14de3c8e-be6f-3a26-87ad-16484c57006e | -9.70469 | -43.5384 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd569de4-7b1f-32a2-9141-176ecf7e33fa | -12.53359 | -45.33268 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 357028d4-951e-3ca7-93e6-dc5d0f7add32 | -11.48669 | -43.6394 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4be27809-014f-3448-af63-cfd6c3aecdd1 | -13.65086 | -45.69793 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c496cec-b0ea-32bd-a051-9267277a214f | -14.39578 | -47.30755 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7eb5fc2-b798-3c7e-9580-5fc819ed437b | -10.16858 | -46.17863 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea1799a0-0cf9-328a-ae1c-ce0cf66ebd2e | -12.38581 | -54.1698 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 883b30b2-4ed8-3d67-9800-98546b3b6110 | -8.89832 | -51.0556 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 392cbf92-c577-3794-a1a0-3e609b0e287e | -11.35844 | -46.54 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e89fcc2e-2b14-3280-841e-687e6210d9c4 | -11.34243 | -46.4792 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22f1af3b-1a8b-3196-9156-29d82e43e7b0 | -9.15017 | -46.05442 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6aad827-10a0-3322-b176-b92fa3209343 | -9.05752 | -47.06744 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 725f4a27-3b5b-3dba-8c5b-4310b32693cf | -12.85557 | -52.94936 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fc465c9-f8b1-3a0a-9ce9-dc2a8c269557 | -9.89894 | -49.91389 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de0b62f9-60ad-35dd-ab39-b8bff04c58ed | -12.9683 | -54.75548 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21296c86-c310-31a6-b350-013ba797355c | -11.42824 | -43.56812 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c1c719a-c9a4-3cdc-9f8f-f79305392ab1 | -13.29609 | -43.75613 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e5d19d5-2395-32fd-b6d8-8e78c4f6530d | -13.13415 | -54.92298 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7c6e8a4-5364-362a-98e6-9d4a1fc3ecf9 | -11.47975 | -43.62745 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63638ba1-a88c-36aa-b2b6-0f33b857fd66 | -9.80754 | -47.75791 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddb962bf-cb5c-3f00-b5d7-489960bf2c0d | -10.02304 | -51.72893 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7874a9f-9559-3acd-b4e2-c21c28357ab1 | -11.49081 | -43.68336 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fdb3da7-d826-39eb-9888-693f12c75ac3 | -14.27784 | -49.40025 | 2025-09-11 04:23:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad2ddd6e-ba09-329c-8a02-bb9321ab6297 | -12.077 | -50.99664 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b0673edd-8450-34bf-93f2-f9d3fe2fac6d | -14.56411 | -48.77271 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 271f19af-9dc7-37a6-9425-9e2eecf9073f | -12.52859 | -45.34285 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 21cbb11a-649d-3d36-898b-c844f3311029 | -9.05496 | -46.9753 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36134bb5-b51a-3c5f-8720-580ad7f9280c | -9.81803 | -45.40166 | 2025-09-11 04:23:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dde338f3-7c06-3d9b-90a9-cd9cf6637db4 | -12.53025 | -45.33214 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f3460da5-0d3a-3ccb-83af-b215c0316c12 | -11.76851 | -46.47957 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ceb4d31-c087-3cfc-97cd-c31b1e9c6c37 | -11.48849 | -43.67513 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5939e711-17c6-36f9-89f2-7a48c0800533 | -8.51736 | -54.76807 | 2025-09-11 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 798e61a8-5670-38b8-ba62-3f4d5ba612aa | -13.26859 | -43.74781 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cd08398-033f-3be6-a5c0-9a5363d0ea36 | -11.97294 | -51.11416 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88dfdf20-67d3-3c0f-9d56-67bafe3e9012 | -9.78112 | -51.10461 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b95252a-99a6-3896-aa84-ffe8e88ec601 | -14.38389 | -47.33862 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 969c90fe-aefc-3612-a8d1-0be84f59d564 | -13.25684 | -43.77852 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6469ff95-6a6d-326b-99f9-c1a75b658d7d | -10.54579 | -51.52656 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e1f29261-ceb7-3606-a519-e20144bff420 | -12.0638 | -50.95391 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d77d9fa-49d6-3a35-b364-0e7920656cfa | -9.52997 | -48.30413 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0026d5d6-3e9c-3a12-8c70-6b6735625bcd | -10.17192 | -46.17916 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32465973-dfc9-3e06-8ef2-399b6ef793d2 | -11.47741 | -43.64282 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be918a0a-1caf-3800-b407-6db6270d3f75 | -11.94171 | -46.6433 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 930edc2a-5b82-383f-abcd-2778cd195947 | -11.3457 | -46.50167 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 692c2c22-35f1-33ca-be07-73ca55c79172 | -11.11263 | -48.35659 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dc6798f-a366-391b-abbf-d339fa8507ce | -9.05617 | -46.96789 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1116b41d-d058-38c4-9884-bc855b16a7be | -11.78333 | -47.32166 | 2025-09-11 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad3b0f24-f35b-384a-95f5-c58903e824c1 | -11.2211 | -54.99919 | 2025-09-11 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24cc4f95-c62c-308b-892d-dc558748851c | -10.26601 | -48.8186 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README63.md)
