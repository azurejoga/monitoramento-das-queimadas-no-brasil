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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d35c22d-5106-356c-9223-ef2b77abfa04 | -11.59679 | -52.12507 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7c1334cb-0fb5-3595-8e74-f09b97d38577 | -12.92589 | -56.99538 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad6a7533-f380-3753-88d0-519f75d3ee10 | -6.58308 | -58.58844 | 2025-09-03 05:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5d927b0-f4c8-3232-9509-cd8acfe62db7 | -10.03999 | -56.10069 | 2025-09-03 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adf43812-6dbb-3c3c-aee5-1978af062276 | -11.58529 | -52.11032 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3f05fc62-c166-3d47-bb02-57bb006dea1c | -12.91622 | -57.01307 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4893c45-3ab3-3010-9119-711cb02fd3f4 | -12.63681 | -56.99393 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 509683d5-cc8e-396f-8b87-c37861a0f179 | -9.81284 | -54.88348 | 2025-09-03 05:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afd66af0-1c1b-3895-b39f-0dd80f7a7cf6 | -12.17824 | -53.89069 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9730d99f-34ed-3462-9161-d15602d11da9 | -14.99895 | -50.06217 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92a8846a-9d99-3e0f-8ca2-70f80faa7cf8 | -12.84594 | -48.02895 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed47ec87-ee41-38aa-9264-4dc64148c7f8 | -14.56094 | -48.05705 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7ceb4d3-c341-33d2-8eb9-966829274b1b | -11.67251 | -57.35077 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7c36783f-f1b4-3105-a271-82022ab1b303 | -12.88727 | -48.03445 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 441b0dbb-abf0-3acf-b19f-f504a2f5384c | -7.26413 | -57.54828 | 2025-09-03 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58fc8d7a-9ef8-3cb8-950e-7b98df5e2409 | -9.63992 | -47.86052 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09a4456a-15d5-3149-bce9-e53fb7721f8d | -7.53978 | -61.34307 | 2025-09-03 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dc3bc3da-750b-3d0a-9306-39222a82254a | -8.36824 | -52.53272 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93d25d93-fda5-300c-9055-f2256b4c2840 | -12.61004 | -57.00893 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe7f715a-cb4c-3000-b2b7-29958f2db517 | -11.60238 | -52.11703 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b6ec6520-7da6-3fce-9aa6-28ba31791200 | -12.91382 | -56.93554 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7e41b387-2091-307f-8640-fe14f2751a83 | -12.88986 | -56.95492 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a0e2299-5995-3341-85a1-00f46d823d55 | -12.92021 | -57.00986 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d179dda4-b76f-3c6b-8425-8abcca5121e9 | -11.67588 | -57.3513 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2897876e-6a51-3e0c-a254-195ec6491c78 | -14.77486 | -47.51336 | 2025-09-03 05:14:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 997ea9ce-d0b8-3ec4-a52b-5704f6526789 | -9.96508 | -51.62405 | 2025-09-03 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a35ed21-30a4-31ed-b820-0d07e9413881 | -11.63409 | -52.0503 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a53c5b9c-05e4-3e33-a547-f9fe10534da2 | -14.5684 | -53.02824 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4eaeb1fd-bde4-3d24-85cc-e66b8d1cd0bd | -9.14204 | -49.65454 | 2025-09-03 05:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd4d392a-0a85-3fcd-aba2-3c12cf927940 | -15.00462 | -50.05975 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 829bb1d9-118d-3bf0-a094-1d3ac2236934 | -13.10179 | -57.12217 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a194b26-f6ac-3f34-8d2a-887708f36494 | -12.93901 | -56.97816 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb12317d-84a3-3f19-8cb4-212fa8631e59 | -11.6702 | -52.17725 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a42f321b-5c34-3345-b8f7-55a2ff052afe | -11.60883 | -52.13561 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 624d3ec3-ed60-385b-861f-3da0ace01424 | -13.51202 | -47.02641 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03896bc8-33ac-3900-9620-ed6944bd3062 | -15.09375 | -48.12528 | 2025-09-03 05:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b44da043-fce8-3b4a-bdcb-3d3231ba50d5 | -7.69163 | -50.27509 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 09c283d3-70b7-33c2-a25a-10d1ff66579b | -10.90266 | -45.79602 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 256cbffe-248b-329a-8bc9-ebca4123cf15 | -11.21346 | -55.06846 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02af2e78-30f9-3861-ac83-ec52be1856e2 | -12.88679 | -48.03853 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ed130b97-fe54-3b5c-a3d6-2faa25bf4dbd | -12.91668 | -56.93986 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6588e6e6-8408-384c-9b9f-1843f3b10769 | -9.56735 | -55.38914 | 2025-09-03 05:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 563ab423-affc-3c6b-b215-6afcfe004001 | -11.6613 | -57.35642 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9467089e-00a5-3845-95ab-023e6f3e5754 | -13.69729 | -46.96167 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea5f8189-7dc6-3c8c-9136-bdf2e91b18ba | -13.45823 | -46.92986 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16e98f11-a50d-3ea7-bfd0-0eecf0142acb | -12.29256 | -50.00568 | 2025-09-03 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4082ef45-4649-3a69-8f26-5f064b8963e3 | -11.59561 | -52.13371 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4896d95b-8206-30a1-a330-8a792284032c | -12.90869 | -56.94632 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e462a28d-4689-3e2b-b46c-6a004051b3a2 | -7.78326 | -50.97068 | 2025-09-03 05:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e6fd06a-e9c5-360c-b7d4-6716e9ee122a | -12.18293 | -53.88605 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5d8966a-e1c3-3290-93e1-e1c78001e198 | -12.17896 | -53.8855 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b84f5a51-1f20-3fb5-811c-1c2c5ec6d7a6 | -8.367 | -48.29437 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 061e9ead-9b36-3d58-b115-952b48921bd8 | -12.60378 | -57.00412 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a27eb663-6910-303d-ad6e-dae1e362587f | -10.485 | -50.33305 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a32c98a-c3d9-3535-a84b-3cef45134e6a | -13.4587 | -46.92545 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12a6fb83-960e-3d91-b256-6cdebdbf34fe | -9.33899 | -55.21382 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f1bc239-c411-3e6a-9a18-833bc23827c1 | -11.79626 | -48.36044 | 2025-09-03 05:14:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 622eb7f0-aede-38e2-bac3-33880dad7631 | -14.99606 | -50.06098 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb5356cf-5f62-3a0a-a300-a4fccb6321f8 | -13.73909 | -46.93489 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4dea7b8-81ca-3223-b4f0-ff5f67035651 | -13.45777 | -46.92284 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f594ce97-021e-3d2a-988e-8484781af54e | -10.92147 | -50.85997 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ccefc443-f0af-3d77-88a4-b18eca1f5a24 | -12.93213 | -56.95395 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96969ed4-6da8-35fd-9868-f7e81e5e3f22 | -8.06054 | -52.36755 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f86e76e-d2f2-333b-8f29-66d289efdc38 | -11.60715 | -52.08211 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 362d60f0-1560-3b71-a80e-6dd7daf9089b | -12.91325 | -56.93932 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0d387d56-7e68-3817-9d9c-803305bfd31f | -11.61324 | -52.13624 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dffc53af-3e2f-35d7-bc46-4df1cc3f3ad9 | -11.06784 | -52.07756 | 2025-09-03 05:14:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4af8c59e-0790-3f19-b849-25303e769a7a | -8.82345 | -47.52052 | 2025-09-03 05:14:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9705555-ec44-39d2-944e-5599f1792794 | -11.20981 | -55.06791 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df3c162b-9695-3486-a41a-b815b75a5371 | -11.84442 | -51.41839 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b0c2b74-21d6-3460-b62c-33c3aeb054fc | -13.00902 | -48.09621 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9087ec56-a69b-398a-95a3-0eecaf0717c7 | -8.05105 | -52.36143 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e248546c-b50a-3a5d-829c-4d3f7f9674eb | -6.67692 | -58.76232 | 2025-09-03 05:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a34f213-82bb-36e4-849c-667473718afe | -9.137 | -49.65382 | 2025-09-03 05:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1575394-7784-38c3-8c89-e0018501467d | -10.47868 | -50.3434 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 084c1684-f76f-3c4d-877b-f38b26f45bff | -11.86158 | -51.54006 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf69c49c-1851-3a63-aff7-d821f9294538 | -11.00188 | -46.93425 | 2025-09-03 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ab92c82-5226-3945-8acc-62673af4b487 | -9.63289 | -47.85884 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94bf90d5-2566-379f-afa7-1cde89e1426a | -8.86391 | -52.02819 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50048942-648b-35c9-81bc-0518d5934cd8 | -13.29741 | -46.83492 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28d8274f-b04d-3ec8-91cd-2481787512dc | -14.57181 | -48.06891 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7173829-5366-3934-8151-f1fbd471a40a | -12.90634 | -48.10513 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 553f521e-c026-3efa-8ac9-3ab52c55a6fa | -9.08601 | -58.89826 | 2025-09-03 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa0d214d-82f4-3b6f-a867-5515d68fd9bf | -9.76978 | -50.01754 | 2025-09-03 05:14:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1e8528e-3e51-3b24-a323-43f7d4a42303 | -12.95101 | -56.99162 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c902b071-28c7-3b59-ac99-f2dfd1b32558 | -11.19486 | -55.01721 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1344f3d9-bd36-3d82-b63e-4e791b70ecaf | -9.6357 | -46.11699 | 2025-09-03 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1a33a03-cb67-31e8-9963-ab8939287f29 | -10.09318 | -54.76772 | 2025-09-03 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d81618d5-cd72-3e07-b326-f033dc69ad3a | -11.86097 | -51.54468 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aeb347ab-17ac-3beb-9ed2-dd9cd57974b9 | -12.93844 | -56.98193 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2e5ad16-2d11-3bdb-ba28-66ab318c1a98 | -10.91063 | -50.83222 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05832fe5-3ffc-3914-ae36-4ed79703bdc1 | -11.26782 | -48.9522 | 2025-09-03 05:14:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13122dd8-bba0-3a2e-920c-3ae635305808 | -12.92133 | -57.00237 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7a8aeb5-3fdb-3f55-bb58-d1118e20f8b0 | -9.68482 | -56.73922 | 2025-09-03 05:14:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 156349cc-dfc6-311a-9fe2-4efaf7d13bbc | -14.50802 | -53.15519 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3e28405-e9ac-3d2d-8ecb-fa117d8df0d6 | -12.90859 | -48.10574 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e27b6ca7-3c0c-3d1e-baab-9e075da84673 | -11.64678 | -52.0566 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c40f975e-9e02-3edf-935f-d8626454daf1 | -14.8337 | -46.69809 | 2025-09-03 05:16:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| ddd62ed1-ffef-3e3e-b915-cf1dab898800 | -18.06308 | -45.97768 | 2025-09-03 05:16:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 42682a5f-ed37-3935-b307-8482928dec1d | -14.83253 | -46.69317 | 2025-09-03 05:16:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |


[Clique aqui para ver as próximas entradas](README99.md)
