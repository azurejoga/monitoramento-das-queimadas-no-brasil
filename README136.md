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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bb5a046-3b5b-3210-9518-590e122d2b3a | -17.72431 | -46.13748 | 2025-09-11 12:00:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b0be0390-4aca-33ba-bb7e-cee42410d6e3 | -18.63982 | -46.92161 | 2025-09-11 12:00:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7cbe752e-96d0-382b-a767-4b884814e5ce | -20.70966 | -47.12274 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 70933886-2643-3c1a-97d2-4660bb80021b | -15.67634 | -47.02443 | 2025-09-11 12:00:00 | TERRA_M-T | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 31.7 |
| a6a1f7a3-4ede-3a4e-afb2-9d0672dc8fdd | -12.53783 | -45.33555 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| e64eb219-99b4-3a97-bf94-85c0cfbb7fbc | -20.7062 | -46.06523 | 2025-09-11 12:00:00 | TERRA_M-T | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 83a1f702-9709-3132-bc16-9351a7ef7e08 | -13.26133 | -51.74004 | 2025-09-11 12:00:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| ab4a1ecd-900e-3bd7-874f-eca8202de6b5 | -19.34656 | -49.17749 | 2025-09-11 12:00:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 09416fcc-9a5b-35f5-a80a-6f0ed1865583 | -18.37953 | -43.9783 | 2025-09-11 12:00:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 173891b1-b698-3e9d-b357-43acb065aa1b | -21.90974 | -45.55728 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 237da8bc-2045-375a-9080-b2114dc0f58e | -15.1035 | -50.16181 | 2025-09-11 12:00:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 50.5 |
| f2b47918-3082-3c04-8b42-7caeb5577502 | -13.04607 | -47.99747 | 2025-09-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| c4dac885-bf54-3bd5-8044-0b5dc355bdea | -13.61419 | -45.25659 | 2025-09-11 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5bbc13d5-8637-312d-b4ee-735939f0d9f1 | -13.26684 | -51.7091 | 2025-09-11 12:00:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 49266f12-eb10-3dae-ab23-74a301caa4db | -15.15665 | -52.44052 | 2025-09-11 12:00:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 6ac91b3c-0fa7-34ec-893c-d948035fb69b | -15.76117 | -48.04055 | 2025-09-11 12:00:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 18.0 |
| fbfa8af3-2a04-3543-a9b1-8a18fb76573c | -19.89084 | -46.33019 | 2025-09-11 12:00:00 | TERRA_M-T | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 35b1b806-6464-35bc-b4a6-0bf9a4fc45a7 | -12.68531 | -45.29811 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 38a9b184-65a1-3de0-a69f-6cd928cee6f5 | -21.19228 | -46.50078 | 2025-09-11 12:00:00 | TERRA_M-T | JURUAIA | MINAS GERAIS | Brasil | 3136900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 9a3eb25f-4e35-3622-be15-186ceacf50b5 | -19.49324 | -46.20521 | 2025-09-11 12:00:00 | TERRA_M-T | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1bd29e80-b96f-348c-8f56-45af7a4a3241 | -19.51313 | -44.23646 | 2025-09-11 12:00:00 | TERRA_M-T | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| be0953cb-5fd4-3f17-9b92-d6e31cc57ea1 | -12.88035 | -47.95579 | 2025-09-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 414aa226-6821-374f-9f5f-694c3efbaa77 | -13.78461 | -46.28188 | 2025-09-11 12:00:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 90803194-0415-3812-8028-a593691ff2cd | -17.33165 | -46.6872 | 2025-09-11 12:00:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f406df7e-2a2f-3b98-8b5a-f549b29cbfab | -21.84333 | -46.05733 | 2025-09-11 12:00:00 | TERRA_M-T | POÇO FUNDO | MINAS GERAIS | Brasil | 3151701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| ffff364f-7265-397f-81a7-467c5a48d2dc | -17.33348 | -46.67567 | 2025-09-11 12:00:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a47ee456-c381-33d1-b9e1-bfcb51e3dc0a | -14.3077 | -45.04724 | 2025-09-11 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 8b9298f4-9185-379e-82a4-ad4b8923f494 | -20.70463 | -46.07529 | 2025-09-11 12:00:00 | TERRA_M-T | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 42f6901c-6d67-34c5-8e55-66e0184642c7 | -14.30224 | -45.04012 | 2025-09-11 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5ee63829-7b03-3166-a541-221ca03e76e7 | -13.16162 | -43.27458 | 2025-09-11 12:00:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ee152643-4035-3ef3-8872-04542d22290c | -14.58464 | -43.44757 | 2025-09-11 12:00:00 | TERRA_M-T | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8c29f7cc-1ca0-33cf-bca3-edd60ad17ed3 | -19.95764 | -44.14956 | 2025-09-11 12:00:00 | TERRA_M-T | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 3d62ff96-c348-3599-811f-92b528590737 | -18.913 | -47.89525 | 2025-09-11 12:00:00 | TERRA_M-T | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 66d85580-4918-3b53-a32b-5cb8f9c9949b | -15.67229 | -47.04928 | 2025-09-11 12:00:00 | TERRA_M-T | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 8e30c6a9-6a24-30a2-9331-1a25c8827261 | -13.87338 | -40.63247 | 2025-09-11 12:00:00 | TERRA_M-T | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 6110aaa5-f664-330e-b7ad-e0c3ac9576c7 | -21.43569 | -48.91149 | 2025-09-11 12:00:00 | TERRA_M-T | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 06f75a95-e46b-38ab-ba04-47ad95375806 | -13.49907 | -51.7734 | 2025-09-11 12:00:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 2b431422-8976-3493-9645-aca81abe4a70 | -12.92179 | -47.99405 | 2025-09-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c137eaa6-06ec-3183-a683-c8d984cdfa95 | -15.67411 | -47.3686 | 2025-09-11 12:00:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 324f8d37-8435-3551-9bec-2d0aea6f851d | -20.94091 | -44.87188 | 2025-09-11 12:00:00 | TERRA_M-T | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 86a64f47-1d3b-3abe-be18-d44677a443b8 | -21.51424 | -45.91589 | 2025-09-11 12:00:00 | TERRA_M-T | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 2f294c79-78f4-3552-ad0e-9bf72453c09e | -15.62765 | -46.17794 | 2025-09-11 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e52b2c45-81fc-36c9-bff6-155e9b259fa5 | -16.28868 | -45.68217 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 378c8db3-2b38-3470-8778-761f5ad855cb | -15.67434 | -47.03667 | 2025-09-11 12:00:00 | TERRA_M-T | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ce92b9fd-38de-3bbc-be7b-af3eaf87a4ba | -17.90241 | -44.59369 | 2025-09-11 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ea59a981-77d4-3ed7-9f75-61d871fe20fd | -17.2518 | -46.08246 | 2025-09-11 12:00:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 16c1b200-e526-3230-8baa-de8d1d35f683 | -18.01524 | -44.45431 | 2025-09-11 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ab66f2b0-8851-3647-8ef5-04fcf9f29d91 | -19.16434 | -43.05131 | 2025-09-11 12:00:00 | TERRA_M-T | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| bf71b771-c356-3550-8ae3-a5c2a5f61626 | -17.65891 | -44.7396 | 2025-09-11 12:00:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3f846143-9bec-3650-aaef-1e06ff284430 | -17.83727 | -46.74052 | 2025-09-11 12:00:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c921e04a-f387-3431-947c-4885ac983031 | -13.97058 | -48.20197 | 2025-09-11 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 7469c0d9-510c-3eac-85a4-4074a848105f | -15.16265 | -52.40797 | 2025-09-11 12:00:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 19045d6f-e9d8-3e5f-b13e-cdc5b84d1c9b | -20.73768 | -42.22128 | 2025-09-11 12:00:00 | TERRA_M-T | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 852d0ded-54c9-3d60-b835-03d1d0f445db | -20.56207 | -44.94046 | 2025-09-11 12:00:00 | TERRA_M-T | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 7dae3e96-f974-3818-9724-026371cdb41c | -14.18722 | -45.47811 | 2025-09-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 71fcb494-dddf-3aa5-a5d5-7d253b127b5b | -12.83303 | -47.97342 | 2025-09-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 5b6a42e5-aab0-3b46-b8a2-45456ff6b016 | -12.67733 | -45.28582 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| a264091d-0819-3fee-b442-babd4eea5959 | -20.75244 | -46.5428 | 2025-09-11 12:00:00 | TERRA_M-T | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b9d770af-222e-377c-be0b-bf5c9f1c45df | -18.01662 | -44.44492 | 2025-09-11 12:00:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 2193db45-921d-3801-a87a-99f393e25a54 | -12.67405 | -45.30739 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 0896f1b1-9bec-38d8-9580-cd1da3c9b844 | -21.2276 | -45.79776 | 2025-09-11 12:00:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 35714abe-bdae-3fe6-be15-2461c80e44fc | -14.31236 | -45.01704 | 2025-09-11 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3d9c546f-b783-3c08-8bee-4cf3a8537c4f | -13.57956 | -47.69892 | 2025-09-11 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4267bb49-1366-346e-841b-58cfd520f109 | -12.9177 | -48.00035 | 2025-09-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 2423c963-a7ae-3aee-80e8-a077949cba57 | -13.58203 | -47.68363 | 2025-09-11 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| de25fe31-a76b-380b-be50-e85399865e79 | -21.9087 | -47.91093 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4840c455-a6d0-32fc-abf5-46bda8a93bf1 | -22.01705 | -45.6408 | 2025-09-11 12:00:00 | TERRA_M-T | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0718cf98-aba8-387d-bc5f-289722bb167b | -13.27171 | -51.74938 | 2025-09-11 12:00:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 858e9d35-3608-3e39-b15c-53687efd9392 | -13.1603 | -43.28368 | 2025-09-11 12:00:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 31583bb0-ccde-348e-97b1-e1f715ff51f4 | -21.45859 | -45.05211 | 2025-09-11 12:00:00 | TERRA_M-T | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 313091cb-7bce-3625-8347-d6c3afc9b44a | -12.61469 | -45.69527 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| a62ce76c-031f-326c-8603-285900e49eda | -12.66607 | -45.29509 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 37bfbab6-af12-396f-8ecd-ffdf99b22629 | -12.66442 | -45.30589 | 2025-09-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| e0eccf3b-7d2d-3311-9f13-5dabeb16fd70 | -13.84237 | -47.35208 | 2025-09-11 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 78022eef-7dfd-33c0-a629-97c38af5a0ec | -15.60059 | -47.61974 | 2025-09-11 12:00:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 0b8700ad-a9a3-3dc6-8eb8-2402fd7d81c7 | -15.1041 | -48.03909 | 2025-09-11 12:00:00 | TERRA_M-T | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 38.9 |
| f3926d30-bcf1-3962-9d7c-edb5cc81b749 | -21.49144 | -46.18802 | 2025-09-11 12:00:00 | TERRA_M-T | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 5c07672e-8a9a-3d6c-8f9f-0c34dc5b5c70 | -17.72267 | -46.14811 | 2025-09-11 12:00:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 5652295b-0cd8-3d4e-99be-7fd4cef459e5 | -14.42688 | -39.44925 | 2025-09-11 12:00:00 | TERRA_M-T | AURELINO LEAL | BAHIA | Brasil | 2902401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 0e44a54a-a34e-3226-b472-6074216cd459 | -20.15486 | -43.6743 | 2025-09-11 12:00:00 | TERRA_M-T | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| dfa38f9b-3cbd-35c5-92f4-b005087e5b88 | -21.67669 | -46.4785 | 2025-09-11 12:00:00 | TERRA_M-T | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f698b145-eb13-340e-86af-23722614b81e | -27.92464 | -49.31538 | 2025-09-11 12:02:00 | TERRA_M-T | URUBICI | SANTA CATARINA | Brasil | 4218905 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 2c21b12d-bf8c-3f5b-a21f-22a506cc140f | -23.35319 | -47.22145 | 2025-09-11 12:02:00 | TERRA_M-T | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 1936bb6d-16f5-3804-b5cb-3c7b2089cd51 | -23.06685 | -50.25258 | 2025-09-11 12:02:00 | TERRA_M-T | ANDIRÁ | PARANÁ | Brasil | 4101101 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| e7157587-1592-3938-aab0-399bf38b0772 | -22.97381 | -49.7374 | 2025-09-11 12:02:00 | TERRA_M-T | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.0 |
| 2e9cc96f-7d1c-3e71-9a0b-afa036d1bdca | -23.19057 | -47.08063 | 2025-09-11 12:02:00 | TERRA_M-T | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c0d5bafe-367e-3d56-8d63-7cad63c631e4 | -22.9725 | -49.73114 | 2025-09-11 12:02:00 | TERRA_M-T | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| a74f3999-8beb-31a2-b3dc-541171ec8ef6 | -22.9711 | -49.75266 | 2025-09-11 12:02:00 | TERRA_M-T | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.1 |
| 31d85a28-dadc-3d7c-90df-9830513a2a93 | -22.96991 | -49.74632 | 2025-09-11 12:02:00 | TERRA_M-T | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| 94caaef3-485a-3108-96ff-18a2ffccb453 | -23.23225 | -46.69148 | 2025-09-11 12:02:00 | TERRA_M-T | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5e19e781-dc03-3a4b-a46a-c20723f7bb06 | -23.23065 | -46.70182 | 2025-09-11 12:02:00 | TERRA_M-T | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6fd42b59-07f8-31bb-baaf-de01f83dfccd | -23.14626 | -48.25684 | 2025-09-11 12:02:00 | TERRA_M-T | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 467e2ba4-5b4b-38fb-97dd-29240252be9e | -15.6732 | -47.0389 | 2025-09-11 12:10:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 228.2 |
| 1f130957-c1cc-3e86-ad83-5ae7d77d2b1a | -11.779 | -46.4821 | 2025-09-11 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 9ed4a84c-6f41-34fd-9482-d5a019a1a581 | -14.3122 | -45.046 | 2025-09-11 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| b2b6d81f-920c-3fe0-bde8-b51ff3dcadb6 | -14.5128 | -53.9158 | 2025-09-11 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 132.0 |
| bf760eab-6d72-35fe-881c-bada9a3a825a | -8.8755 | -49.5613 | 2025-09-11 12:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| d73ca051-6e4b-36af-b3e0-761dd892f416 | -14.7525 | -46.2876 | 2025-09-11 12:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 6547c247-0161-3b70-9dd0-8a800f4dcc5b | -7.8998 | -46.2581 | 2025-09-11 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| c4a90343-8d82-358a-b64d-5bbd33c72d59 | -9.0579 | -46.9688 | 2025-09-11 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |


[Clique aqui para ver as próximas entradas](README137.md)
