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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b490b56-5ac9-3fab-8975-463347618d42 | -8.98101 | -49.18039 | 2025-07-08 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 786d1060-fb2f-3e4e-8edf-1620c0fe3954 | -9.00696 | -48.72374 | 2025-07-08 04:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08491458-72a2-3eca-9944-7ee55e88bd2a | -11.45171 | -45.10537 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00ca7473-c0ec-34ed-bea3-e890cc3be0c8 | -10.97708 | -45.11247 | 2025-07-08 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 63f6e80c-8aa6-3984-b7ab-0917aa21c234 | -9.74661 | -53.29367 | 2025-07-08 04:42:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4db21630-e5a5-3f05-af63-5d8d7c6be98a | -9.22569 | -48.59401 | 2025-07-08 04:42:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 69aeb243-382f-3a67-a7ce-a1eb785eb924 | -9.1791 | -50.18129 | 2025-07-08 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d099c9eb-7879-3958-93fb-8a8dc002e9ec | -11.30177 | -46.76785 | 2025-07-08 04:42:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28ccf703-345f-3657-8322-f6ecb2fd10c0 | -13.41732 | -47.87996 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b4db3b5-c523-31bb-a2e0-52008cc69626 | -10.64784 | -49.46282 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0ef4c884-da09-3e12-a7a9-987db006c770 | -11.20072 | -48.99614 | 2025-07-08 04:42:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 816ccc17-eb8e-3ac4-ad43-61b55e1fd010 | -11.00397 | -42.78336 | 2025-07-08 04:42:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5ab58e23-fe1b-3d75-ae14-16b107c82ee4 | -10.96178 | -48.20419 | 2025-07-08 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01782b68-9f49-349d-b2fc-798460c0b02d | -10.36275 | -48.72939 | 2025-07-08 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee6e4290-0652-332c-9579-db72d510624f | -14.18924 | -45.51093 | 2025-07-08 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50d264fa-0a2f-386f-a246-70f7ff332ce8 | -12.33263 | -49.32349 | 2025-07-08 04:42:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a01dfb6-f9a7-3088-a925-16eac5182b31 | -10.63499 | -49.45713 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01d99fee-a3e9-30fb-be9c-bb64edab2dc0 | -9.21497 | -48.59605 | 2025-07-08 04:42:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 98119df3-1cea-3e3a-a63a-7c26ca06a4e3 | -10.2809 | -49.55807 | 2025-07-08 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6724a9d-519d-3512-8e0a-ea060c7a9992 | -11.34891 | -55.40628 | 2025-07-08 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6c73824-5cea-334d-833b-be1085cec4fe | -11.4245 | -45.10634 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 78401d6c-b663-3a6d-b627-f4a340da4a4b | -11.20015 | -48.99982 | 2025-07-08 04:42:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bcc22d6-89ef-3516-933f-636c98f639be | -11.29406 | -45.27163 | 2025-07-08 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 440654c1-2ee5-3f0f-a477-9caab70d4124 | -9.87274 | -48.46586 | 2025-07-08 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd9c1593-03b7-3c1a-8222-26cd4c03eeba | -9.23247 | -48.59507 | 2025-07-08 04:42:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f58b8142-deca-38d1-8456-333f8ba60145 | -10.65063 | -49.46692 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2e092a4-f30e-3788-9062-e27635cc6035 | -10.71563 | -48.4035 | 2025-07-08 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8cfbb1a-fbff-3898-8ae5-d058d28f0395 | -10.671 | -56.54674 | 2025-07-08 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fae1bf12-7c64-3261-929d-b2b47c172aa6 | -10.82701 | -54.02009 | 2025-07-08 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c87ab625-ddfb-3b42-b242-92c409ac8466 | -13.40585 | -47.88253 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1e1ce80f-7427-343f-9ed4-5fae902af1dc | -12.98911 | -44.87829 | 2025-07-08 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30ab84c0-94b0-3d69-be73-723c08a3d806 | -14.60231 | -46.59663 | 2025-07-08 04:42:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f670d7e5-a861-327d-9993-e812c8bb67e5 | -10.63889 | -49.4541 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7420b21c-afeb-3900-b6d9-a55446990f22 | -13.4137 | -47.87942 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21e54a16-5f4d-3901-a4c5-68fb06cdc846 | -8.70406 | -50.01585 | 2025-07-08 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6191a8bb-060d-3166-bb0b-03099320f416 | -10.63834 | -49.45767 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc30e3fd-0997-3b8d-a893-2f3b4a408064 | -9.17965 | -50.1778 | 2025-07-08 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a85fc95b-1a41-3d9b-ac90-352083201d9a | -13.3668 | -47.79439 | 2025-07-08 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9210106-4ae6-30be-915b-a093c725d1f5 | -22.67614 | -42.8544 | 2025-07-08 04:44:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 447ad283-247c-389f-8435-00f93069abdd | -14.27181 | -53.23247 | 2025-07-08 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ea6224a-5753-3c40-a1bb-3b63e4853b03 | -17.78079 | -42.80865 | 2025-07-08 04:44:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a664dfa1-5c1f-351a-80f7-f901e77df978 | -16.04618 | -43.80443 | 2025-07-08 04:44:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01eeef9b-a0fe-3033-ba89-b0186b3bdb8d | -21.49496 | -47.26965 | 2025-07-08 04:44:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbcf7f81-54f5-3276-a7ae-5267a62cb573 | -21.21951 | -55.9465 | 2025-07-08 04:44:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f96cf8e-384d-3c36-8c74-6b0601a45123 | -19.75094 | -54.00032 | 2025-07-08 04:44:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e75d6d27-ca27-3585-8b63-7b480b1d63d0 | -15.69337 | -53.32942 | 2025-07-08 04:44:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 513c67ca-e542-3244-8090-140944ac09ec | -18.28886 | -54.28823 | 2025-07-08 04:44:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75d4ff1a-2fbc-3183-9971-94d3f885ddba | -19.59657 | -47.61468 | 2025-07-08 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 605b13ba-c050-38fe-b374-b03284aab50e | -17.77366 | -52.44374 | 2025-07-08 04:44:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6ac5315-90be-3d61-a6ec-0b3252b8aa97 | -18.65421 | -55.7406 | 2025-07-08 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 10f5989d-8a31-322a-987b-dcf895380073 | -14.26837 | -53.23188 | 2025-07-08 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0784259d-99b7-3ce2-b305-853c9e31288d | -21.04292 | -55.99842 | 2025-07-08 04:44:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46f25e23-ac77-3775-97b5-60e3098f9e1c | -15.61937 | -46.46393 | 2025-07-08 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac28e550-f4b0-3442-ac5e-f3402f79862b | -19.77759 | -47.9231 | 2025-07-08 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b05edbbd-8ff7-36dc-b7d1-f0ac8bbc2c9f | -19.00342 | -48.05686 | 2025-07-08 04:44:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92299c0a-2e50-3939-8f6d-8782a32b8041 | -19.59832 | -47.61616 | 2025-07-08 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f54b25b8-8724-31d0-819a-1961286c8f1f | -20.99501 | -51.79404 | 2025-07-08 04:44:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 89d973f6-fb10-3dfe-a49e-a9ab9a8f7c98 | -14.84784 | -48.2445 | 2025-07-08 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b49b6ed-73f7-3360-8487-283fd8710e1a | -20.77675 | -49.86718 | 2025-07-08 04:44:00 | NPP-375D | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c6bef7f-42a7-364b-9b0c-1f6282596f8a | -21.30544 | -49.45434 | 2025-07-08 04:44:00 | NPP-375D | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 51d79979-6faa-336c-8db0-a34bc262aaeb | -19.08901 | -56.05285 | 2025-07-08 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9e334bce-724b-35dc-b251-1252b1f189e1 | -15.02463 | -49.24715 | 2025-07-08 04:44:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5700141b-e0e5-3fc4-a90b-6f3c9505408f | -18.63835 | -55.72374 | 2025-07-08 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 15a70e6a-a2a7-3ab4-97cf-4b84b1be60e8 | -19.59436 | -47.61556 | 2025-07-08 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 896689a6-0c19-3cbe-b9d9-caff91319dff | -21.03935 | -55.99772 | 2025-07-08 04:44:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96ccbd33-4471-3aea-bf2d-b5bd678535b5 | -19.69644 | -52.39087 | 2025-07-08 04:44:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eeb561fd-4ada-3244-9a6e-35996cadd313 | -19.59368 | -47.62097 | 2025-07-08 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1797ea28-44d4-3b76-93c9-ebeabddbc017 | -21.79227 | -52.76285 | 2025-07-08 04:44:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 240c1912-c857-3ec8-9886-bbf483b30ef2 | -18.23005 | -44.20076 | 2025-07-08 04:44:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f77deeee-3ff7-3a82-952b-6115fa51a408 | -19.75157 | -53.99654 | 2025-07-08 04:44:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98a33f90-ea0c-3299-90b6-05503e97b074 | -18.51901 | -47.15807 | 2025-07-08 04:44:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d6e4ab9-1868-37b9-911d-8aee102e207a | -21.30482 | -49.45887 | 2025-07-08 04:44:00 | NPP-375D | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 662729b6-d40d-3e44-b1d3-3fe3a0d71977 | -22.67925 | -42.85271 | 2025-07-08 04:44:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 14c91b67-a694-3867-8082-3acd4594cbb2 | -18.6508 | -55.71701 | 2025-07-08 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8ee9105c-d88d-3a83-9d7e-dcd23485748b | -20.77796 | -49.85867 | 2025-07-08 04:44:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| df373a42-4a21-30a5-b14b-1f031958a34c | -18.65498 | -55.73616 | 2025-07-08 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 13931123-95fb-3355-a884-b579d2eac74f | -21.30056 | -48.56324 | 2025-07-08 04:44:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fc1791d-7646-340c-873f-d745d394e1fe | -21.49448 | -47.27357 | 2025-07-08 04:44:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e50ff87-dec6-3a35-9da6-cdf9bc0fca17 | -22.67363 | -42.85217 | 2025-07-08 04:44:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 67eb72f5-3347-35f5-b100-105726dac510 | -21.7956 | -52.76345 | 2025-07-08 04:44:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b266fc5-9ca7-380b-afee-3dd97d19ce50 | -15.24846 | -51.53429 | 2025-07-08 04:44:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e058ca4-e4b8-373e-ac48-cb8549691893 | -15.08015 | -48.94489 | 2025-07-08 04:44:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7621201-7eaa-3644-851e-9522f97360fd | -20.76515 | -46.76975 | 2025-07-08 04:44:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ffa9ccd0-0f98-36a6-b048-b51163056ffe | -16.68052 | -43.88408 | 2025-07-08 04:44:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a00ea450-2710-3dc1-9e48-805f0bf2ce25 | -20.57794 | -47.49474 | 2025-07-08 04:44:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19abb7a2-4d23-344c-9675-717db3f68384 | -19.20827 | -55.76 | 2025-07-08 04:44:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8b38809d-e809-3ec1-a1de-ebcc38dce1be | -20.76401 | -46.76846 | 2025-07-08 04:44:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8960637b-cb28-3a9f-bf3c-d8ad2294c244 | -20.41741 | -43.55448 | 2025-07-08 04:44:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 34b30ffa-930b-3bdb-ba27-5e0b526dd3a0 | -19.59585 | -47.62008 | 2025-07-08 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8da678c-58e7-3535-b477-2904f9799b64 | -18.22518 | -44.20023 | 2025-07-08 04:44:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d6f9dbe2-a795-3fea-a5e1-4b5b504c3d3e | -16.4692 | -54.54527 | 2025-07-08 04:44:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fd3e30c-d5b1-34ee-a059-193976c8f0cf | -20.77736 | -49.86294 | 2025-07-08 04:44:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3370dcee-6966-304d-8549-1e114b7f09b9 | -15.25834 | -51.53204 | 2025-07-08 04:44:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b942de08-f107-3eb1-a737-821e6bba4c42 | -21.19631 | -44.93683 | 2025-07-08 04:44:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 92b03d90-bfe8-3893-9134-51e4ecd76ba7 | -19.64862 | -49.51598 | 2025-07-08 04:44:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 350972b2-4998-3aa5-9d6d-e1adce46b334 | -21.04216 | -56.00272 | 2025-07-08 04:44:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15b32172-a7f4-3543-860a-f83af7851e15 | -19.59189 | -47.61948 | 2025-07-08 04:44:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8902c0f-de1e-38c8-97f4-c4c67f660e0e | -18.40174 | -55.59902 | 2025-07-08 04:44:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3036d76b-90dd-355c-84ef-eb332fb1c254 | -16.05103 | -43.80509 | 2025-07-08 04:44:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e5b4ea4-c454-3638-8ba9-389e8cc726b7 | -18.4476 | -50.1398 | 2025-07-08 04:44:00 | NPP-375D | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README16.md)
