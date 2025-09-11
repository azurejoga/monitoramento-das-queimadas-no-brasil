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
| 2f30d22c-c94f-3f89-91e3-84731eb84235 | -11.10769 | -48.42987 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfc7edca-672f-3d86-85ae-737141b85285 | -11.21644 | -54.99476 | 2025-09-11 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4dcada2-71d9-32ce-a573-86e54172124a | -13.96111 | -48.23112 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9e8a98fd-cb43-3463-b814-6fd3d5bfe5f3 | -9.89847 | -50.16841 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d834d309-863a-3283-b2b7-1a003124635a | -11.48959 | -43.64378 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8432f728-0cc8-362a-9dd9-3732f1671acf | -12.43025 | -47.80983 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69f2680b-7061-37b8-9f2b-8740c3965da0 | -11.22638 | -55.00039 | 2025-09-11 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa335915-0be5-3534-beed-129608302291 | -9.99041 | -51.70975 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c660a59-c50f-36ff-bfb8-a1522bbcc152 | -9.0247 | -49.77441 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dab91e8e-5613-3a44-a5ba-c11732530c2f | -14.78737 | -48.22184 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d5f3005-4c9e-396a-bc85-40db6792746b | -11.14157 | -45.28558 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0d8a7a6-f1bb-3071-a0c4-51ddad08d581 | -10.7444 | -48.18315 | 2025-09-11 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd785c7e-4fb7-383a-9e7a-4da191464936 | -11.16214 | -45.307 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e03f826-c310-31da-8f88-efb3d4f8bf2f | -12.02101 | -47.57694 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2558b77f-14fd-3002-8cfd-6d6b983f8349 | -15.21635 | -44.04308 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0874d75a-8e1c-3740-8250-ae03f3e8a6da | -14.40746 | -47.32042 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e5001a6-1533-323d-b153-530882ed3cc8 | -11.43345 | -43.58083 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d60eb5ad-16cd-3362-88cb-3aa3e4e32369 | -13.83975 | -47.35112 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90745f92-473c-3bf1-bb0b-6b8af41e7b82 | -8.87949 | -48.51044 | 2025-09-11 04:23:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b590e14-d15a-3a8f-a7b5-d65975ce06ab | -8.8064 | -48.09402 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2922ea8-9008-35f4-a038-2a9c2f2e0455 | -11.43693 | -43.58137 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2fe3bfc7-32cb-346c-8f38-775fc5164f9e | -9.08366 | -47.07978 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 404b30e7-907f-3ab5-ad90-3f37af474b30 | -12.92301 | -54.78642 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 378579a8-134f-3903-9f01-303baa85ee7e | -12.42341 | -47.80867 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6adc30f-fffd-3a26-8d8f-38f72dacc5fc | -12.92475 | -54.77724 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9ecba4b-c712-3ea3-b9f0-07c9b937d1e5 | -9.09009 | -49.81654 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f760c89f-94a5-354c-89f2-55b6b208ed70 | -11.38488 | -43.5188 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 820dc0c6-a223-3add-9939-642ea8295115 | -14.78269 | -48.2289 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1859cee3-808a-3d88-860a-61d8a85b5f98 | -11.31159 | -50.75468 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8c1c9007-f082-3bf8-bbe5-1034596f8a14 | -10.01793 | -51.7324 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8feba4f-d259-3e68-9f9a-c40bfae88d1e | -14.30203 | -41.69104 | 2025-09-11 04:23:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5f2f1f40-0d1f-3386-bddc-d58257b1cb1c | -11.36236 | -46.53695 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 896e96bd-4e9f-3101-bb5b-4cd0d24f39d6 | -12.86243 | -47.96095 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5bd2b55-7814-3066-a09b-46acf6aeca7d | -13.00179 | -48.00873 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0527682d-d8a2-3999-ad38-f2a45bb298a0 | -14.39244 | -47.307 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b89b57a-e45a-3e03-b27f-8f43514641a1 | -14.91614 | -47.3094 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38025fab-145d-310f-b2bb-701dbc880bdb | -10.79265 | -45.20837 | 2025-09-11 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e92b7ad-cdad-3d53-802d-caa9d9efa422 | -11.43868 | -43.56974 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f08fe7ad-41b4-3388-b5ca-45800b495632 | -12.3982 | -54.16125 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b75f838-3926-33e5-a6b1-7eff05a15328 | -9.00586 | -49.52756 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 610a6899-9147-3ca2-9648-ebc73f083693 | -10.17823 | -44.76706 | 2025-09-11 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6fb8a25-706b-3daa-88e1-d20475d2ff8b | -9.05876 | -47.05979 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62d2a4b3-40c8-3d39-8098-dd0cf0cdbbf5 | -9.11473 | -46.97431 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eabd2827-5911-327a-8ab8-a359f8143378 | -11.47799 | -43.63899 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1990557d-1eec-3059-97e5-1d0eab9d561d | -9.04693 | -46.98157 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 64e7432d-e0bc-368b-b0d9-1e0c199a0515 | -13.03663 | -48.01108 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 617b482a-7274-332c-a176-77cfd009e024 | -11.31497 | -50.75891 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91f04904-0928-3b53-82a7-534993d82e68 | -9.07784 | -50.47971 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 341bd178-13fe-3b6a-9376-42e23553be29 | -12.42061 | -47.80434 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80f94d28-fc4e-30a3-a38a-8cd2ca9c90ca | -14.40134 | -47.31574 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aa2fb38f-9501-3eee-9629-153da10b1815 | -12.9389 | -54.75807 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd42ba77-1dfd-35ed-9d27-125e2e763683 | -9.09665 | -46.95598 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38fb9b49-9871-37a3-af94-9d2c03070b9b | -11.36294 | -46.53338 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b33dbb2f-6108-3eae-9328-c605449d718b | -14.30378 | -45.04055 | 2025-09-11 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8cf3d2b-1e08-300c-8334-07aaafba51b8 | -9.0689 | -49.8404 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b253e25-c5f3-3a58-a431-60964b47bcca | -10.54152 | -51.52577 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90d5a446-b855-38e5-b3a8-881652852fb0 | -9.98198 | -49.0599 | 2025-09-11 04:23:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1826aa5e-d023-35c0-b350-61836730d09b | -11.49192 | -43.65202 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e692d672-12de-39cb-bce2-eac2805723c6 | -13.95213 | -48.22149 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b8f3971-a1fa-3d01-ab0a-2b37a91c031c | -10.38934 | -48.57452 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f2d7274-ab52-3395-ab9c-1dd9a722835f | -12.47894 | -47.4896 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8515475a-9705-3eb4-ad12-651076600471 | -12.60303 | -56.96107 | 2025-09-11 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c546979-b859-3c78-a03c-49db45347f7d | -13.13662 | -54.91887 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60e5f021-4f33-3cfe-858d-87e846e14ded | -15.03732 | -48.08475 | 2025-09-11 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0357747e-0363-36d1-997f-05f74bf7a35c | -12.03827 | -47.55695 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e65a4204-e297-3f5f-b625-0d9a7b931695 | -12.14089 | -44.8625 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02f3e08d-c5dc-36ab-9e9d-b5ccbe8db3e1 | -12.94301 | -54.75026 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5494139-8a1b-367a-ba86-118a23b25194 | -10.78478 | -47.78509 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f3f1c64-eaf8-3bd5-877d-987bd5d89659 | -10.139 | -47.89156 | 2025-09-11 04:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29950e6b-3bbc-373e-8c07-854ea04bff2d | -13.28907 | -43.75505 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ff79dfb-be0c-325d-a3c8-fef3b7056a16 | -14.85163 | -46.7872 | 2025-09-11 04:23:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 68058cdb-17f3-3a00-9d2f-274dbb0c7ea1 | -12.47615 | -47.48535 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 52867683-7251-3e79-859a-49a2aac45833 | -11.35901 | -46.53644 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ef57072-74b2-3609-9748-097509ea37d0 | -12.05631 | -47.5942 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cdfac04d-e627-3a6c-b51e-a2617b40e845 | -11.47638 | -43.68502 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d57be5ff-a871-30ac-b459-e4403944f2ed | -11.4653 | -43.60552 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7aaef3aa-e245-3a5e-b44d-52b971b51090 | -9.34348 | -48.94703 | 2025-09-11 04:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c4497f0e-b729-3451-aea4-ec7c36d1300a | -11.45487 | -43.60394 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ec6a9ebf-72f7-319e-b8b2-7b84fd1af45f | -13.95768 | -48.23055 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 541eba7d-b08c-3365-a0c1-fcb880432455 | -9.72685 | -48.33441 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 14deafae-eb88-3d33-b0d6-156d91a8e356 | -10.14634 | -46.1678 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26855b0a-fd0c-3787-b3bd-a00f5df3a5bb | -11.50378 | -50.39603 | 2025-09-11 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ea73f95-4589-304c-8ddd-df7128655cf7 | -14.56064 | -48.77205 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| febe9d7e-4ced-3e2a-a8ad-df80fa4e87c9 | -8.80572 | -48.09816 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 658b9302-6e61-3640-91d5-52630b7f0393 | -8.04926 | -52.32957 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6d549719-9e36-36ee-990a-0e7b495d94a5 | -12.83726 | -52.94402 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 217b6421-b0bd-3d5e-98dd-6987897e0388 | -12.887 | -47.96137 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45e8505e-d17e-34df-90af-a2a6abdc369f | -14.14207 | -45.41377 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cde4280-f3c1-3529-ad58-d6cb5cf9bbb1 | -12.85281 | -52.93928 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb66157c-cd09-3886-b7f6-08edcbde56e1 | -14.40905 | -47.33182 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b55b08c-a8ae-3206-babe-8a6acb4ff65f | -12.89885 | -47.97487 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5683a0d3-b5c4-3fd2-bf02-fcf7116468e0 | -14.44594 | -48.42648 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98beb3f1-2085-3463-b1b6-99ec0300e31e | -9.90283 | -49.91458 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f58798c9-f563-3af8-b124-ed69d3d34cf8 | -9.09283 | -49.81886 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ece55ae0-1912-3b63-8459-23e063d4b0a0 | -13.29549 | -43.76011 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9cc1070-938f-3d19-bc8c-f7010c4b5bc2 | -15.58323 | -43.42516 | 2025-09-11 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 02921d42-8513-3299-8a01-1e1a1140dd2a | -10.06543 | -50.37529 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dac53ab-1b7b-34f8-b599-10636dd0e32c | -11.47485 | -49.26689 | 2025-09-11 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 980e1538-d15f-3e04-86b2-f174f9c6f9b7 | -9.71176 | -48.33667 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2285d4ab-0dd3-3d2a-ba2b-2f04dc4795bf | -13.58922 | -47.66547 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README56.md)
