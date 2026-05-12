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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b7c8b20-3ed0-3404-a29b-f804fab9f559 | -13.18704 | -52.70758 | 2026-05-12 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1928dad3-f7ff-3cbf-bcd7-1e4f27b104ca | -11.29006 | -54.02509 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 733aef8b-9fb1-3a8e-895a-52d55e15d8f8 | -9.45216 | -47.79505 | 2026-05-12 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93c139ae-2690-3e9b-bf0f-fb96f7e0c491 | -9.75996 | -55.62334 | 2026-05-12 05:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89ba9623-ed50-3bd7-95bb-24e7bcb4f3e1 | -11.97045 | -46.78732 | 2026-05-12 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4909d279-3482-3c97-ac75-d070020da5e6 | -11.29367 | -54.02563 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 226eed22-96c8-31c5-88cf-0524b5be70f6 | -11.92615 | -54.10025 | 2026-05-12 05:14:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 855fb08a-adeb-3185-8768-90d45ef28239 | -13.15348 | -56.81826 | 2026-05-12 05:14:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6225cfaa-7b43-3306-9a88-45a00d775413 | -11.29852 | -54.02553 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55502fc7-75e2-34bb-b80a-41f9c6261741 | -9.45391 | -47.82162 | 2026-05-12 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48f219cf-9b33-3fd4-9f3b-57b65473c1cd | -10.63621 | -48.01481 | 2026-05-12 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0646dcb-5907-3ca5-948b-1df0a20814fc | -13.11425 | -51.72538 | 2026-05-12 05:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b45b5f9-5d3c-3ee3-ac6e-b7442042f57c | -11.2913 | -54.02444 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d1fab26-49e4-39b3-ba92-6b359f6ac8aa | -11.30213 | -54.02608 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f1f65fc-2b45-330f-bef2-65495ca2e3a9 | -11.97627 | -46.788 | 2026-05-12 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 645edb2a-861a-391d-a333-84c4bf454253 | -12.54257 | -57.22292 | 2026-05-12 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9194416e-59ce-3257-a7f4-a8b0c7cc4708 | -11.92553 | -54.10445 | 2026-05-12 05:14:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ac4c963-0e8e-3883-b843-272d95309e0d | -11.29552 | -54.02083 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29ddd99c-e9fe-31e8-99b1-9835eb551f16 | -11.95446 | -54.6758 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12604878-6749-3413-8430-d3cd793cc0b2 | -12.53924 | -57.22237 | 2026-05-12 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 24a075bf-0339-31c0-9213-d4553f1fce3d | -11.76427 | -43.63589 | 2026-05-12 05:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae08a3b0-6864-3760-bd26-14924f9106dd | -11.95505 | -54.67179 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94229cc8-0f8a-32e2-8617-b45078012cab | -11.05974 | -52.48524 | 2026-05-12 05:14:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e332af7f-8fdb-3488-b1f2-68b130a1ad36 | -10.63659 | -48.01186 | 2026-05-12 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0d7d258-f8e0-3ac0-b862-26044452cf80 | -11.00316 | -46.4855 | 2026-05-12 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f7fb0c6-101c-3c17-9df8-cc35e57d2c9b | -11.9574 | -54.68031 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9385791-b3c7-3d8f-a1ae-17717d045255 | -11.28566 | -55.79003 | 2026-05-12 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d2c253d-6574-355d-8bf9-9d983708b589 | -10.55668 | -56.32849 | 2026-05-12 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d1411a4-12b4-30d9-9ee8-d2e3b87a2832 | -11.95564 | -54.66777 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0660f9ea-ecdb-3bc6-a92d-1438af14f8c0 | -11.73767 | -54.24761 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fa4355c-fce7-3e0a-a0d4-58d555882600 | -13.1182 | -51.7246 | 2026-05-12 05:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6eb29e3f-6c1d-3f80-9d3a-f6d0cdd64b93 | -10.13147 | -47.92505 | 2026-05-12 05:14:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf661946-2d8d-38ce-a338-f8befca0decc | -11.92666 | -54.10281 | 2026-05-12 05:14:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92efe9be-85d5-3a8e-b462-7c5e32dfa0d2 | -11.95623 | -54.66376 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 377d926e-c1ed-3f9c-9d20-46b7c0f817b0 | -9.4526 | -47.79179 | 2026-05-12 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b52c900d-b069-3ecd-997c-88d926ee28ac | -11.63201 | -54.15651 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a3908f7-07a0-39cd-bfa0-4dcd866c9456 | -11.95858 | -54.6723 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f1a669a-b1e3-34fe-99e3-893a6f69bc4f | -12.53535 | -57.22537 | 2026-05-12 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad82ff1e-b0fe-3a83-901f-4a388b6f2557 | -9.42412 | -50.73244 | 2026-05-12 05:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e37ad8b1-5341-34d6-b4ef-3570927e3229 | -11.29429 | -54.02148 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c3d630e-98d2-3849-853c-8be5bc812fed | -11.75653 | -43.64174 | 2026-05-12 05:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f63f3d03-6cb9-32ee-b818-ff8118c127be | -11.73466 | -44.52617 | 2026-05-12 05:14:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| becf2ab1-4190-398d-ad9f-79e8c66117c0 | -11.98259 | -46.78455 | 2026-05-12 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a35e1e59-32b1-3fde-b6c3-843823db8b9d | -11.28229 | -55.78947 | 2026-05-12 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f6616cb-8ad6-3e7a-97f5-2cb425fc7ad3 | -13.15404 | -56.81468 | 2026-05-12 05:14:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5070815f-e975-38aa-918d-ef9d66a2d62d | -11.95799 | -54.67631 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 902e865a-6f43-3871-8083-de5c096d22ca | -11.29491 | -54.02499 | 2026-05-12 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ecfe197-e5d1-35e8-9ed0-cb746e43c788 | -11.95387 | -54.67981 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a71ef0af-6324-372b-a6ab-5de12f73967c | -9.45741 | -47.79577 | 2026-05-12 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17e1abe8-c94a-3e09-aafd-debe52d98017 | -11.95681 | -54.6843 | 2026-05-12 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8267ee88-8c41-3bff-9608-d04d45f36092 | -9.65141 | -42.95716 | 2026-05-12 05:14:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 766d492d-63ca-3261-9131-4ef6494c40f1 | -12.53868 | -57.22591 | 2026-05-12 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d13671a6-e9da-3fe3-b561-daa969c20c79 | -9.44737 | -47.79093 | 2026-05-12 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b0ba570-ee0c-3ecc-8502-d7b851228d33 | -14.14708 | -52.88549 | 2026-05-12 05:16:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1e80c476-45a5-3f03-8a65-ed6977c490dc | -20.1338 | -50.49566 | 2026-05-12 05:16:00 | NPP-375D | DOLCINÓPOLIS | SÃO PAULO | Brasil | 3514205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a94762c8-4d62-300e-a976-38d05841929c | -16.44683 | -58.15518 | 2026-05-12 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 417cfda8-61cf-3039-8558-710b0f9e4fa5 | -18.48045 | -51.70702 | 2026-05-12 05:16:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa692ad6-7654-3465-bc51-399020f287bb | -17.35425 | -51.80652 | 2026-05-12 05:16:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60b2fc79-e324-345e-a6ba-253e579fb355 | -14.14913 | -52.88995 | 2026-05-12 05:16:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ed0b3559-866d-3dfa-bb19-022575f64dc4 | -19.91772 | -54.74299 | 2026-05-12 05:16:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 922e3ea5-819a-3c97-ab9e-ba972e5d9dc7 | -14.15035 | -52.89143 | 2026-05-12 05:16:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c989afa9-2f05-3d23-acee-36c992c9c843 | -14.14239 | -52.89021 | 2026-05-12 05:16:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 086a95b3-48f8-34c5-9467-c2347669b463 | -14.14515 | -52.88932 | 2026-05-12 05:16:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d00d1e49-6bfe-3b43-8e1d-65697e8600a4 | -14.15106 | -52.88616 | 2026-05-12 05:16:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 148ebca9-521a-3222-bbd7-3599dfa6214f | -14.55257 | -58.7944 | 2026-05-12 05:16:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49e8de5d-2547-3847-b865-bdf76a22ba5b | -21.28479 | -48.60302 | 2026-05-12 05:16:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1a5f5128-005a-3274-8830-ce9adad41da0 | -18.48597 | -51.70356 | 2026-05-12 05:16:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bddf160c-c8b9-398c-8cb8-67d08655f761 | -14.55449 | -58.79046 | 2026-05-12 05:16:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de5ef261-afad-309c-9b14-90240c0f5538 | -14.14637 | -52.89077 | 2026-05-12 05:16:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fd3609f6-ab15-33bd-adc8-a7c343ee45b4 | -18.48654 | -51.69867 | 2026-05-12 05:16:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0adc653f-4598-3e2d-b872-fbed92f5cdc7 | -18.48082 | -51.70778 | 2026-05-12 05:16:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5202019-91b1-3694-90b7-9efb08c4f441 | -18.4854 | -51.7084 | 2026-05-12 05:16:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5765131b-f1fe-3662-8b83-443380936eaa | -14.54864 | -58.79747 | 2026-05-12 05:16:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fcbfd5c-6ab1-333d-9a92-9dc2a1e1fdfc | -23.54992 | -55.45842 | 2026-05-12 05:18:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e159b5f5-1871-3021-be6a-a4d97b01badb | -23.55059 | -55.45323 | 2026-05-12 05:18:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c2541acb-3f47-301f-ab2a-b813ad375a11 | -10.55375 | -56.32553 | 2026-05-12 05:31:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8cd56393-a9f2-393d-aa65-8428739bc5c1 | -11.29997 | -54.02289 | 2026-05-12 05:31:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6de9c56c-2a16-3cfd-a641-1316813cc2f7 | -11.29955 | -54.02614 | 2026-05-12 05:31:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 636cceb4-bae6-37cf-9db0-667b3e90b737 | -11.29425 | -54.02546 | 2026-05-12 05:31:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46b4f992-b692-3264-af12-58e8df48bb27 | -11.29466 | -54.02222 | 2026-05-12 05:31:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ed9f469-dc1c-329d-9a29-022e1b28080b | -10.55315 | -56.33001 | 2026-05-12 05:31:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0abfe53c-bc10-360d-aa9c-ed9903d874f0 | -9.75795 | -55.62473 | 2026-05-12 05:31:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3366569-54a4-306b-be28-1b283aa3625b | -11.73568 | -54.24814 | 2026-05-12 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88a5ee59-7c3e-30ab-a62b-47f5200ce01d | -14.14838 | -52.89161 | 2026-05-12 05:33:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efee6622-5c17-36d6-a9a7-af009861f66a | -11.95431 | -54.67417 | 2026-05-12 05:33:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e3ba424-287e-349e-b9ee-bb5cbd218552 | -14.14297 | -52.88642 | 2026-05-12 05:33:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d28c6518-28d5-3f99-a592-9038845dab50 | -11.73527 | -54.25136 | 2026-05-12 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdcf2adc-6ba2-36ed-bb38-8ed716244967 | -14.14596 | -52.8913 | 2026-05-12 05:33:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a979550-a132-3409-b373-164c607cf4a3 | -14.15234 | -52.88787 | 2026-05-12 05:33:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc10bd03-4b1d-38fc-aa44-3972e46ef480 | -11.95789 | -54.68704 | 2026-05-12 05:33:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d8ed660d-6f27-39b6-925c-5fbfe884c4d9 | -14.14246 | -52.89088 | 2026-05-12 05:33:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cee2db5a-267e-33f2-a40a-1b787a26b917 | -11.95353 | -54.68039 | 2026-05-12 05:33:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 632552e5-a1d5-32cc-b0aa-b660171b79f4 | -11.74137 | -54.24551 | 2026-05-12 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6be15b9c-1df7-30dc-9bc9-63874d3f730d | -11.9551 | -54.66792 | 2026-05-12 05:33:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebdc27d6-0cf0-3079-a594-c4b704dac7a0 | -11.95828 | -54.68396 | 2026-05-12 05:33:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ed042560-bdaf-3983-84ec-3361a6aff780 | -14.14889 | -52.88722 | 2026-05-12 05:33:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b665587c-61d0-3f34-9ec7-56a8bf9b7533 | -13.18602 | -52.70549 | 2026-05-12 05:33:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 426b57ce-1a79-3066-a114-9fe187f09491 | -12.53867 | -57.22424 | 2026-05-12 05:33:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9fe6a65-9902-3f80-b856-17119e7f5012 | -14.55435 | -58.78932 | 2026-05-12 05:33:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96d242ce-cd16-3d77-887d-31e11cb074ef | -11.95867 | -54.68087 | 2026-05-12 05:33:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README6.md)
