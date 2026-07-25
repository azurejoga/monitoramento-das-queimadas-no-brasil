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
| 61c38a07-56fb-3afc-9736-cb188e17e61e | -11.80248 | -47.0936 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| dff90b66-8dc1-3df7-bdd7-57804f0716e6 | -12.62367 | -47.55545 | 2026-07-25 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53e5977b-b332-3923-9c23-3414a9b14fc2 | -17.68166 | -40.27926 | 2026-07-25 04:08:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 1fc6c39c-ce0a-33b1-8abb-7aa341039a94 | -11.7982 | -47.09084 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 60875088-4061-305e-a075-becd130b3598 | -10.63512 | -45.22455 | 2026-07-25 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee732f70-f4e7-3d5e-9968-98956aff3133 | -11.16777 | -46.36405 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66bc9c6e-3bfb-32be-95f7-46ab2f3d4c66 | -11.60732 | -50.14777 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fbe9e1e-de50-34be-b3e2-cbbec1be5886 | -15.58471 | -46.81527 | 2026-07-25 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 12edfaa4-31db-3eed-a31a-eabb678e121f | -12.84956 | -44.39409 | 2026-07-25 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06322d5a-aa7c-33b8-8a08-2733cca044de | -13.79108 | -47.14259 | 2026-07-25 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f7f7014-4adc-3e9d-9a4c-ad737bb8b76c | -13.29915 | -54.33814 | 2026-07-25 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec1aae80-b050-3e2a-800c-2e9fa7f726de | -11.80306 | -47.08775 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 11e43d84-04d2-3f14-aa55-61277b6f3ac6 | -11.60157 | -50.14987 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 704cdbab-062b-3418-8a39-c0502d740481 | -15.58858 | -46.81594 | 2026-07-25 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e1f012a-9e94-32f0-b120-649096596aa2 | -17.68107 | -40.28329 | 2026-07-25 04:08:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c772d6f6-4c6c-37fd-a72c-28cf85336985 | -12.42951 | -50.40999 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 306bda8d-1aa9-3234-9aa6-986dddc3c715 | -13.30595 | -54.33661 | 2026-07-25 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c917663e-44e9-35e2-84d6-a25465a6a375 | -12.43466 | -50.41105 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 563327e5-8a37-3400-8255-a9b0dbb1c786 | -11.79751 | -47.09474 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ab8788a7-6175-31cb-9b39-8aa182169002 | -13.30562 | -54.33954 | 2026-07-25 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a74249d6-fde9-37cc-9313-2f96c4d68a38 | -13.40026 | -48.16359 | 2026-07-25 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b3da467-c10e-3465-9363-5fac3b197451 | -15.4481 | -43.81075 | 2026-07-25 04:08:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c1021d7-d898-3f00-8c77-506670295f71 | -12.7039 | -43.98871 | 2026-07-25 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f976992-faba-3258-ad34-668fb3cf183c | -12.18966 | -44.49834 | 2026-07-25 04:08:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c305444b-d266-323d-b389-df01b055e08d | -11.69596 | -49.02198 | 2026-07-25 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1f2b23e-ec65-3515-aa53-65ab92c9746f | -13.77547 | -47.13598 | 2026-07-25 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8b018fe-f021-38c9-a38f-61cfc2d2cb1a | -12.45283 | -44.6961 | 2026-07-25 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae528017-54a3-3163-9344-bd615b5ed017 | -13.7809 | -47.12923 | 2026-07-25 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b6a3146-8d97-3cfe-a837-c0bc41d51502 | -11.83499 | -44.75133 | 2026-07-25 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62e51dc5-513e-3f0a-a7fd-0b7062e2b77d | -10.67842 | -46.34188 | 2026-07-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f03e95f5-99f1-338c-befe-7e12354178ed | -11.8017 | -47.09555 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a3f695c2-6d45-38b3-9a24-13b9a0e062ab | -11.79401 | -47.09003 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db16a1eb-42fa-35af-8126-146e76f8bfe1 | -13.29948 | -54.33522 | 2026-07-25 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bae1ed7b-d114-3e03-ad33-a33d8ab22a75 | -11.4342 | -47.49477 | 2026-07-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a55178cd-6202-39e5-87d1-27eeb24b7327 | -13.40464 | -48.16439 | 2026-07-25 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e64d505b-5a7c-3d6c-b2db-4a77c48a3db4 | -12.01826 | -50.492 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4a1c3da-9e1c-3a98-acda-b3a2c6404c76 | -13.61086 | -44.35596 | 2026-07-25 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97f7ab95-bf2a-3744-86ba-726c118e07fa | -14.17096 | -51.90719 | 2026-07-25 04:08:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4c8b492-817b-375c-8724-76614bb475d2 | -11.60791 | -50.14463 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5697df32-00e1-3647-bd2d-bbbab9ebc262 | -11.43496 | -47.49062 | 2026-07-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47031f2f-ac82-358d-97d1-5c3c974ee1d1 | -12.43982 | -50.4121 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02e995da-4bd2-36c4-ad08-753e997b6169 | -10.67777 | -46.34555 | 2026-07-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27100ddc-1a2c-3dc0-97a5-597c59da01d4 | -17.67759 | -40.28273 | 2026-07-25 04:08:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 40139510-d8aa-31c8-9b62-bb7e88d9d9d0 | -11.83138 | -44.75051 | 2026-07-25 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92572952-e22e-3d01-b955-fab959a4798d | -12.66394 | -48.20499 | 2026-07-25 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6920cf7b-f625-3fb0-9bb5-04721a1a0cc4 | -13.39947 | -48.16794 | 2026-07-25 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6393e3de-3ab9-3e02-b871-f61672769a0a | -13.41598 | -40.12977 | 2026-07-25 04:08:00 | NOAA-20 | ITIRUÇU | BAHIA | Brasil | 2916906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9e43cc09-437f-3bc4-89b1-99de4dd28bb8 | -14.23479 | -42.77201 | 2026-07-25 04:08:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9a297f0a-7615-331b-853c-38adf6502f99 | -14.72506 | -47.14549 | 2026-07-25 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c317c17e-4dca-3ac1-80c4-bf6b759a6bfb | -11.79483 | -47.08811 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a14b4e5c-4d53-3076-865c-69de43d3badf | -12.42374 | -50.41212 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e2a075d-70cc-332c-a97c-eae4b8b8a8dd | -15.57695 | -46.81386 | 2026-07-25 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 53b3c393-c9cf-37b7-80ba-418ab520e970 | -11.7983 | -47.0928 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4fcc6b65-4c22-3312-ad6a-819f6fd13332 | -14.16412 | -47.02391 | 2026-07-25 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9e080e4-1188-32e0-afbb-c9458353509e | -12.0324 | -50.47454 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21f0014a-71c4-33f3-b03b-98809ba8ee96 | -12.33943 | -48.22279 | 2026-07-25 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 439feb38-e6bb-3cb2-9cf8-cec7eb7adc5e | -14.72385 | -47.14503 | 2026-07-25 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d12f558a-13db-36e6-b8d1-a069f360f2d5 | -12.34025 | -48.21822 | 2026-07-25 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73d72c71-189d-3e23-93c8-18ffa83a29d1 | -10.67648 | -46.35294 | 2026-07-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2a16355-15a8-3e72-8989-8bbeca699208 | -13.30674 | -54.33419 | 2026-07-25 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cd884b5-7742-3584-ab4b-5306b3cc9f91 | -17.67471 | -40.27813 | 2026-07-25 04:08:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f2807f9a-9d33-3c08-998d-bfeadf5b7524 | -12.70108 | -43.98418 | 2026-07-25 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb11947a-9112-3189-b0dc-ae7da0e46920 | -11.80238 | -47.09165 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f6af1674-e28a-3202-8eca-31871839bda2 | -12.03225 | -50.4747 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1432f3d5-dec2-3552-88ea-5ce2bd48846a | -12.42435 | -50.40895 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4ab5a33-63f3-3c22-b6f0-1222eb0a0e14 | -12.02985 | -47.80587 | 2026-07-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63809d51-4f62-3065-8adc-1c488c4912b0 | -10.26967 | -46.73893 | 2026-07-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8f7df25-0603-3842-9d5f-a134e86818e4 | -13.47913 | -44.03683 | 2026-07-25 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f7ce4a02-0334-39fe-b2f9-705c7f708583 | -14.709 | -41.75851 | 2026-07-25 04:08:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| c36c2bbd-1761-3b5d-9000-a96d2e4b6c3f | -13.40384 | -48.16878 | 2026-07-25 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50c81a78-9ca9-3c60-ae5f-f5e7c62b674f | -14.37723 | -50.33322 | 2026-07-25 04:08:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6279096-e810-3f8e-8b87-4268a28d6bcb | -16.54399 | -43.76618 | 2026-07-25 04:08:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8982b0ee-c65a-3b05-8e6b-d741466a7809 | -12.00517 | -49.26982 | 2026-07-25 04:08:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8b6d3884-d37d-3567-b67d-0ed2d2ad1cbf | -12.13716 | -44.91695 | 2026-07-25 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f53d697c-541f-300f-ab93-684ea9a1d6c0 | -16.41167 | -54.65557 | 2026-07-25 04:10:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d657b74d-773e-3544-b7d9-3af5f4f0a58e | -18.56785 | -46.53111 | 2026-07-25 04:10:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48fbff77-042e-3e7c-9a19-ec5234b9a806 | -17.55367 | -46.5421 | 2026-07-25 04:10:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c0a5410a-494d-3c7f-a411-6da0fcd0bb29 | -18.48613 | -51.57177 | 2026-07-25 04:10:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acea7f5c-5fff-3e2e-8d9a-ae54244b4eaf | -18.84165 | -46.59991 | 2026-07-25 04:10:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8e2a0aa-48d4-3645-9a64-2a659a1872d5 | -16.41054 | -54.66069 | 2026-07-25 04:10:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb76b46b-77e4-3644-a5ef-919d4a32c600 | -18.83879 | -46.59468 | 2026-07-25 04:10:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cba219e-79ca-3cee-84c0-5c72b0a90973 | -17.55538 | -46.54484 | 2026-07-25 04:10:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d1b0339-a2a9-3027-825e-46cd6f35f2d5 | -22.66758 | -43.29889 | 2026-07-25 04:10:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ee0570ac-19ba-3c67-a344-b3aed7ed26aa | -19.71525 | -47.96843 | 2026-07-25 04:10:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e13a1b2b-6d2c-3ff0-aefa-48107e4be07f | -17.55167 | -46.54412 | 2026-07-25 04:10:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d9f1379-3878-390d-9f39-c4db66a5dd13 | -18.49108 | -51.57293 | 2026-07-25 04:10:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e64c885-e6a8-32e1-b5fa-4e354d958ce6 | -18.80728 | -53.14458 | 2026-07-25 04:10:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 87e5fcc2-de55-30b4-aed3-37a6a1a846d1 | -18.80649 | -53.14821 | 2026-07-25 04:10:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f84abef2-8373-33cc-be21-d88da1cb4c4b | -28.4266 | -49.65834 | 2026-07-25 04:12:00 | NOAA-20 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4c36b7ed-557e-3bf4-8515-ccfe6af9d437 | -2.76097 | -49.47253 | 2026-07-25 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 190b2d36-2b43-34e9-8dcf-ef7d0aaff2d6 | -2.85234 | -49.54021 | 2026-07-25 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 646eb199-14d9-3117-99a1-2e0cdba118df | -1.25662 | -50.65683 | 2026-07-25 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec899dba-a5c5-347f-9e72-f4e9c48891f6 | -1.43949 | -55.22597 | 2026-07-25 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bbc2661-8916-36be-ba7a-ef523afe3415 | -3.17142 | -48.12884 | 2026-07-25 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58badc60-493d-35b5-948c-f45716d6f8aa | -1.37443 | -48.40415 | 2026-07-25 04:49:00 | NOAA-21 | ANANINDEUA | PARÁ | Brasil | 1500800 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3dd5f52b-4cc1-3871-b492-c18787028072 | -1.59032 | -50.4363 | 2026-07-25 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54a05c55-505f-3cee-aa43-6516f9ca310c | -2.6172 | -50.83198 | 2026-07-25 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5071f578-1b17-39a4-88c7-fd4f3f76a318 | -0.92445 | -50.8247 | 2026-07-25 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89ef3e61-bb7b-3bf7-82fc-36e7668d700c | -1.40183 | -50.70757 | 2026-07-25 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c24fceea-ba14-3d65-ae05-75fb4f2ceb2c | -1.78331 | -55.52699 | 2026-07-25 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README5.md)
