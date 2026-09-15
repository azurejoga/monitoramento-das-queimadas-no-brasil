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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8280d44-2b58-3b44-bdce-5068fdbe3c82 | -10.47514 | -50.9945 | 2026-09-15 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a5c6530-c5b9-3d1d-beb8-444531b4cdc8 | -11.24238 | -43.46648 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c87a850-aa1d-350c-82ee-0b5d442253cd | -6.80849 | -43.17836 | 2026-09-15 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6edc504a-d76f-37d7-93ae-c1e5662d3eef | -10.47298 | -50.99101 | 2026-09-15 04:14:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17d1d198-456d-3a94-bd3f-f12107d25089 | -11.26181 | -54.12867 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6a5d804-68af-3fa3-a47a-7c5b8c2c6dfb | -7.084 | -42.10517 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ecb0500c-4bb8-31da-8974-2118bbd7419d | -5.61928 | -45.24554 | 2026-09-15 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8c88c52-c848-37a4-a2ff-fb5c67b0c853 | -7.55663 | -46.86632 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d7e9c47-f3ca-3437-bb36-1eaa81ba41d9 | -10.67453 | -54.13653 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfc248a7-6762-31a4-84f7-4bd7bb1620b2 | -12.12815 | -44.21778 | 2026-09-15 04:14:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3eb961f7-465b-33f3-ac3d-cf8e586a851d | -10.70306 | -47.50302 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85349e93-5829-3269-84a0-9c0e8cd80223 | -7.31506 | -39.31368 | 2026-09-15 04:14:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8a7e9f35-65a1-307a-b1e5-27466c39f4e0 | -7.2136 | -46.13616 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00ba291a-1803-32a3-80ef-38f30fabfb06 | -9.2517 | -48.54637 | 2026-09-15 04:14:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eed23d2b-6d74-33d7-915f-d4d2a875cf3f | -9.25269 | -48.54094 | 2026-09-15 04:14:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0af882e8-b446-3a03-a35f-1e0d353c2c33 | -7.1734 | -43.60879 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2692c4a-007e-3c63-b9f7-e81769921c31 | -6.51523 | -44.05561 | 2026-09-15 04:14:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 582d5db4-6bda-3777-9ba3-5570bf6dc76b | -5.1574 | -49.4363 | 2026-09-15 04:14:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f32053a-a2d5-321d-8254-7c7e09f2b876 | -7.23821 | -46.17397 | 2026-09-15 04:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 586528ca-47a0-33ae-8c2d-ad8b631a612f | -10.58699 | -47.73753 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69872d34-f8d3-3a55-a42a-adc242afc0bb | -10.94848 | -49.63831 | 2026-09-15 04:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6417c7a0-4631-330c-a11f-96a1e5ee518a | -7.13018 | -45.8667 | 2026-09-15 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f40a0ea3-59e9-3abc-89d4-174139c23e24 | -8.5027 | -50.14806 | 2026-09-15 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78f1f4fa-cde6-3012-99fc-c646e93d51cd | -8.48394 | -44.57905 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 626d4c6a-d16c-34a7-83d2-e160f032ec11 | -9.42215 | -49.55069 | 2026-09-15 04:14:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58d5e9e8-8aa3-3a17-a009-4f730c964d8b | -9.45659 | -40.38585 | 2026-09-15 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 113a0887-ee43-3e78-91c7-9c16697b520e | -12.49251 | -41.41728 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 69a373d3-4351-3527-9df1-6be2a5dfed4e | -9.35972 | -50.10835 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 82cfde3f-ba64-34d8-9eda-a623844ead11 | -11.33178 | -47.67955 | 2026-09-15 04:14:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8b7ad3d-2893-321e-9c9a-957d2defec6a | -7.45918 | -46.14476 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e657e76-9e5e-375b-ab04-76de34523d37 | -11.81406 | -46.59322 | 2026-09-15 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46645674-90f0-3c99-8e72-78d66adcc879 | -12.78716 | -47.56605 | 2026-09-15 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2be09328-74fd-3f4e-9b18-6ce9a91971ca | -13.55694 | -43.52863 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71edf1ff-abf1-356e-a45a-4e7ef5918b91 | -10.68155 | -54.17734 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c803b35-b545-3620-ae04-8fa10d25b3db | -6.78851 | -46.46107 | 2026-09-15 04:14:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a64261a4-b2e2-365a-a93e-26dec7fbbf9b | -10.57715 | -47.74017 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 280a962b-7f32-3bd2-83a4-a46c5d9a4bb1 | -10.89473 | -51.56161 | 2026-09-15 04:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| edcf399f-a154-3d79-82a8-495fc8067d54 | -10.58532 | -47.74668 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2496a28-b0cf-3246-8dd3-82a84f526d05 | -5.41479 | -48.53625 | 2026-09-15 04:14:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ebecd1ff-659b-393c-9e8b-5164177801e9 | -6.9532 | -42.5678 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aab981f7-b594-3edf-b4ec-3c9914e5bc37 | -8.39664 | -42.22224 | 2026-09-15 04:14:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 54dfdfde-13fb-393c-abb4-324f235ede78 | -6.65915 | -43.6531 | 2026-09-15 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efc4dc2d-f5c7-3102-8e91-b898cbf47eeb | -9.41644 | -50.1049 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8b8a13a4-a78c-3a50-80f1-44cdc2fe11ea | -11.88606 | -43.82705 | 2026-09-15 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b7c6d074-3a9b-3206-a67f-8037f378f1ab | -11.79631 | -46.59761 | 2026-09-15 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fe33d9f-687a-3993-899a-006056a91fca | -8.61121 | -44.46333 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac75f893-4cbd-31fa-b7ac-1f49dcaa22c5 | -7.24599 | -39.28135 | 2026-09-15 04:14:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 12c246a7-d455-3748-b66d-91a18142c77d | -8.48614 | -44.58943 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fbf66fa6-2129-3640-948c-c7ca22f3ffa0 | -11.88742 | -43.81905 | 2026-09-15 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 6f6c6df5-c84b-3a98-b519-7d4060be7e13 | -7.77713 | -49.48117 | 2026-09-15 04:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a784e645-8ffb-3b9d-b4c7-bae5b0f993ad | -11.8837 | -43.8238 | 2026-09-15 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 28d725de-e71e-354c-bed8-48b63b0d532a | -11.17238 | -42.79193 | 2026-09-15 04:14:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 291592ab-1bbd-33df-86fe-16d8d9b2dd78 | -6.61024 | -44.2084 | 2026-09-15 04:14:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09359dab-6000-3889-87e8-55e1e6fb09e3 | -10.4209 | -48.64391 | 2026-09-15 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8f80a54-b11f-3c82-b8c3-ce8d1cbdcb18 | -10.89517 | -51.56409 | 2026-09-15 04:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5bd73d20-5cc5-364a-8cbe-b98e62b2c873 | -7.09002 | -42.13317 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eb4e592c-e7f3-3de3-b885-8a069262bf1a | -9.3584 | -50.11533 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f76ff760-ec5d-33e6-868a-da4a33194ccd | -10.86137 | -46.30218 | 2026-09-15 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 152ba6c6-eeb4-3d32-a0b0-f054a287fbb2 | -5.41534 | -48.53309 | 2026-09-15 04:14:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c59aabf-de13-3a82-b898-a83bc9f2729a | -9.36137 | -50.18861 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 934372bf-1982-3cd6-a486-c0c2028714de | -7.16506 | -42.1069 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ff075b21-82e0-336d-96d3-7f1ef5bd1717 | -11.25002 | -43.46376 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bdd06a9-0a2b-36dc-a643-bc485050f7a7 | -8.48315 | -44.58379 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8d81d8e-e733-3b4a-b44e-63ece557933d | -7.29915 | -42.35278 | 2026-09-15 04:14:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3870e9f3-159f-3358-a31f-22931c891f5e | -7.08867 | -41.77792 | 2026-09-15 04:14:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36971358-1e49-33d7-9215-4e5496202cdc | -9.4197 | -47.8596 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f97ac37-1b7e-3b2c-a17a-d5d1a0c95a88 | -9.41514 | -50.11185 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88fed4ed-cd3e-3aad-b991-daed8fb8f4e1 | -7.54673 | -44.88803 | 2026-09-15 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be7fe7ec-48f5-3eff-8b50-7bd3977c88f8 | -11.2393 | -43.44179 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f290d5e-a846-30bd-9949-e7166b4f6468 | -7.24097 | -46.15765 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 16f0f49e-32c3-3529-aee2-36f207a0a080 | -7.93354 | -49.73225 | 2026-09-15 04:14:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57239ca7-b86e-3881-aaf3-b6a4a43ac5f3 | -9.84728 | -48.34659 | 2026-09-15 04:14:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b86ba32-e1c7-3674-b592-8749b20ca7b5 | -8.55939 | -44.49289 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3c17ca3d-8606-3c88-a425-2289826b42a8 | -11.23888 | -43.46588 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 394effcc-b908-36fb-a5b9-08e9ba3c9e6c | -9.15861 | -49.995 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b9a0dac-fbe5-37f6-a58c-7705b12d00d6 | -7.2332 | -46.17728 | 2026-09-15 04:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 52ed49f3-2f93-3ac4-83e6-68b648fcd959 | -11.49934 | -45.75221 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5d75e9c4-3584-3928-9dbd-0dfbb69d928b | -5.31289 | -49.25376 | 2026-09-15 04:14:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9721af5-c882-359e-b576-6ce6db32457d | -11.19198 | -42.81748 | 2026-09-15 04:14:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5e7d5073-cf5e-3777-8232-b80200354e66 | -10.03615 | -52.09237 | 2026-09-15 04:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c64362a9-c767-315d-bb08-206b3c289a0c | -7.55998 | -41.84607 | 2026-09-15 04:14:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b9fe6a16-f498-305f-96c4-dc494a903b15 | -9.35937 | -50.19918 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f91e1ea2-7f8a-3a0d-98d0-9f1ba4054cc6 | -11.81059 | -46.58881 | 2026-09-15 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0246a545-8bb2-3d17-9eb3-6af7f857d76b | -7.10097 | -41.81015 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1dc6a799-3ded-3e2a-9453-e9b646b29bff | -7.13324 | -42.12867 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b322a49f-eada-3442-89ed-4d3d2bc99c03 | -8.21186 | -43.78449 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 257c9b7c-5e4a-3020-bd2f-6afb82151763 | -8.50888 | -50.14551 | 2026-09-15 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c7dcace-6f54-30f9-bb0f-24fcc8b88cd1 | -9.36204 | -50.18509 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dd651c6b-bb54-34cb-92e2-7184cdde48bd | -7.29505 | -42.35605 | 2026-09-15 04:14:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7ecfc926-6582-335a-9d9c-2855edd2c029 | -13.30946 | -43.71621 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d0697fd-c555-38e8-8f0f-b6d86c2bc030 | -11.97643 | -52.46911 | 2026-09-15 04:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19ae1ff0-e552-38e0-89f0-a15ab11885e7 | -11.17336 | -42.80744 | 2026-09-15 04:14:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d54b5cff-9b2d-388c-8e9a-6ef9435e7a5f | -8.37212 | -54.73182 | 2026-09-15 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0285164f-4e4e-30f4-aa62-11624b2d4605 | -8.62732 | -39.26628 | 2026-09-15 04:14:00 | NPP-375D | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 95b5ec82-7204-3f87-a860-0a53ac39f2ef | -10.67752 | -54.15648 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67180085-edb4-32e3-8dba-6d642c74cca7 | -7.56338 | -41.84663 | 2026-09-15 04:14:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a9d1224e-4dbf-350c-b05b-9dd61479a0b8 | -9.35647 | -50.18095 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 570e96dc-902f-30f7-b5da-8a73bd3e88dd | -8.64187 | -48.59494 | 2026-09-15 04:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e901821-6473-3426-addf-7c12a7723e3c | -10.58166 | -47.7411 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf9c84b5-0e08-3400-a222-739676e2de3d | -7.07807 | -42.11969 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README30.md)
