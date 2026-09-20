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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f6b1829-c470-3569-b4e7-9749a933149a | -8.44951 | -45.86748 | 2026-09-20 04:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 668b9ad9-88df-3ba1-8628-2b85e50a6003 | -12.44833 | -48.25332 | 2026-09-20 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84df3e74-06f4-3e4a-87cf-fde98e112e18 | -6.34869 | -58.30727 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f9fe6f8-2fc0-3d09-99d9-1e5486a63f23 | -5.94185 | -53.82367 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec169ea9-c0b8-3e60-a614-3221366352df | -9.41757 | -48.57396 | 2026-09-20 04:40:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1544a968-f906-3ee3-b1c8-89b7be5ec51c | -6.46661 | -48.43909 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f0b5a43-aace-341e-97eb-a1612c4f5ed7 | -11.47717 | -51.47908 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 576c8c54-c9e1-37a3-94f5-17cd4a43f172 | -14.10784 | -44.8454 | 2026-09-20 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 392a769d-f58e-38e3-8137-a74c048a0e78 | -8.41007 | -54.73875 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 760211f5-ed2e-3eb4-b740-864a3286deb6 | -10.54775 | -46.74271 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6e71695-be90-37cf-943d-f9015bc17c43 | -8.7916 | -60.80138 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 47d327a5-d50c-3661-84d5-e39a25a14b15 | -10.27105 | -50.27099 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| a0c65b69-5a30-3e8c-9581-157e00ba6fc5 | -12.64603 | -50.92078 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2536454c-7b6e-3543-9c4b-6c585389c579 | -11.86171 | -47.67648 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cea0b7b4-4952-305a-8ffc-ca278ea01fbc | -8.77065 | -48.73398 | 2026-09-20 04:40:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 256eb942-98bc-3f80-9be7-85cd17230c04 | -9.82081 | -46.38681 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fda6080-27eb-36de-96c5-c203d36c25da | -13.89222 | -48.58924 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 594173ed-6eda-302e-8838-a35f8c29c769 | -10.85782 | -56.17856 | 2026-09-20 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26166972-4c1e-3f84-9f29-063c64add2aa | -10.91904 | -53.97517 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3943c075-3f00-3185-a441-6e1f806a57f4 | -11.45101 | -45.37988 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6123c025-ca9b-30df-9761-d1b262a062f5 | -9.29039 | -48.19558 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 244c84c0-0ae1-3d3b-8d11-9911cedc1c1a | -12.75939 | -46.12577 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f8d1e0a5-024b-3ad8-90c4-eafd4a03c16b | -8.06101 | -48.47433 | 2026-09-20 04:40:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e566678-a1ab-3507-a387-362a245885e8 | -11.03365 | -54.15401 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 214dd3f1-a475-305d-8425-6990c0e9559d | -11.85832 | -47.67594 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c9ada97e-ee76-387b-b802-f7ae1f472d71 | -8.76569 | -48.65837 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3e822fb-b452-39df-b219-76264a68123b | -14.17817 | -47.85961 | 2026-09-20 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58e09462-797f-3340-867a-1f54d223efd0 | -8.47393 | -45.09098 | 2026-09-20 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35c4ca93-b543-330b-a1cd-1110781c7424 | -9.03124 | -48.7613 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5c7a662-94a1-3704-810b-617cb5290635 | -11.12518 | -54.01654 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f4fdbe8d-8ac4-3b42-9e26-b9d9b7149235 | -12.06057 | -50.00393 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d68c95af-61fb-3cd8-b64c-1576bc05dbce | -11.95366 | -50.09549 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d7e9b11-a5f6-3297-a917-e8a9958a8d78 | -10.84459 | -50.93007 | 2026-09-20 04:40:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4bd105e-8a65-3db4-a408-a047ac6eda51 | -7.57645 | -57.69086 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e41e6273-fb44-3137-b51a-8fa2ecb711fe | -7.39339 | -47.7772 | 2026-09-20 04:40:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 692eb903-bf6c-3f36-b51e-c3e0a4ca9db4 | -11.48513 | -47.76148 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c5dab76-3499-396c-91c1-004deab2a291 | -11.76597 | -47.45637 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d0aaa37-7a8d-3ea8-bbb3-e469ec8d5a2d | -8.42936 | -46.86381 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e136052e-36c5-3da4-b02c-b952ffb5685c | -11.83626 | -48.84683 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2605eb39-2bf0-3828-bf45-bf228d1db953 | -10.40402 | -48.92944 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67b26ed3-f525-3a75-af77-575ed6f46a63 | -11.65698 | -43.42932 | 2026-09-20 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9edc05b6-de93-355a-bd34-6ee1c2fb2b0f | -5.84844 | -53.53071 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d25205a6-6020-36ef-9c9e-16a93c082034 | -13.88324 | -48.58056 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99e5f599-d34c-3e48-8447-55510e5ccfef | -5.8896 | -53.64432 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b266b3f3-f20c-3b91-be57-412f76ec31c6 | -13.21232 | -51.76277 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22832a98-8e24-3833-9b17-6d21af901a0b | -12.33103 | -50.70371 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64197c16-32ef-3d36-b54e-2c790f92be20 | -9.04448 | -48.76342 | 2026-09-20 04:40:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1eddd48d-9463-3670-8853-4b5ff55f2beb | -10.93057 | -53.9559 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef34b869-8f55-37d0-b914-c89b13977c33 | -9.18185 | -60.76583 | 2026-09-20 04:40:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e146177-a07b-3887-b9d5-d2a9e60198e2 | -6.48979 | -58.38459 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9cedfc04-f542-30fb-9e7b-379f6168af5a | -11.23084 | -54.0805 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d087a7af-192e-3a6a-93cc-941917ba9f87 | -13.02041 | -46.922 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec430910-187d-3cef-a101-fccc78af05f1 | -8.76734 | -48.66933 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e25b6c2f-f25f-3fc0-a3cc-219b8ba88be7 | -11.72098 | -54.62555 | 2026-09-20 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17573126-351e-3c01-84f0-db0ab3501cf5 | -10.32304 | -45.33179 | 2026-09-20 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09499374-7e66-332f-847d-268cfd6b1db1 | -8.01752 | -43.33671 | 2026-09-20 04:40:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2addf57f-bd39-34ad-a8a1-1b1fcd0bb0c8 | -13.02989 | -46.90652 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63746bfb-fb05-301e-8a21-ea960f2514bd | -11.00848 | -48.32408 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4390c282-a712-3592-b57e-c0fd0ca4f0d7 | -7.42392 | -44.74568 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a5bcb30-1632-3170-aba9-6943a51fb550 | -8.72716 | -44.87397 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc8b09df-8915-3b6e-b0bb-43ae7235d7b1 | -9.81326 | -46.38952 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93dbc401-b777-388c-82aa-b93893e819db | -8.87338 | -45.95622 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0dcf6ad-42c7-37fe-81de-5bac6ed6afa3 | -6.49178 | -58.37949 | 2026-09-20 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80f0d973-20cf-3326-90af-a4a715dfc7c4 | -12.56692 | -49.10262 | 2026-09-20 04:40:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec7e2dc2-af0c-37b3-9351-e9c8b44cf295 | -11.0201 | -54.13686 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 445cec2b-6188-3f47-802b-25b8fd827d60 | -10.87452 | -54.08866 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ad1cc4c-3bcf-3b6b-a9d0-61bbf4b2bab2 | -11.88432 | -48.99553 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15fbade9-771a-33ca-8ba5-ef001b48bd3d | -8.17226 | -54.75568 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49f0b00f-c049-3a40-87c9-f5f12437966a | -5.75355 | -57.57803 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a95c0fb-1368-39ab-9dcf-fc573e755b88 | -10.53966 | -46.72572 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34f19f68-7d25-36d7-ad22-f44c1268eac4 | -7.75155 | -49.20031 | 2026-09-20 04:40:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49becb1a-d715-3c1c-8ffc-49d1d9ba9e1e | -8.7278 | -44.86973 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 551c28bc-12ed-35fa-8fe3-ef375146c92d | -9.12777 | -45.73298 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9183cab9-302b-39ed-ab68-b9b5c1753474 | -8.61691 | -54.59291 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1c615b7-3afc-308f-824d-b2e1ece33c15 | -12.5281 | -50.07372 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc8c1b2b-a9ff-3a58-8efb-148bb3134507 | -12.55726 | -47.5679 | 2026-09-20 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1109865-6819-3f0d-afb8-985712898c70 | -11.71496 | -54.56356 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 640600e1-8a91-3443-ae46-5cc08ba50fe6 | -7.8409 | -49.21831 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8698d2e2-0c8f-3831-976c-8e532b15af0a | -11.35741 | -51.35276 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17938fc8-a835-3680-93cf-a9f3224ac5a0 | -12.75321 | -46.14246 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b1a5ac5-c24e-3288-8b90-a3e661305c01 | -11.85437 | -47.67909 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 141f1850-2559-3965-87d9-f3af2697c867 | -12.75091 | -46.20837 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a30966c7-2d70-3876-be25-0bf657c492de | -11.24708 | -54.10505 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d500d7cb-ac2b-3085-b089-ff953611b2f0 | -9.57632 | -55.1031 | 2026-09-20 04:40:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 074e76d7-9936-37e8-a68d-56d355e12ba6 | -6.81152 | -47.89136 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8136335e-51cd-3ad0-be9d-48dbc7206920 | -7.59242 | -46.73235 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c504d34e-1667-3f63-8249-0bf34a87f2a9 | -10.40622 | -48.93697 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c066b45-1c8a-3b7f-8258-88b827621f69 | -8.29513 | -50.92434 | 2026-09-20 04:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a2b147c9-1ec3-3c7f-976d-1bc17cc876be | -10.39291 | -48.91305 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f86e20a-8a03-366b-9602-260c7dcf03cb | -12.75239 | -46.17327 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2ea5c19c-187d-3fcd-94ab-ac723aa7b02d | -11.00626 | -48.31644 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55ed7a2e-d79a-3330-97b5-de251b238f44 | -12.29105 | -47.10996 | 2026-09-20 04:40:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 25e8857a-db78-3a76-856e-df519c86564c | -10.30606 | -50.2357 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 35698226-0bdf-3e33-9184-c6a618e269b3 | -5.87312 | -52.03851 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4d6e3a84-c4cd-3435-84ff-1587677e8e25 | -7.10876 | -48.41758 | 2026-09-20 04:40:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1a93fb5-40af-3479-916f-f898494228a9 | -11.48851 | -47.762 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49eab9bf-4f5e-3c45-97a9-fe8931d2e049 | -7.40616 | -46.62185 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 648abcee-c0f7-3845-b30e-2f7630257085 | -12.76175 | -46.135 | 2026-09-20 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c28299e-9d58-37e2-9850-61f43b136e61 | -7.76526 | -44.8363 | 2026-09-20 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74140fd4-c072-379f-998e-9937a0e3a62a | -11.48627 | -47.77668 | 2026-09-20 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README78.md)
