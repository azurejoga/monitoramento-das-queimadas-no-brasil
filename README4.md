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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b212462d-b992-3733-bc0c-7c66080b82c4 | -17.16402 | -46.83443 | 2026-04-22 04:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 136e3e46-5bed-319c-bec5-f1512e5fdd97 | -13.98606 | -56.66185 | 2026-04-22 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58e89dc9-db36-3128-9f3f-4856612f45f6 | -13.99564 | -56.63278 | 2026-04-22 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 041056f3-a401-3472-bc77-32e5f2afd6c7 | -13.99686 | -56.6337 | 2026-04-22 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89a5f1e6-8685-3543-9286-4e00463ecca8 | -21.46777 | -48.6576 | 2026-04-22 04:49:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98bb2393-0d65-3f20-8bd7-11db02e4dd34 | -18.4065 | -51.43587 | 2026-04-22 04:49:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b10add3a-9f66-3a89-9f8f-8a74291066dc | -21.53476 | -48.90351 | 2026-04-22 04:49:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23646df1-b263-376a-a0cf-9d33b0211108 | -21.5354 | -48.89865 | 2026-04-22 04:49:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ea004a1-3357-3e4a-8223-274010ddf48c | -13.99752 | -56.62997 | 2026-04-22 04:49:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e8a95c1-66cd-3905-92c2-11a7c0bfb260 | -20.86283 | -48.62786 | 2026-04-22 04:49:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 6e4bbf7c-6345-3ada-9938-38ee694a7253 | -17.16392 | -46.83516 | 2026-04-22 04:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d24673f-6b1c-3fd5-a555-9669049fa17d | -21.46843 | -48.65252 | 2026-04-22 04:49:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe53fc62-b14c-3400-b2bc-7b6cffe50fae | -21.47161 | -48.6582 | 2026-04-22 04:49:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2aa40f5a-99d7-3285-aa0f-ca25b27f4fd1 | -24.94929 | -53.74961 | 2026-04-22 04:51:00 | NPP-375D | SÃO PEDRO DO IGUAÇU | PARANÁ | Brasil | 4125753 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6db484bb-1d06-381b-9711-cf3f2e82db47 | -24.35221 | -52.07697 | 2026-04-22 04:51:00 | NPP-375D | IRETAMA | PARANÁ | Brasil | 4110805 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ebf764c9-a770-3fb8-8b7a-4e62f6cbfb8b | -26.78876 | -48.67176 | 2026-04-22 04:51:00 | NPP-375D | PENHA | SANTA CATARINA | Brasil | 4212502 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d9e043d6-e1a8-328d-b387-25d96bfc2d51 | -22.58549 | -54.89614 | 2026-04-22 04:51:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| be3f7e7a-efde-3b9e-a652-85b2cd8cb19a | -22.68211 | -50.95122 | 2026-04-22 04:51:00 | NPP-375D | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2b0dbc01-af70-3063-86da-0d64778e82d3 | -25.2632 | -49.2821 | 2026-04-22 04:51:00 | NPP-375D | ALMIRANTE TAMANDARÉ | PARANÁ | Brasil | 4100400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 33c30148-d949-38e8-9487-761ef79a7d86 | -25.49532 | -50.27264 | 2026-04-22 04:51:00 | NPP-375D | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c4319eb2-a02c-3364-86b8-cf3f23b331d0 | -21.71176 | -48.429 | 2026-04-22 04:51:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f102142-7f74-3149-bb9f-a60c1b4a2e49 | -25.49902 | -50.27327 | 2026-04-22 04:51:00 | NPP-375D | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 94b766f5-10e0-33a3-ab67-bc62a733c063 | -21.70851 | -48.42319 | 2026-04-22 04:51:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de2de5ae-7774-36fe-88a5-6b97b6e53dde | -22.68561 | -50.95179 | 2026-04-22 04:51:00 | NPP-375D | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 14fd3899-b84e-38f7-83ce-42656da308ab | -22.58614 | -54.89226 | 2026-04-22 04:51:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 34dad249-7c3a-35fc-accb-10c65f1d6e5d | -24.91791 | -51.44155 | 2026-04-22 04:51:00 | NPP-375D | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 671030f8-6517-3506-ab0a-519dfa8c8e71 | -27.95316 | -51.06539 | 2026-04-22 04:51:00 | NPP-375D | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 89b5c80a-6400-38e7-bd51-85983f6c3912 | -25.2671 | -49.28271 | 2026-04-22 04:51:00 | NPP-375D | ALMIRANTE TAMANDARÉ | PARANÁ | Brasil | 4100400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 495c325a-2b37-3ac8-becc-964b58887344 | -21.71244 | -48.42369 | 2026-04-22 04:51:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 30883e61-d919-3044-836d-15a8262dea59 | -24.91801 | -51.4441 | 2026-04-22 04:51:00 | NPP-375D | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 73a91d93-4e8d-34e3-92d7-b89d8613c9df | 2.90261 | -60.29302 | 2026-04-22 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 542907c8-7769-34c4-b2d0-d951a90eb270 | -14.49406 | -47.76978 | 2026-04-22 05:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6be664b-62be-3d56-bccc-305590b91928 | -11.91617 | -58.07263 | 2026-04-22 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28dd9d79-9e8b-37aa-b8b2-b3544b92514b | -13.24646 | -53.29032 | 2026-04-22 05:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 644d2069-6f88-35bd-9fd4-34d152705a20 | -13.38128 | -45.334 | 2026-04-22 05:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69b1ebc4-a195-3213-a53a-4608f82cfb86 | -13.99513 | -56.63316 | 2026-04-22 05:08:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a48021d7-62a0-3e8b-bf43-ff0dd0fec19e | -12.01386 | -45.23026 | 2026-04-22 05:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b074951a-0ae8-379a-b768-b9f5f447d75d | -13.24578 | -53.29501 | 2026-04-22 05:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cbce186-69b4-3216-a8ac-ae1a3b3e0f90 | -12.02077 | -45.22591 | 2026-04-22 05:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe45f303-a5ba-383a-9ed3-db1aba17e35c | -14.49931 | -47.77005 | 2026-04-22 05:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c585c0a8-293f-37c6-8067-9043255e997e | -12.02709 | -45.22668 | 2026-04-22 05:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61205ffa-ad2d-3aac-ac32-5dc49e3a2204 | -13.98736 | -56.66137 | 2026-04-22 05:08:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bacbb65c-8a16-32cb-9c08-f04c51972be7 | -13.38305 | -45.33546 | 2026-04-22 05:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cb723dc-b064-3bea-828f-ec1f024d3f38 | -11.76866 | -43.65155 | 2026-04-22 05:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3a6df49e-ac58-3434-aa85-e1714d4f0af9 | -13.38766 | -45.33474 | 2026-04-22 05:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e01de16a-d1a8-3430-b12f-9bfd89cd0278 | -13.38361 | -45.33018 | 2026-04-22 05:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e76d0763-2e7c-3b42-87ed-2e22504bc0cc | -13.98791 | -56.65778 | 2026-04-22 05:08:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 361b5423-16ff-3389-9dbe-0664384acaf6 | -13.99568 | -56.62956 | 2026-04-22 05:08:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 320ae72a-4310-37c4-a9e1-20f18c86d0f4 | -13.99068 | -56.63981 | 2026-04-22 05:08:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43b4e000-5766-3bd1-a72c-e916fa73921e | -14.49966 | -47.76999 | 2026-04-22 05:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c166d89-8f04-3658-ab58-50c112f61df1 | -12.6381 | -52.14304 | 2026-04-22 05:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22ecc845-2be5-3e06-b4c1-389f3ae67236 | -11.91283 | -58.07207 | 2026-04-22 05:08:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a3fcf58-e952-393f-8e2b-71fefd797dca | -12.34935 | -54.77125 | 2026-04-22 05:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c29df258-7e3b-3c77-9a86-e253ffbb1f1c | -14.49372 | -47.76979 | 2026-04-22 05:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 866281e7-06cf-33a0-a3f3-fbf5a88df209 | -12.55011 | -54.61391 | 2026-04-22 05:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89e3dead-86cc-3c09-afe3-2ad238c47471 | -21.53346 | -48.90279 | 2026-04-22 05:10:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 816b5e42-c377-3c7a-9a8a-beb92ff9fa34 | -21.71279 | -48.4272 | 2026-04-22 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e56e4b9-41c8-3bbf-91ea-94098a6f7650 | -18.90156 | -56.30523 | 2026-04-22 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 856aaded-b44c-35b7-87f9-61efe38421b6 | -20.15475 | -50.9872 | 2026-04-22 05:10:00 | NOAA-20 | RUBINÉIA | SÃO PAULO | Brasil | 3544509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f39483aa-12a5-3d04-84d8-921f5717ded6 | -21.53383 | -48.89894 | 2026-04-22 05:10:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d73af527-6583-3c9e-bab5-dbe36ceccf87 | -22.68472 | -50.95603 | 2026-04-22 05:10:00 | NOAA-20 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b82f96a8-8666-30c1-9c26-4b7b898bb888 | -20.85983 | -48.62621 | 2026-04-22 05:10:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4636f752-2b1b-347b-a95c-f6c115bf8631 | -15.42096 | -56.30547 | 2026-04-22 05:10:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e3347bc-4493-3d7f-a4cb-e00f26660f4e | -18.42827 | -49.5912 | 2026-04-22 05:10:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e68bd95a-b36f-3271-b403-7fb745bdfc3a | -15.75686 | -56.69364 | 2026-04-22 05:10:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04c18aea-e1a5-3659-bf16-26d891d39588 | -20.85945 | -48.63012 | 2026-04-22 05:10:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c7836e9e-274a-3a63-9502-59f6d725aeaa | -21.4683 | -48.65718 | 2026-04-22 05:10:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90071ba7-4445-3a80-9c4e-85773d73e937 | -21.52785 | -48.90211 | 2026-04-22 05:10:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd9d980b-3ba6-3d4c-9d83-373680cd09aa | -21.70695 | -48.42695 | 2026-04-22 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68b65483-c38b-3886-8e18-6b40ac83ae35 | -21.5342 | -48.89502 | 2026-04-22 05:10:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ea7ac65-256b-3d89-8031-86e56d89481e | -22.58525 | -54.89333 | 2026-04-22 05:10:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0698c0d2-58a4-349f-af81-e1d33a569879 | -21.70737 | -48.42248 | 2026-04-22 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78d30b81-9fff-354c-9a80-f5eb0db43232 | -22.68535 | -50.94984 | 2026-04-22 05:10:00 | NOAA-20 | IEPÊ | SÃO PAULO | Brasil | 3519907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ff9dc881-7d36-31ec-802e-de9714cf5ca1 | -17.16695 | -46.83583 | 2026-04-22 05:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9284527-a56e-3a98-8184-0ebd91b06cbe | -18.70603 | -49.48816 | 2026-04-22 05:10:00 | NOAA-20 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b8f83d0-9aa6-33a4-b3d3-f4524c9551bf | -21.52822 | -48.89823 | 2026-04-22 05:10:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30fdbc22-be81-39ba-9bc1-fc316016c87c | -18.42791 | -49.59438 | 2026-04-22 05:10:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ad8aae72-af71-31e1-9054-06d76782a43b | -21.7132 | -48.42278 | 2026-04-22 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb8acd7b-3220-37d3-a70a-dbf3309a92c0 | -18.40682 | -51.43428 | 2026-04-22 05:10:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4434758f-52a3-3180-a81c-7a34cb8c690f | -18.89866 | -56.30064 | 2026-04-22 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 471733af-a596-319b-b572-0e7434b6162d | -21.4687 | -48.65302 | 2026-04-22 05:10:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a6e1f58-22e9-3fc2-81a9-f2f76a62cb50 | -24.919 | -51.44228 | 2026-04-22 05:12:00 | NOAA-20 | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f62f14c8-285b-3306-b44f-2329cda05fcb | -25.49784 | -50.27439 | 2026-04-22 05:12:00 | NOAA-20 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a3862a5e-92c7-3763-bf6a-13aae686b52f | -25.49491 | -50.27406 | 2026-04-22 05:12:00 | NOAA-20 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 49eb66ff-5757-36b7-89ff-7d53e5bca260 | -27.95019 | -51.06514 | 2026-04-22 05:12:00 | NOAA-20 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d1bb08bb-e2ca-3a1c-bfb9-6c269c5f88f4 | -25.49524 | -50.27027 | 2026-04-22 05:12:00 | NOAA-20 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 39b42ee9-5a92-3168-8a41-2eb048df01cc | -11.77512 | -43.65171 | 2026-04-22 05:40:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 83d7e43a-38b6-3609-b831-684f87caf98e | -11.76412 | -43.64463 | 2026-04-22 05:40:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 08882860-7de3-37bf-b3d0-96c9d759ccaf | -11.76412 | -43.64461 | 2026-04-22 05:40:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 3b7bfa6e-ac04-3814-ab6a-b9fb8e391ef4 | -11.77512 | -43.65173 | 2026-04-22 05:40:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 7ffca1d7-33aa-3656-8bdd-bc9d3f55def0 | -13.3761 | -45.3243 | 2026-04-22 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 225af52c-2774-339c-9deb-224e600a3d8d | -13.3761 | -45.3243 | 2026-04-22 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 27e44fdc-598a-3df7-beac-74dd2faf25f2 | -13.3761 | -45.3243 | 2026-04-22 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 7be42739-2986-39fa-b8e7-ef34a7e4020c | -13.3761 | -45.3243 | 2026-04-22 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| c6933635-d3a3-3e11-aa4e-18bcdb076108 | -13.3761 | -45.3243 | 2026-04-22 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| b8e6e354-fd8f-3b94-8fad-bb4467c7e187 | -13.3955 | -45.321 | 2026-04-22 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 375d7737-e678-335e-8666-7c558336507b | -11.78667 | -43.65582 | 2026-04-22 12:02:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c36178e8-120f-399e-937b-780aa2e41c1d | -12.23496 | -44.19263 | 2026-04-22 12:02:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d8b546d7-1e83-3cfa-91e4-40ea996eaac7 | -12.23683 | -44.17796 | 2026-04-22 12:02:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0f1845cf-9e86-32e9-90a4-ded386130a87 | -11.77517 | -43.65425 | 2026-04-22 12:02:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |


[Clique aqui para ver as próximas entradas](README5.md)
