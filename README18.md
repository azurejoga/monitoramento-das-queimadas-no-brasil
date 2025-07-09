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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 299f1518-9929-36b3-8e04-0b4f2141a919 | -15.56662 | -52.20985 | 2025-07-09 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81ef6731-558f-3b60-98ed-79f044d00a3d | -12.57802 | -56.97554 | 2025-07-09 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 824cf877-6c54-326c-b3b1-6654149d4e5d | -16.6907 | -49.3926 | 2025-07-09 04:23:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12efcda2-02fc-31ad-aaa9-de5fbeb52f5c | -11.50883 | -48.95855 | 2025-07-09 04:23:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3ed02b0-2fed-3a92-af8d-19b26fd0bbde | -14.05515 | -46.26629 | 2025-07-09 04:23:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb4679ef-1ac7-32e1-9d26-08116e8a18da | -13.10155 | -46.88165 | 2025-07-09 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06c5a016-d3f3-3b9d-908a-fec87c4b4ac6 | -11.90595 | -49.19605 | 2025-07-09 04:23:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 896cf3df-d664-37c8-9d60-c7bab466a10f | -18.97103 | -54.38158 | 2025-07-09 04:25:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5beaff8a-61be-3462-80b9-0cc77a77f823 | -21.42938 | -48.64449 | 2025-07-09 04:25:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e409f4e-49ec-3a1e-9f4d-d2a78eb9ff2a | -21.53683 | -49.52742 | 2025-07-09 04:25:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| af35b59c-a6c2-3320-9ad0-374b046202e5 | -21.53346 | -49.52678 | 2025-07-09 04:25:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d815af2a-7cec-30c3-964a-e80709f0df37 | -18.64282 | -55.7243 | 2025-07-09 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 78affc19-ad48-3757-925b-b62bf08aeff9 | -19.43816 | -44.34282 | 2025-07-09 04:25:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8fc0cd1-47cf-3f68-aa6c-dc0f987b2487 | -23.59432 | -47.43838 | 2025-07-09 04:25:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 33b50a2b-9e99-33c3-a662-f0cde6f94750 | -23.40428 | -46.55521 | 2025-07-09 04:25:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e7275e01-3260-30a7-a61a-1b1ca435a3c1 | -20.47872 | -45.20387 | 2025-07-09 04:25:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| df1ef317-2964-3d62-b3d5-de345cc35d2c | -23.98459 | -48.91893 | 2025-07-09 04:25:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d5609c6-6e57-3de3-95ca-a36d540ea5d2 | -20.39005 | -48.60534 | 2025-07-09 04:25:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2a9b799-2a01-3fcd-b891-32f64bbbed79 | -22.62351 | -47.91167 | 2025-07-09 04:25:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efbbf359-cb8e-3dea-84f4-78733cf10d03 | -23.63124 | -46.42678 | 2025-07-09 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 062e2aec-7058-3159-80d7-c55c70a79cb5 | -19.08951 | -56.04765 | 2025-07-09 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8c05e0dc-4a75-3b3f-867b-038a7460f6ed | -24.17643 | -53.03862 | 2025-07-09 04:25:00 | NPP-375D | GOIOERÊ | PARANÁ | Brasil | 4108601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6d637bb7-9e07-306b-af78-4c028804d2d7 | -20.42049 | -45.58299 | 2025-07-09 04:25:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7b9ee7a-04e3-3ffe-a916-9e7d7997f6b1 | -23.40775 | -46.55574 | 2025-07-09 04:25:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2338ed7d-a6ca-3861-b365-6b103c304a55 | -22.85421 | -42.9809 | 2025-07-09 04:25:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ca838469-b799-3492-aec3-19c67af59af3 | -19.65307 | -49.47767 | 2025-07-09 04:25:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a474264-ae93-35c8-bbba-32acad150267 | -24.24207 | -50.74119 | 2025-07-09 04:25:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0476fd97-4102-3064-a3e1-b61e428d4807 | -22.61959 | -47.91484 | 2025-07-09 04:25:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b182928b-959e-35c5-9468-195e5bfd384b | -22.8569 | -45.2202 | 2025-07-09 04:25:00 | NPP-375D | APARECIDA | SÃO PAULO | Brasil | 3502507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 332abc03-e327-382e-8d80-5717db289b4e | -19.73847 | -47.44126 | 2025-07-09 04:25:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3b2c6e0-0c7b-318a-b833-c35297063b37 | -22.74861 | -43.27548 | 2025-07-09 04:25:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1ff3ea8f-abb3-3f60-a89b-78ac76cb1fe5 | -18.09069 | -54.28624 | 2025-07-09 04:25:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67729f0e-3398-3ba6-8ef3-70455da79d3d | -20.69907 | -45.09322 | 2025-07-09 04:25:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1aa0f3dd-a4f1-3bd3-b386-43b822452ab4 | -21.63519 | -49.84167 | 2025-07-09 04:25:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f832a347-0e3c-39a6-b1dd-a11a19e692d4 | -18.6454 | -55.73661 | 2025-07-09 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 65611ea3-df25-3177-ab35-182be8dd00e1 | -22.62235 | -47.91921 | 2025-07-09 04:25:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eda8dd5e-e875-3f26-aa38-47baa37e3dc0 | -23.45171 | -46.70288 | 2025-07-09 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1296c51c-42cf-339a-bdbd-733f2ab94fd2 | -22.62293 | -47.91544 | 2025-07-09 04:25:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee9a0ad8-eec5-348f-8781-a0182651ef71 | -19.96219 | -44.68841 | 2025-07-09 04:25:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64c7f2bb-c0bf-3792-9e18-949812a81224 | -18.40484 | -44.19361 | 2025-07-09 04:25:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efad0117-3962-399a-bbd5-5f6cc3afc9c9 | -21.04971 | -45.27631 | 2025-07-09 04:25:00 | NPP-375D | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 80fb1f09-0c28-3668-a573-51d6120f7269 | -20.85914 | -55.29556 | 2025-07-09 04:25:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6df58fd1-d7e2-3d5b-8be9-f9b2c66e0b28 | -23.54732 | -47.63639 | 2025-07-09 04:25:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b1f12777-895c-3857-9313-3b0bc652367f | -19.33277 | -54.43198 | 2025-07-09 04:25:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba36e7f1-b0cf-3fc9-9e65-3bd2d6033c7b | -18.63799 | -55.72321 | 2025-07-09 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 69dce62d-2170-3392-b064-b0df859d3b0d | -22.69865 | -43.34833 | 2025-07-09 04:25:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 112861ab-7467-374a-ac76-3eb504f61716 | -19.89985 | -41.74085 | 2025-07-09 04:25:00 | NPP-375D | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9b9343a1-9f25-3cb8-b1b3-6383f88c41de | -18.40121 | -44.19307 | 2025-07-09 04:25:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58407c79-4ef7-35ef-a56d-40fd92ec87ba | -20.41784 | -43.55472 | 2025-07-09 04:25:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 71f72aaf-51df-32b2-abe6-0ab1c5b4e1b6 | -19.75148 | -53.99908 | 2025-07-09 04:25:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 967a0b65-de58-3bb9-beea-d2e111b90ea7 | -22.62626 | -47.91604 | 2025-07-09 04:25:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ad13a42-78a0-38cf-9a46-125679a955c1 | -20.39338 | -48.60595 | 2025-07-09 04:25:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 163dfec8-2b44-38d4-a9ea-c53dc320093e | -22.54032 | -48.81312 | 2025-07-09 04:25:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fdaf48f-fd2f-34d7-8b13-36118fc3d991 | -18.08845 | -54.28463 | 2025-07-09 04:25:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7275086d-9707-3753-9768-6f602f3c0448 | -21.79164 | -52.76171 | 2025-07-09 04:25:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3047bae-2fd6-3f14-bacc-f64f3dc92691 | -19.64725 | -49.51234 | 2025-07-09 04:25:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2ad92a0e-6cad-336b-95f4-e904ac73388b | -20.40493 | -48.6195 | 2025-07-09 04:25:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b068e67-cda0-3cf1-ad3b-d3659af29b3d | -21.42879 | -48.64821 | 2025-07-09 04:25:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbefa2d6-66a4-312a-ab7e-d70ed3bc4031 | -20.76396 | -46.77105 | 2025-07-09 04:25:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 10c900d9-2b33-3854-a43b-8b86bca792f7 | -18.65135 | -55.73211 | 2025-07-09 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ace91e56-82d5-3ed2-a6dc-bac256267870 | -20.99445 | -51.79399 | 2025-07-09 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 86d97dd1-987c-3336-8ba9-8a2970b6f2ab | -18.41386 | -51.97908 | 2025-07-09 04:25:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 128b835f-08b6-3a15-ab18-7ff3d01fbbb4 | -20.21764 | -44.47763 | 2025-07-09 04:25:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ea531e95-07d8-34e1-ba2e-19ec6cee7e67 | -23.76257 | -46.9135 | 2025-07-09 04:25:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bd192746-1545-3d38-95d8-0c11df94c044 | -18.41336 | -51.97721 | 2025-07-09 04:25:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 639c370d-f24b-3879-85bc-e7d753ad951c | -21.18908 | -48.9394 | 2025-07-09 04:25:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 97e380da-ddd6-30ad-829a-8e9f0d57342f | -22.61901 | -47.91862 | 2025-07-09 04:25:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 975fa2b4-200d-305c-90b4-9cb1e9d85fc4 | -19.37149 | -51.40634 | 2025-07-09 04:25:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea70dbb7-95d8-37ae-9396-69547fd40345 | -20.72771 | -56.65607 | 2025-07-09 04:25:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 86dbf0ff-ab22-36a8-b019-5686da950ae1 | -18.64653 | -55.731 | 2025-07-09 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 2c492252-49f7-3cf0-bf74-0af663502762 | -18.6417 | -55.7299 | 2025-07-09 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 5c10552d-274f-3aa1-802c-5017a02f51e7 | -18.08624 | -54.28527 | 2025-07-09 04:25:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09d20917-50e0-3fc6-8986-b5ee1f0e59d3 | -21.31681 | -56.1272 | 2025-07-09 04:25:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f27a062-42cf-3bed-96b5-a1b8c9dee543 | -23.33772 | -46.7714 | 2025-07-09 04:25:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9e6ef459-98c4-3ebd-b330-e8bf6e581723 | -19.08344 | -56.05229 | 2025-07-09 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a6db996a-fe88-38eb-92c0-066fda5fc29a | -18.64811 | -47.92238 | 2025-07-09 04:25:00 | NPP-375D | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba12cfb2-bf9a-343a-90b1-a3bae1cbaa2e | -21.04616 | -45.27576 | 2025-07-09 04:25:00 | NPP-375D | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ee47a555-27ba-37fe-91b4-565960c1c089 | -21.43928 | -54.57371 | 2025-07-09 04:25:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6146df1f-9fb1-3324-9285-2a25437f3bf2 | -18.08755 | -54.28917 | 2025-07-09 04:25:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73d50cca-7cbb-3d3f-ac88-ac378b7ac40c | -20.40279 | -48.61147 | 2025-07-09 04:25:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 065c58f9-898a-3191-9439-247bc4bf6dd2 | -21.18847 | -48.94314 | 2025-07-09 04:25:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1a0b5e2f-aeac-303e-adf3-79b0f584bc76 | -20.40552 | -48.61578 | 2025-07-09 04:25:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dd38971-3b7b-3466-ae0a-54370f73510f | -21.43843 | -54.57799 | 2025-07-09 04:25:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53135611-1d93-3aa1-8368-7039d7e7b520 | -23.67185 | -46.89028 | 2025-07-09 04:25:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a34f5751-9e4a-32eb-8af9-9763f907a8a0 | -19.75068 | -54.00322 | 2025-07-09 04:25:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67fe9d45-ac3b-3321-9c3a-1fe489926411 | -20.39671 | -48.60655 | 2025-07-09 04:25:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 019c0d86-f119-34b0-80cd-637922cce84c | -19.36861 | -51.40107 | 2025-07-09 04:25:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73af3ce3-f77b-3ac3-a7ed-76f4be141fa0 | -21.85865 | -46.62563 | 2025-07-09 04:25:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c46a88ea-58f2-3c2d-8165-f9da7d752b00 | -18.40907 | -44.18983 | 2025-07-09 04:25:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 624b503c-9345-3319-b131-9bb8b4acef67 | -22.85756 | -45.21805 | 2025-07-09 04:25:00 | NPP-375D | APARECIDA | SÃO PAULO | Brasil | 3502507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3edfd181-063a-3b57-8c5a-bdcf6f066a10 | -18.65248 | -55.72652 | 2025-07-09 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 277bc971-9c64-3fba-8504-6648b04ca4ac | -22.52262 | -48.53674 | 2025-07-09 04:25:00 | NPP-375D | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37d19cd9-7e80-344b-8b62-35de435e097d | -18.64395 | -55.71872 | 2025-07-09 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a492251e-33a2-3feb-b880-cdd1db9c1003 | -18.64765 | -55.72541 | 2025-07-09 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c6d668da-0fdf-3f41-9282-27d53652ee9e | -27.09061 | -50.51228 | 2025-07-09 04:27:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e43d8a04-4bb0-3f9e-a165-499e4fce980c | -27.68782 | -48.75165 | 2025-07-09 04:27:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7bc772da-e435-3ebb-b85c-63602532eb5f | -8.5217 | -43.2593 | 2025-07-09 04:30:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| fe28adf7-2d83-3c76-9d1b-80babb91a13a | -8.5214 | -43.2828 | 2025-07-09 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 180.1 |
| 5dd0932d-82f3-38a9-b25e-2642eb978ff6 | -8.5028 | -43.2614 | 2025-07-09 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 62ea88fe-3e5c-3192-8a7c-0043ee619c95 | -8.5025 | -43.285 | 2025-07-09 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 174.2 |


[Clique aqui para ver as próximas entradas](README19.md)
