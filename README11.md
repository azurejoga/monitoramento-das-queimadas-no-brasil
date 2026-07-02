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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cec0fcd7-3e58-38b3-a400-5a11eabee8a0 | -9.20121 | -45.32179 | 2026-07-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 245d34a8-292c-3da9-aca5-e94540a00bdc | -3.47252 | -39.58001 | 2026-07-02 04:17:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e6677a69-7ac5-3bc7-8402-680eb84e7f16 | -9.25425 | -46.42657 | 2026-07-02 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13a7c4c3-796e-300e-b9ab-c46610fcfcfd | -4.47312 | -40.8654 | 2026-07-02 04:17:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 392b24c2-8599-34f7-801d-51c70dbea792 | -8.65314 | -49.71388 | 2026-07-02 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 900e7054-b1fc-3d80-bc03-67c79783095b | -4.15609 | -43.08599 | 2026-07-02 04:17:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70b3d293-e80b-3d34-b3f4-73ad5e3609ce | -6.92848 | -43.72379 | 2026-07-02 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f6c29cd-2d12-3c80-ac70-fe871248cb3b | -6.91819 | -43.72211 | 2026-07-02 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 224313e1-535b-37a3-99e5-30e1b0529aa2 | -8.71377 | -48.33664 | 2026-07-02 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fdab03de-33d1-3670-9c62-9123e14b78d6 | -2.48824 | -47.09213 | 2026-07-02 04:17:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e0c7e61-3e25-3c32-97fd-d6b6385cfaa0 | -7.0049 | -42.7756 | 2026-07-02 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4944ba81-8b3b-363a-bf8c-04407bb104da | -8.71738 | -48.34148 | 2026-07-02 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dacb7ab9-590e-3e81-8cc2-e06badb773b3 | -7.90598 | -48.24204 | 2026-07-02 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49ec247b-4a94-3de1-912d-64d967f5bca7 | -9.82048 | -46.44202 | 2026-07-02 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3b914db0-d656-3f31-8c5d-7ee1e02fb829 | -6.91476 | -43.72154 | 2026-07-02 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 6d4e01b7-cbc8-3fb7-bd74-981d484f1731 | -6.92505 | -43.72323 | 2026-07-02 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac975207-4a0e-350b-8caf-427da10370f1 | -9.19474 | -45.31648 | 2026-07-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17300d9f-9787-31bd-bf12-12d85f3c55e8 | -9.20479 | -45.3224 | 2026-07-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d4902a6-29d8-3107-938e-42f9cdc7124b | -9.15816 | -47.23046 | 2026-07-02 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c115e0b-d3d7-3efe-b465-31012c1ce8e0 | -8.35622 | -46.80564 | 2026-07-02 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 983bde09-37fb-3021-91d4-c12f43cfc67c | -9.53358 | -47.75744 | 2026-07-02 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2efdd8d3-4777-3813-9b51-b5589b52121b | -8.49398 | -47.19806 | 2026-07-02 04:17:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a5a9f88-2b5f-3a98-b9d0-c7950a3094bc | -3.41689 | -41.70253 | 2026-07-02 04:17:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 906e2968-8ad7-3f48-8d12-281f23058707 | -9.15942 | -47.23254 | 2026-07-02 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4904514b-26d0-370f-9ce5-5a3499d2e18d | -9.53422 | -47.75379 | 2026-07-02 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fe6e505-5383-36eb-ad55-f52e3b8ac17b | -7.00654 | -42.78674 | 2026-07-02 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 32863b3d-956e-3d6e-9523-e42108d85410 | -8.50201 | -47.19952 | 2026-07-02 04:17:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33134750-8526-3d51-9b70-5d584bf6af76 | -2.94748 | -40.50163 | 2026-07-02 04:17:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c84301e7-a6d3-3266-b3e2-b6d9e477610e | -8.65882 | -49.70954 | 2026-07-02 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6705fb31-0c47-31e9-918f-117288d819da | -14.81408 | -49.01012 | 2026-07-02 04:19:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45648a5e-e437-31c3-b6f9-07d70df324f7 | -12.84825 | -44.34417 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1862b0cc-4972-37a2-9e9c-a05a98a9698f | -10.12353 | -52.09724 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e60a763f-9b9a-3f84-ad18-f5437228d380 | -10.47034 | -46.57874 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebd48f66-800b-393f-b061-7b57dbd15014 | -6.48732 | -43.73004 | 2026-07-02 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7746ff6-31aa-308f-ac1a-050d2333f8ea | -5.37305 | -43.37895 | 2026-07-02 04:19:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf26ff2d-796c-360c-9667-fcb9ac8dc4c8 | -10.94816 | -43.04839 | 2026-07-02 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| aa5aacfe-141c-3e58-a296-3b51bde79995 | -12.85379 | -44.35256 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| b5b142ba-ef22-3c49-b7f3-07cd157173ba | -12.78168 | -44.4974 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0f91209-6179-3411-8999-5279ddd4b22a | -12.51824 | -48.28889 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a47311e9-1298-3e62-8a5c-a54e993eee11 | -14.15956 | -52.88353 | 2026-07-02 04:19:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3261da35-a7dd-344b-8532-8f1c506f9a40 | -18.13155 | -43.97665 | 2026-07-02 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 116ad5d3-a3a7-3cf6-985d-c3c6d08a321f | -11.855 | -48.24613 | 2026-07-02 04:19:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d2f69422-b7ef-33f7-a2cc-f4922b238dbb | -15.39509 | -47.09867 | 2026-07-02 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b36ee64e-00d2-33cb-a9cc-e5d7e1c3519e | -10.78105 | -53.54548 | 2026-07-02 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4648f464-1272-3d57-b9ca-1585555c8fa4 | -9.74383 | -49.03342 | 2026-07-02 04:19:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5759bb8-ae56-3244-be6a-636667613278 | -5.79843 | -45.03329 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 318d93fc-3461-3be9-9cc9-9b1c75d21433 | -5.29674 | -43.70726 | 2026-07-02 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9176a3bc-8e7e-3125-927a-15216948a052 | -12.45378 | -46.52526 | 2026-07-02 04:19:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89365fd1-f571-3fa2-a16c-0b6ffcb3befa | -13.4634 | -47.86734 | 2026-07-02 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9b5ab5c-2c25-3a0a-8133-752ffac9e6f2 | -12.84866 | -44.36287 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 98919938-6deb-32c0-b75c-abc5ad10fb49 | -12.14126 | -45.81854 | 2026-07-02 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dc9704d-b8b4-3464-9c87-47bc63c57aee | -13.73176 | -47.89314 | 2026-07-02 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a055598c-1e05-3be5-b605-77e9e6accdbb | -14.15427 | -52.88243 | 2026-07-02 04:19:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 310c354e-cf6c-3a11-a44f-d2a13880712e | -10.36864 | -46.69637 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| a0eef32b-1968-3bc6-b0bf-7349bfe73291 | -10.37726 | -46.66904 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ed04647-cd94-32ca-8f7e-15b59e25dc3b | -12.85438 | -44.34893 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 8e89993b-0903-3a40-aeda-34546e5a62a5 | -12.75868 | -44.52795 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9bb9859-20bb-34a0-947b-d1be70093b40 | -12.85043 | -44.35199 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 456c8820-31d4-38d0-b048-f769839dd641 | -12.78625 | -44.49067 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcd8e49d-26b6-32e0-863a-5c25c414f031 | -12.85715 | -44.35313 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 2d345620-8b44-3fe1-ba5d-c31a2fc5f969 | -10.80148 | -48.56596 | 2026-07-02 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6e3e4ad-ab57-3a57-8ee3-495b5011a47f | -16.39486 | -47.41752 | 2026-07-02 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cbf7361-8339-3b76-804a-14daa54abaff | -12.7545 | -44.48964 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 58b058d0-12a1-3425-baea-5f5af78f8d30 | -12.76184 | -44.48714 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 32120ba2-dfef-305f-b1a4-91738b09637d | -12.51144 | -48.28015 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79df7428-cb09-32b3-8383-8d14d763c986 | -11.41175 | -56.06762 | 2026-07-02 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b01de849-84eb-3801-bab1-6bed93c25774 | -12.78565 | -44.49432 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cacd6745-59f6-3b46-b1a5-4037746eb1c0 | -11.79383 | -57.00576 | 2026-07-02 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 52096291-36ab-32c7-97eb-a783be4ea70a | -10.94703 | -43.05543 | 2026-07-02 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cafcec78-c3ee-3918-acce-2c960febd285 | -12.8532 | -44.35619 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| aba1cea2-f473-31fc-adfd-0b551b7c0044 | -12.75965 | -44.47926 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| db7a98c4-ad14-39cc-be05-bdb764faa819 | -12.52633 | -48.29039 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 53b6bd8d-b945-390f-917b-0b37ed3d35e1 | -10.11876 | -52.09271 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c01c91d-2a01-38c2-8656-7c7227e97538 | -12.85065 | -44.39308 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9c94f3a-eca4-3aba-a9ca-2f1d0c3b5079 | -12.84925 | -44.35925 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d3c663c9-c304-383c-96de-f48bf26cb7d8 | -11.40734 | -49.00645 | 2026-07-02 04:19:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70822756-0e89-3f9f-9850-826d11ce814a | -10.36944 | -46.69174 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 89be5e8a-3b05-32c5-b5e4-1507d2a3dd1d | -18.10077 | -45.14445 | 2026-07-02 04:19:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bcc8fc7f-57df-3254-a166-1ce77157dcaa | -11.35926 | -55.42652 | 2026-07-02 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c661c151-b690-3b75-99da-e2adc16641c6 | -10.12895 | -52.09827 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5dd0374b-53e8-37f7-9529-cf0d5443fc00 | -10.40745 | -49.4415 | 2026-07-02 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88df0f66-18bb-3236-9451-e95f6c3e8de5 | -10.12849 | -52.10453 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1eab0738-610f-3e2e-9d77-01e5a675664b | -12.77951 | -44.48953 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4a450a47-4cea-3647-8e21-e3ad8d23a4ad | -5.79772 | -45.03762 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95aaac7e-c8e8-3746-bddb-ad8257a417fe | -12.85102 | -44.34836 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| bc102099-40d5-3b54-8839-1648305f79e7 | -11.91944 | -43.38783 | 2026-07-02 04:19:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3783a33-3480-3f44-92ee-01b38a37b381 | -5.4715 | -45.42056 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3d415bb-5a30-3591-8c4c-a65aa211e4b3 | -12.75569 | -44.48233 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| c1fea35c-56c1-3541-8d1c-fc5f6bc64fb4 | -12.85833 | -44.34588 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| a3a9d0a8-9f40-3639-9f34-a551f6541451 | -12.51952 | -48.28166 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb75f56f-b640-3396-826b-304f7da0a2cc | -11.9089 | -43.38971 | 2026-07-02 04:19:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f21f2f3-7568-384d-a21b-4a746996807b | -12.77036 | -44.50299 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95ccfb30-6438-35f9-a598-ea2cb08a5097 | -12.74954 | -44.47754 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| b6c517ad-8f28-38b5-af2b-37cdd9378fb6 | -11.49167 | -47.39038 | 2026-07-02 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ba7b798-e5e7-3d63-a27a-603e1e6ed4f2 | -12.50803 | -48.27585 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2b1dac8-0c58-3382-a955-90f40ac625d6 | -12.74776 | -44.48851 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 30856116-970d-34cc-8963-7e85f93f5539 | -16.28587 | -47.01064 | 2026-07-02 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d778946-742a-336a-ba02-88bb8fe93bb9 | -10.12035 | -52.08852 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 856eadca-5ae4-3117-b13b-6f0b2ae1ef0d | -5.88776 | -46.96713 | 2026-07-02 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ff666dd-8007-3cb5-8d86-aba89f7b3d9d | -10.37484 | -46.68311 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README12.md)
