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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83a5d5ee-8a42-3a41-8132-1fcee88b40e2 | -10.75857 | -53.97507 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbbf7a88-3b47-39c4-81a7-17d352648754 | -11.28755 | -54.02761 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 423965f4-91f7-3156-be5e-e6c5a2ee3298 | -11.22847 | -53.99952 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41d92547-aebe-36b8-86db-8fd7f7ba8d03 | -10.06728 | -46.94184 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d99638e1-6683-304f-a089-c90637e0d7f6 | -14.91074 | -52.60963 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b15fa9c9-e2c3-3272-84e6-be38dd0e4d36 | -11.81964 | -47.21559 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d032fc3-0ade-3dec-82e4-6e09394333e0 | -11.71127 | -54.54333 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20d296f8-9b68-3d3a-afb8-7c74750a7947 | -14.15055 | -52.83639 | 2026-08-28 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d22b40a2-d11d-31a9-9dba-ea5b984bcbfe | -10.17541 | -48.46855 | 2026-08-28 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f2f6c1f-30a3-30e1-a212-f3256877cbc6 | -14.30041 | -51.7332 | 2026-08-28 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38ef5c97-09e8-32e9-be23-5248a6e0d044 | -11.21936 | -53.99118 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b757fd4c-4aea-3f90-887e-d31ba1c466e2 | -11.7181 | -54.52592 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2377d458-0c74-3ba4-84ce-1d21d361e5d6 | -10.79795 | -50.64639 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f6cc808-9d4a-3680-a19a-77c3c7cdf882 | -13.40715 | -51.40992 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6545ad1e-04a6-38a9-81eb-1de041a9118a | -10.93001 | -50.53798 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f6370f86-b9c9-3bd7-a37c-41a683a75af3 | -12.78047 | -46.44547 | 2026-08-28 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16d25319-ad27-356f-95ee-5d194423ae22 | -9.21134 | -51.55256 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7e40b0a-4d58-3d21-b3fe-8c38d066435e | -10.98884 | -51.08496 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b88a66eb-c34d-3d19-bb2e-9fedcc8a4a8e | -8.80884 | -50.04961 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0286c99-37cc-3b4f-9f7b-2552ef19c5c9 | -10.75714 | -54.02854 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 672dd433-f9b5-30bb-9562-1b59d9a95218 | -14.49342 | -53.40228 | 2026-08-28 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cdc4394d-a0db-33f8-aab7-54ca604ec67a | -10.61174 | -52.22519 | 2026-08-28 04:51:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b1042ad-d783-3725-b54b-d45da663637f | -10.06479 | -46.93897 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b626c609-68fe-30b6-8a88-effb497f96d2 | -8.77447 | -49.94398 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ee1cc94-b27f-3cc2-b4b3-be441f4dbcd7 | -11.49119 | -45.0642 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7afc1a22-4036-3da6-b649-ab3925e40419 | -13.45954 | -54.02321 | 2026-08-28 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6707b2c-d484-3309-9350-7fcaa89f725b | -11.22118 | -53.99823 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1bf80c0-4cef-320d-a0e3-3149c1a618c1 | -10.9916 | -51.08903 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d94e2b18-3087-3ac7-857f-a6134a995736 | -14.86469 | -52.61686 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c07b8e04-60db-3599-a8f3-41e2d39ec825 | -11.57733 | -45.53321 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fbb08e4-3ad8-3221-93c8-69c342688e41 | -13.59088 | -45.78134 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da3b3bbc-acdc-34e0-ac65-2af3f7ce118d | -10.48875 | -46.19014 | 2026-08-28 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35261098-2c88-38cc-9428-8e750422cd05 | -11.21115 | -51.24129 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 4e5b8e20-53aa-325e-8333-9a9e796e9077 | -11.27952 | -54.03064 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30c378b8-3fdd-35e4-91bf-35503ddafa23 | -13.75087 | -52.00912 | 2026-08-28 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 063f5362-253e-3932-875e-5213916c74a2 | -12.28274 | -50.58701 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9476db77-153d-3ca4-9aac-ee8cbde73748 | -9.4702 | -51.70239 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52d80c5b-8c4c-3e82-a2e0-f81fd6ba4e57 | -8.09407 | -51.67674 | 2026-08-28 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a6b66f3-d815-3e8a-afb6-1c67662a47a6 | -11.82398 | -47.21181 | 2026-08-28 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 882e4d87-f3b5-3f3b-a007-b7e0d0e17261 | -12.28384 | -50.60168 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0faef14-4f45-3538-bbf4-07341876b3f8 | -12.50178 | -43.81099 | 2026-08-28 04:51:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 452a20a7-c1a3-3709-b8be-639e310c6df2 | -9.97182 | -53.94037 | 2026-08-28 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1f75497f-8402-3d04-a16e-199def642a91 | -14.42111 | -52.59417 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 305e7707-1b71-36ab-8843-389067d6c0ff | -9.85908 | -60.26533 | 2026-08-28 04:51:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d871b584-e848-31c2-b271-811c88dedcce | -12.30266 | -47.72191 | 2026-08-28 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cf6e11d6-0d25-34c8-9bc8-26a787961d24 | -8.21979 | -54.95572 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d0969c67-faf2-36b5-8e90-18632ab9e928 | -8.6005 | -54.71669 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd1df6ff-256d-3e05-becd-4881983d4994 | -12.28107 | -50.59761 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dc0b55c-4dc9-3e4f-8016-7fd9671dcc72 | -12.29161 | -50.5957 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 641a8274-f6ef-3f44-b3e5-e3030ad517c0 | -10.75126 | -54.04099 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d0fe7fb-dca2-3f82-ae15-0ce0d33d2e18 | -9.88605 | -49.71564 | 2026-08-28 04:51:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2387db3-4123-3288-b446-ba0c6ec3e566 | -12.29549 | -50.59271 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 41e08d51-33b6-3fbc-9dc8-f13735a296c7 | -14.90858 | -52.60172 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f35ad1b-540c-3740-a3ff-d033157ed600 | -12.7851 | -46.44092 | 2026-08-28 04:51:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 376b6592-2d00-3490-aa2e-012e002f69b3 | -11.20327 | -55.08911 | 2026-08-28 04:51:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a209053-a96b-3a20-a781-e289c2fdef72 | -11.16295 | -51.20068 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30c9b777-bd62-3ae7-8179-988864f19eee | -14.42663 | -52.6027 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 032d1c1a-332a-3e04-b776-4e764e7da44d | -13.60736 | -45.78394 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5e6605b-9003-3db3-b195-16bde9927bd5 | -6.75569 | -55.68623 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74d9e040-1afd-3e8d-9cc0-f89aaeb0c2f9 | -11.02489 | -49.6588 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3be217fa-193f-363f-840c-da3c036d7436 | -11.2839 | -54.02697 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 60589e40-3298-3246-8eaa-3ff1de075830 | -11.65654 | -50.46071 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f4e69c5-22ea-365d-a77b-39eba94fb573 | -12.91905 | -59.89384 | 2026-08-28 04:51:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86745da7-28b5-324f-9d14-6847d3055e43 | -9.43637 | -51.69666 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea9fe56f-3465-392e-8385-7b4e5a8f629e | -6.82196 | -55.60928 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2e17835-df07-368b-a792-4636f1769548 | -10.76008 | -54.03352 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0981741c-bc50-3329-bd24-ef53cc2bfbec | -11.33667 | -48.37868 | 2026-08-28 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c37aceba-847b-371f-bc96-120882e6d01f | -11.7983 | -47.6645 | 2026-08-28 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 879f51ac-62f5-3c17-9e8f-6eca61f79192 | -9.21589 | -51.54579 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffd6f00c-0402-3671-8721-56aab8d939b7 | -10.79726 | -54.00645 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ff03fac-8166-38d8-a3cb-d52652542efa | -9.15691 | -49.96595 | 2026-08-28 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 890c49bc-d2e9-3f1a-b192-b4b6cb8daf65 | -9.98256 | -48.5925 | 2026-08-28 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51e756a8-d2e3-3cb1-9781-d085edb11e60 | -11.01539 | -49.65363 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da1baacf-e1f2-3e25-a065-bc0d88ae326f | -10.91825 | -50.53268 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cddae69-e9bc-3c59-acd5-bd275e5932ad | -13.40386 | -51.79298 | 2026-08-28 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f16783d-dd52-3d7f-b8f5-88fdea458dee | -11.6516 | -46.73139 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dd618427-2ce7-38ca-b542-0d1276d7ff61 | -9.43779 | -51.57797 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d74e90c7-6542-332c-9a19-2e0341e07763 | -11.20698 | -53.99786 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1ab1eb8-6f68-346b-a162-d6b9d4d78331 | -9.43697 | -51.69301 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8ef4ec5-3885-37f8-bec9-bb15f8ce29d4 | -12.69752 | -48.42753 | 2026-08-28 04:51:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6fddaa3-5fe4-3c29-88aa-31155f4f274d | -9.42811 | -51.59502 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28c6030f-e51f-3f64-9593-efc8e965a000 | -14.87224 | -52.59172 | 2026-08-28 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48da2adc-347f-3a0b-b6b0-65ef89b334ba | -11.00814 | -49.65614 | 2026-08-28 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93b36028-f1a7-309c-a516-09dfcc73af7e | -13.47889 | -57.04551 | 2026-08-28 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa900809-eb9d-3517-8412-4f4351308c8a | -10.76965 | -54.04417 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 096b2dff-8340-351c-97b2-c4754e8177cb | -9.22763 | -51.55902 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 188024af-eec1-3e39-a7c3-43173d770866 | -11.61993 | -46.73629 | 2026-08-28 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b40aaae7-35c6-35ea-a337-e368fe723a33 | -13.2825 | -46.63988 | 2026-08-28 04:51:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d255d2e-8c36-3b4f-8e28-ec1ea9b7defe | -12.25391 | -50.57506 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a7ed9a4b-8279-300b-967c-b370dfe025af | -11.16238 | -51.20421 | 2026-08-28 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44b917d7-c436-3e24-9d3b-472a310869ab | -10.75935 | -54.03786 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 86d0ebdd-e22b-349c-905e-203e4fa9c353 | -15.60071 | -46.58054 | 2026-08-28 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ddeb1c85-6dd6-3841-ba38-1ec24f2824e2 | -11.65987 | -50.46125 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f91a0920-ffac-3508-a1d1-de4d1057e73c | -11.22192 | -53.99393 | 2026-08-28 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ed21d0c-2083-32fe-97cf-bb0a3e4c5929 | -12.26611 | -50.5843 | 2026-08-28 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7844af2a-4766-3816-9e69-d4b49b3db479 | -11.48584 | -45.07182 | 2026-08-28 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08635217-68e4-3ae6-b545-c5118cd3de8c | -9.44174 | -51.57497 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da4fe859-b767-3bfb-b1e1-e237c894536e | -11.73286 | -54.55186 | 2026-08-28 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0fe163b-431f-322e-96e8-9ea588c045ae | -10.26397 | -64.51182 | 2026-08-28 04:51:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59fc199f-2759-36d2-84fd-570774799603 | -8.95191 | -50.16949 | 2026-08-28 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README38.md)
