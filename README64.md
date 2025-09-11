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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 631c615c-0ef4-3085-ae78-51e4825036e4 | -11.48029 | -43.64719 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9dfd9084-327f-3086-a99b-ea3e72f31b96 | -8.80929 | -48.09878 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d7e177b-5541-3223-b3b6-697bcf2e9acc | -10.17412 | -46.18679 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a3a5edf-a762-325f-975a-6244a0e5d967 | -10.10298 | -48.17731 | 2025-09-11 04:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a2c4c99-56f0-3e4b-80c0-dd0b6e7477fc | -11.47524 | -43.69269 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f52226a2-bb3f-3150-8731-a6bdbbe29566 | -12.11382 | -51.04766 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfa83e62-9ae7-3d79-8737-46db77df0bd9 | -12.95746 | -54.74329 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 122768be-0d46-3053-9586-763d0ff297af | -11.14546 | -45.28259 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82b69f74-6e2b-3704-94e3-582074336e98 | -11.48205 | -43.63567 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e542f531-14f7-385d-bc8e-742232019b9e | -9.70927 | -43.53145 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d45a83d-d609-39f9-83bc-fbe5f0679325 | -14.66872 | -44.0549 | 2025-09-11 04:23:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 13357b33-1ba0-3cd2-b61b-9afb4fe056b6 | -12.05569 | -47.59793 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0efd2f11-5649-3c09-a31a-9a1aab17e84c | -13.28722 | -51.71657 | 2025-09-11 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03dfa123-b9a8-36b4-b4f1-f2f3a8b0aaa2 | -15.22459 | -44.03606 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32e24cfc-3219-397a-b292-793ec366c80b | -9.06861 | -47.04239 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ea0ab852-4b99-3ba7-b895-bb1fec5c595a | -11.10396 | -48.40858 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5167206-715d-38c5-93aa-92551bd9d3f5 | -9.34127 | -48.93764 | 2025-09-11 04:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ef8b334-39f8-36bf-9d98-0134e3a4dd62 | -14.13816 | -45.41687 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f26d7a13-5617-3d2c-b69e-60d6572c72a4 | -11.60736 | -52.21679 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6a9dc77-cc55-3222-a942-737cd7a2213a | -10.55158 | -49.87108 | 2025-09-11 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4213e12-ba68-30b3-833e-6beeb52dfb66 | -13.97633 | -48.24569 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8775115-1833-3f8e-8070-7f466b296050 | -10.26734 | -43.82956 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90f42dc3-ab2b-377d-a5a4-5ff7d84d79d4 | -12.12462 | -44.85625 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e3d0cfcc-2d88-36e4-b8ab-f2a73eff61fd | -10.00635 | -51.72145 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d10e1837-2274-36be-ba24-4f025db653ca | -12.97555 | -48.03935 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29327eec-6797-3ab8-aae7-af1f025b7c37 | -9.01774 | -49.7681 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee64dc15-131e-302e-8fef-3f4cc30e3c76 | -9.06402 | -50.49225 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 773aa619-1eaa-3151-988b-dd6bbd3f8e93 | -11.41026 | -43.54544 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a91e117-e338-366f-bd11-b1bd23ca7868 | -12.95919 | -46.7298 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16d29d53-8e73-3fa9-943a-0db6ebf69b82 | -13.98275 | -46.65376 | 2025-09-11 04:23:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aae3884d-7efe-3a5a-b90e-09c76af2c9b6 | -9.30152 | -46.76984 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00b49ade-5586-34de-9b3a-4a7522e17a25 | -11.71725 | -46.50024 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73765ef0-f6da-3ab7-82fc-b8b9b6f40f4a | -11.35786 | -46.53284 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f4ec3815-ac2f-37ce-8a2e-35de358ceb5c | -15.25053 | -44.03177 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9cadb28-579c-33c9-9f23-6969fa9aa77f | -14.56559 | -48.77198 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e43503e-3127-3cdb-a997-fba3096d4737 | -9.83797 | -47.79113 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be60b6f7-c2cb-3e96-9404-f703742dcdd3 | -15.19868 | -44.04034 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c73222ab-5bfe-3232-abab-b7b27116af79 | -11.33966 | -46.47512 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1d68ff1-9ecf-3ace-bc6f-01cd76d546b8 | -12.97337 | -48.03127 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c7e7b1d-c566-3039-9601-588514ffd5e8 | -13.27221 | -51.72903 | 2025-09-11 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cfce8a7-ae50-3b9a-86d0-39e69ae188a4 | -9.51375 | -54.63858 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df26bffb-6b47-312c-8904-afafd8ca5f7c | -11.45142 | -43.57966 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27fb28f9-d453-3b21-8cc2-50523688143a | -10.65796 | -48.63942 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cb60d08-1124-397c-99da-a73a230edcac | -11.3607 | -46.515 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 058a66f9-9516-3511-9425-6de0493718da | -11.09782 | -48.44535 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6dcd6ad-5c1c-3b37-83a6-5992d847f110 | -9.00747 | -49.51792 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 587d21fc-c86e-3ce9-ac7c-2899aaa27797 | -11.02254 | -45.05622 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7f9bcddd-1f7e-3c85-b542-96c324986ee7 | -13.79102 | -46.2832 | 2025-09-11 04:23:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0dd03e8d-8691-3a31-b6ff-abf092c02d14 | -11.45431 | -43.58408 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b7d8ef2-e847-3300-95fa-e07e93058763 | -13.58315 | -47.70247 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a76f5aa6-539c-3298-838c-eac2d2cbf560 | -11.45835 | -43.60447 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 36f88bf9-6efc-3d71-a558-390ce064eb85 | -12.85527 | -52.94753 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 254c543c-0497-3e0e-b78a-47b60324ea34 | -15.20516 | -44.0455 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55763f49-a3f3-3663-bf56-89f4f55b762d | -12.98091 | -46.72246 | 2025-09-11 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 558581eb-22ad-3621-9394-70de7f7d4ab0 | -11.13096 | -48.35554 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29d24b74-7746-39d1-bd6e-f8db98d70722 | -10.54363 | -49.89449 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6d9e5c5-6475-37f0-9ab3-0f664d558571 | -11.15633 | -52.04316 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0712ea58-ecd3-30a2-a8db-c0b277b49d2c | -11.46588 | -43.60167 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ae49d6a-6dde-37e3-8625-c284af3716dd | -13.90211 | -47.99654 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f2e18cb-64fc-3ba5-97f5-587ea46019b3 | -11.39919 | -45.60539 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1b2dc0a7-3ddc-36a4-bfaf-3805a8f222b7 | -11.19813 | -48.40744 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 321af25e-e8b6-3db1-aa98-0d3afd5bda73 | -14.13477 | -45.39397 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bf990ab-f5bb-3de0-9bd4-c88bde8557c5 | -12.94676 | -54.74426 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 175f22e5-a5da-354b-8263-b22599d376f3 | -13.01641 | -48.72158 | 2025-09-11 04:23:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fccc225-2534-3ed7-9246-31d5f32c6176 | -11.37674 | -43.52547 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6af42805-a495-3263-8aea-48f3a4bbc0e2 | -11.0328 | -46.04037 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8fc43d50-f4e5-3a12-a840-ad7ca4d389f3 | -11.41142 | -43.53766 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dadfa42-171c-3d16-9c00-89a602a7c648 | -11.73182 | -46.47346 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 749befc3-a5fc-3a50-94d3-611c1af23a60 | -11.87846 | -58.82087 | 2025-09-11 04:23:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3d646aad-d26f-3135-8f6d-7c0848514538 | -9.91808 | -49.8717 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c051f7b2-48f3-398e-96b4-ef2df3470d3f | -11.44041 | -43.58191 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89662e02-c873-3ed7-a9ae-bd9343bf2292 | -9.02207 | -49.52541 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38496145-4d92-3243-b39e-d386a7c1b144 | -9.05898 | -46.97216 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d44f41d1-0aa0-3dde-afda-e1a3d686a78c | -11.39974 | -45.60187 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c34222f6-db71-3981-b37f-3b79287df7c1 | -11.14984 | -52.02889 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51ab79bf-6e70-3a5c-afec-7b1b2b9f8ceb | -14.37995 | -47.34165 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 152d0696-f03a-3cdc-bcb5-2170c83a2fb9 | -13.27154 | -51.73281 | 2025-09-11 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c2862f4-505e-3158-984b-223d74a0f4d7 | -12.53083 | -45.35053 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be9bfe92-0949-316c-b50b-7a11f20a2550 | -12.95936 | -54.74733 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd78be3c-3c33-3cb8-b852-36ee994ae271 | -12.95994 | -54.74438 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57dc4186-bf9e-3122-a252-ebcc280e562e | -12.8485 | -52.96211 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0372e6a5-3381-3164-9710-469b5b74e99b | -11.22046 | -55.00254 | 2025-09-11 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2aef4f3-d046-356c-b28f-df816e8fd9f3 | -9.10969 | -46.96207 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 230bb6fa-90a2-36ff-a1ec-0ef907e939c3 | -9.02165 | -49.76878 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 57c5d60a-617c-3e94-9da5-bc84fb3a96d3 | -9.57992 | -48.11131 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d830b1c8-9fc8-3d36-a04f-cd1df5fca84e | -9.09043 | -46.95116 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5eeae30a-2584-3e24-8824-bd381c2cb62d | -9.67929 | -46.76414 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3afa6015-17c1-3db3-ade5-0522dc4a6468 | -12.94635 | -54.81398 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5c2cb5a-f2a3-3a00-b3fd-b86c2e5153c1 | -12.92821 | -54.75898 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a947cc16-85d0-3854-ae73-2a3e79f29706 | -8.5837 | -50.8021 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d7a670c-cc80-376a-b539-bef4e433b733 | -11.08201 | -51.33381 | 2025-09-11 04:23:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 940f8045-71f1-3794-8d68-3c844a093073 | -13.01289 | -48.72099 | 2025-09-11 04:23:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b9130ab-b0ca-3417-bee7-97e17e7cceaf | -12.13753 | -44.86198 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 72cb0e36-ba81-376b-8e34-dc3e485376b7 | -11.99071 | -47.59091 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8b7170b-b00a-3d91-9b9f-91af2bf2fac2 | -11.4873 | -43.65919 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0b669b9-ea0b-3d8f-a0f8-5a7f452cd77e | -9.06436 | -47.06858 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e86fed6-5f6c-3cd3-85ac-5db835685095 | -11.43809 | -43.57362 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ee2766c-ade3-3469-9e6c-b4a3c9ef2d83 | -12.05979 | -50.95318 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c5aedbf-fa99-3772-a33b-77e487e85182 | -9.07741 | -47.07489 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee337349-ea40-3538-b71d-f09cf6e6da53 | -11.15784 | -52.03464 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README65.md)
