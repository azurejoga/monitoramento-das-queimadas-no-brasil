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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef2685c8-a6ca-353d-a0e9-8cc0c9600ce9 | -15.58917 | -42.39273 | 2025-03-13 04:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 129954bc-78ed-36bf-aca3-0d2be96d4e0c | -8.71193 | -38.63892 | 2025-03-13 04:34:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 41d21667-e881-322e-a5e7-60457394cd71 | -15.58717 | -42.40164 | 2025-03-13 04:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fc73cfe-47c9-373e-a6fc-68be0a4ec574 | -10.65091 | -44.40173 | 2025-03-13 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37ad7347-6a42-3d3f-a52e-1f14999e45ec | -11.59704 | -44.83448 | 2025-03-13 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23b5550b-ec1d-3e0e-8acc-272b1cd385ff | -15.5885 | -42.39115 | 2025-03-13 04:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83f69972-f0eb-3246-a730-6fc165caa1f8 | -10.39248 | -47.99739 | 2025-03-13 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c33d7b00-a032-37c5-830c-433ca7b839c0 | -10.39025 | -47.98981 | 2025-03-13 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 101ec8c1-e76d-3f22-985d-e0aebd00c8b6 | -8.11276 | -43.14143 | 2025-03-13 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| c90e3255-55bd-3fac-a8a6-ba9bde7331c4 | -10.66326 | -44.39853 | 2025-03-13 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 993bc626-7c99-30b8-b6ce-0e00a190cdbd | -15.59733 | -42.39768 | 2025-03-13 04:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6175b087-7250-3213-ba73-0bacb4058d76 | -15.59391 | -42.39346 | 2025-03-13 04:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84124293-e9a2-336e-a684-c3c3a9799d89 | -10.66396 | -44.39361 | 2025-03-13 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 181e4eaf-a399-3452-ac23-3aae6f1635c8 | -10.39615 | -47.9868 | 2025-03-13 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ac2a4e1-d7a4-3f38-aaea-21f619029552 | -10.87778 | -49.55293 | 2025-03-13 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 054b318e-dd31-31b9-93a3-34f415f304d6 | -15.58855 | -42.39797 | 2025-03-13 04:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8320d011-41a0-38ec-bb84-a59f2932ad70 | -8.71144 | -38.64261 | 2025-03-13 04:34:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| de096bba-2adf-3359-865a-e6a574da75eb | -10.87168 | -49.54829 | 2025-03-13 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11c8aa99-c6dd-3713-a342-d15b5814de4d | -12.34972 | -41.27781 | 2025-03-13 04:34:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 990b577e-1051-3237-bc3a-22421af0a42b | -11.59321 | -44.83391 | 2025-03-13 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3e18111-97ec-3ad2-b04d-eb817c6d622c | -8.71651 | -38.6371 | 2025-03-13 04:34:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7e7e8f05-8f1a-3d16-9bd4-2cd25193581b | -11.5649 | -47.62021 | 2025-03-13 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c4bdff7-b46d-3b76-abee-8a19d737a612 | -12.10807 | -41.32143 | 2025-03-13 04:34:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a537ed86-f150-3774-a77f-a0ae8a8ed335 | -9.02271 | -48.80919 | 2025-03-13 04:34:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f27aa932-f3a7-3c04-a0e9-e2039ed2af39 | -10.65938 | -44.39797 | 2025-03-13 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83515735-e85a-35ee-8269-126d86749467 | -15.59324 | -42.39186 | 2025-03-13 04:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ffb7950-2f79-3314-ada4-283819277509 | -11.56097 | -47.62332 | 2025-03-13 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 005faa4b-5b1f-32db-b768-9ca2360a9ce6 | -10.87501 | -49.54884 | 2025-03-13 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e00fa29-539f-35d4-9609-a7601b5307f3 | -8.71048 | -38.63998 | 2025-03-13 04:34:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| faa6324a-e017-31c9-afa7-bf83c8f6800a | -10.39561 | -47.99033 | 2025-03-13 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8229a8e7-fbb5-39dd-bfd2-db0606681c34 | -10.87445 | -49.55239 | 2025-03-13 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cdebfde-07c8-304c-a10c-981b7a57f7d0 | -11.56772 | -47.6244 | 2025-03-13 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ea40c3d-694d-30c5-a660-c3978330c656 | -12.66831 | -44.51519 | 2025-03-13 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae52479c-2fed-3472-8f27-77e33e5c8b68 | -11.56828 | -47.62075 | 2025-03-13 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf777d30-1b68-34db-8030-c5d5f143da25 | -11.56546 | -47.61656 | 2025-03-13 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2594dca5-d584-3724-a9cc-632eeff26f3a | -11.56435 | -47.62385 | 2025-03-13 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26f20b2e-3526-3885-a04c-338ec46e1c2c | -15.59258 | -42.39708 | 2025-03-13 04:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a242e68-151c-3f33-a12c-7eb4352d6caf | -20.38767 | -49.76445 | 2025-03-13 04:36:00 | NPP-375D | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d28e081-d0c6-37c0-bb39-0835ca3477c2 | -16.61218 | -43.33105 | 2025-03-13 04:36:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b74c711b-9ca9-3327-8c45-323a76a955ba | -17.78149 | -42.80903 | 2025-03-13 04:36:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e542ecb-dc83-32c0-8b6b-983aa82c806c | -15.0764 | -48.94497 | 2025-03-13 04:36:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0479d107-abd6-31aa-8cbe-f2ea9d70b645 | -21.00327 | -44.19484 | 2025-03-13 04:36:00 | NPP-375D | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| acce38f1-cbb2-3906-aa1d-c0518bd32de8 | -17.67777 | -42.74542 | 2025-03-13 04:36:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc3fa0a3-8663-3894-8a48-040745e720e9 | -17.60806 | -49.1338 | 2025-03-13 04:36:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f64339d-1bb2-3890-b2a1-1beb1bd8a06a | -21.10538 | -49.24987 | 2025-03-13 04:36:00 | NPP-375D | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 35736032-71a3-31ce-971b-9b0063d57cdc | -17.61143 | -49.13434 | 2025-03-13 04:36:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c85692f2-2312-3d3c-8d65-9270eed07335 | -15.07974 | -48.94553 | 2025-03-13 04:36:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8d821c0-ac17-3f74-bcbf-74880f57ed9d | -21.1048 | -49.25383 | 2025-03-13 04:36:00 | NPP-375D | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6af0fc10-f9d6-32d0-860f-1464810464aa | -19.70557 | -49.85096 | 2025-03-13 04:36:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1df0611f-1271-3c8d-b88e-63bdead888bd | -20.70825 | -46.6201 | 2025-03-13 04:36:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b7fb79f-c536-35fe-a662-4b4dfe1a6f8f | -16.67997 | -43.8835 | 2025-03-13 04:36:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63d497f1-4af6-36fd-943e-0f5d6a44acb3 | -17.78168 | -42.80788 | 2025-03-13 04:36:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0ed4737-3c87-332e-964c-44b7459169a1 | -19.705 | -49.85471 | 2025-03-13 04:36:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d083b0a-012c-35c5-9cca-196a2e49a0d3 | -22.78549 | -43.75652 | 2025-03-13 04:38:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4bc6debf-3263-3e49-9090-00dcfa759cef | -22.78496 | -43.75779 | 2025-03-13 04:38:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f56c6fad-dc74-3332-a2c8-ac5f39cc7be2 | -27.13684 | -52.4657 | 2025-03-13 04:38:00 | NPP-375D | SEARA | SANTA CATARINA | Brasil | 4217501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| afb23d19-be18-3ce8-8a89-64ebe2c71ba5 | -5.4442 | -45.42875 | 2025-03-13 04:55:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57e341da-428b-324a-915f-f11b1eff6e4f | -7.2429 | -44.76915 | 2025-03-13 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32c6d79d-10f2-3523-8ea5-d1f1d736997d | -6.95367 | -43.04594 | 2025-03-13 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 187ddb35-908d-34cb-8f49-0520c1215421 | -10.66389 | -44.39824 | 2025-03-13 04:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26012079-9643-3160-8a73-6f68955c0d2e | -10.66241 | -44.39611 | 2025-03-13 04:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7997270-f308-3801-9315-35255b1f1d60 | -6.95976 | -43.04694 | 2025-03-13 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21982ea7-1c0e-3a67-a280-0de8bed71354 | -10.39318 | -47.98954 | 2025-03-13 04:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfa1b4fc-f73e-3a7c-b1c3-eadb3d2c57b3 | -10.87496 | -49.54932 | 2025-03-13 04:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 764e905f-43e4-3c2d-a6f5-2c77020548f3 | -6.22481 | -48.05539 | 2025-03-13 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c5ef991-29a5-3daa-ba73-87aef29ed8fe | -6.95304 | -43.05066 | 2025-03-13 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ab71df3-0833-3613-bf99-5c2037df6e44 | -6.95913 | -43.05169 | 2025-03-13 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6346d8c-54d9-351c-9cc5-8813c5fb7000 | -8.11425 | -43.1475 | 2025-03-13 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 01b136a0-6e1d-3bdf-887c-d13ea7ab8f3e | -6.96039 | -43.04225 | 2025-03-13 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 137fed67-7024-3151-876c-ad6bc9f4bf74 | -6.99982 | -45.61468 | 2025-03-13 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 195c56be-ef88-39d4-848a-cf1510a6f4eb | -10.87078 | -49.54873 | 2025-03-13 04:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81c01dfe-4652-3e6d-9f67-48e0bd3b76e9 | -9.02446 | -48.80858 | 2025-03-13 04:55:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56ce3a59-771f-39cf-a955-5713312b0156 | -7.24241 | -44.77281 | 2025-03-13 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7f067af-89b6-3f4a-97c8-088894231e23 | -6.96102 | -43.03757 | 2025-03-13 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d4ab1646-87b1-3245-8036-519d629b44f5 | -8.11488 | -43.14271 | 2025-03-13 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e297fee6-596d-3827-9eef-2d598d1119d1 | -15.58733 | -42.38913 | 2025-03-13 04:57:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4cc7d71c-d5fe-3ad4-944b-ace4874ea344 | -15.07895 | -48.94641 | 2025-03-13 04:57:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7d5d7913-8a20-3e5f-91d1-cb91e14c864e | -15.59368 | -42.39711 | 2025-03-13 04:57:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa5c1990-72cb-3cf3-a22f-fb97ee47e482 | -11.56451 | -47.6245 | 2025-03-13 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ef44162-52ed-31db-ab9e-b00ef6755a92 | -17.61133 | -49.13727 | 2025-03-13 04:57:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87006698-60ce-3fcf-9049-00ba6e0f1233 | -17.6066 | -49.13676 | 2025-03-13 04:57:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b88a937c-94f6-349b-ab7e-d1b694c6e991 | -11.56519 | -47.61923 | 2025-03-13 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2567db4-0a92-371a-b78b-21a84a9deea1 | -18.29856 | -54.57335 | 2025-03-13 04:59:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dc7ecd1-4507-3bbe-a8fc-950d47acd838 | -6.95087 | -43.04391 | 2025-03-13 05:21:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 020a1179-64e2-3010-851e-03843cb7b446 | -8.11033 | -43.1416 | 2025-03-13 05:21:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 02a81326-4a82-3280-9411-ec0d71c141a8 | -6.95219 | -43.03509 | 2025-03-13 05:21:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ef2e8fe9-c77b-36e4-94d1-ea5f411ac0c0 | -11.88983 | -45.27307 | 2025-03-13 05:23:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e804770a-9b38-315c-9530-5b65a49112ce | -11.58819 | -44.8303 | 2025-03-13 05:23:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fbfdcf83-0986-3729-a9dc-af3bf6fdfdc5 | -17.60585 | -49.13516 | 2025-03-13 05:25:00 | AQUA_M-M | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 005b9dde-9b17-3ee3-8676-75785346abf7 | -14.4604 | -45.3922 | 2025-03-13 10:40:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f7a3488c-9de5-3dcc-ac90-bac93d55efd5 | -11.13196 | -38.48829 | 2025-03-13 11:45:00 | TERRA_M-M | CIPÓ | BAHIA | Brasil | 2907905 | 29 | 33 | nan | nan | nan | Caatinga | 31.3 |
| a73f8613-7d21-370c-8e22-607e7eacb7d7 | -10.56456 | -37.06954 | 2025-03-13 11:45:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 208a0af1-9fb8-3087-accf-eb3888a84b7e | -10.56598 | -37.06001 | 2025-03-13 11:45:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 8ca03eed-f844-3b16-ac65-73b2be622f70 | -12.23938 | -38.81529 | 2025-03-13 11:45:00 | TERRA_M-M | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 668a99b7-c940-304c-ae0d-5a1a03527cef | -10.1148 | -45.28738 | 2025-03-13 11:45:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 03489f3a-9c5d-370e-86d2-b9effdc22369 | -7.92642 | -38.04511 | 2025-03-13 11:45:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 10cff9e8-de34-3709-a8cb-5affd55f5df4 | -21.89854 | -41.41579 | 2025-03-13 11:49:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 159587b0-b769-33c9-b022-3971a125f03c | -14.4408 | -45.3957 | 2025-03-13 11:50:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 9d029be2-28ff-3eec-94eb-04ff0fe222ac | -17.5603 | -46.4863 | 2025-03-13 12:00:00 | GOES-16 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 100.3 |
| daf84244-26ae-3f74-82f1-820120d5eb43 | -14.4408 | -45.3957 | 2025-03-13 12:20:00 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |


[Clique aqui para ver as próximas entradas](README4.md)
