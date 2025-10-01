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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6660baf-c363-3f5c-9163-d93e28b899e5 | -14.3489 | -45.9237 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 669ee5d3-6045-3579-b7ed-0fb62be82000 | -11.06908 | -47.84296 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dc146e0b-ded6-312a-bbd2-dbde4eaa042f | -11.84348 | -48.04971 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 63464f7a-263b-35e4-8ee7-961d30235e66 | -13.66937 | -48.06794 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d7dfa48-3009-35f6-806b-26415ab7e6db | -14.79557 | -45.80508 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 71e9f1db-aca9-3b65-bf1a-50f13309944a | -14.50673 | -48.48527 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 747fbe7b-90f0-3702-8f21-378a89ffd2a8 | -13.07677 | -47.07012 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3608a0b4-b536-348e-985f-c1f7de4c105d | -10.21884 | -43.03971 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| da6c8ceb-35ff-3595-bba0-0b4da39cdf17 | -13.8492 | -47.93887 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57babb32-25e3-3822-8f3e-53a094f9ab3c | -13.94125 | -48.10925 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb4fb299-26d8-3f92-a910-b07fa02bafbf | -13.37792 | -48.10224 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf2d8ab6-94d8-3a22-9d00-e97cc2a493a1 | -14.89939 | -48.11145 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a9a4c483-d606-3e30-8ff5-1d4473429ef0 | -13.5396 | -47.27023 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb888fe7-f0d4-3d93-8af6-5161c367c823 | -14.90202 | -48.12228 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b419df11-7fef-3050-b055-50158bd766c0 | -15.40209 | -47.05485 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 366ade11-d3cd-337c-82db-6bc2f5c70b3c | -14.9018 | -47.20883 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 153f2927-4759-3a60-8a08-69fbc5380e5f | -15.2614 | -49.28236 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ad800487-0188-329e-87d8-49b5e3b405d0 | -13.28411 | -47.23079 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ece5dfe8-52f1-32f2-acda-1e138c9a203f | -11.37801 | -45.05141 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b07e5e80-7b6c-336d-84db-65981da9d9c6 | -13.37216 | -48.11338 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac0e9e85-bfc7-357c-9482-f8746ea91b15 | -12.87995 | -46.91193 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0a6015d6-6439-3305-ac5e-132adca49f0f | -14.20524 | -46.10281 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aab8573b-6c42-3e51-8d8e-019e8755439f | -14.76455 | -45.74969 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38a7df1a-73dc-3869-ac1a-72c41ec35f2e | -14.38861 | -46.22186 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39f90bc5-38d0-3507-bd06-4bd3f254bbb5 | -14.98732 | -50.76128 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f06d84f5-d4cc-38f5-8980-81b975654a9a | -15.34004 | -47.93062 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f41c01d6-dafd-3a88-93cf-c59d74b0575a | -14.18295 | -46.12555 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c12ff59-f6be-37f6-90bc-8142e0c94cd0 | -13.73237 | -48.81715 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e19e6aa2-4a0f-3d5f-862e-ea4e6d5f0091 | -13.36606 | -48.15825 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d0d08fa-84e4-382d-bd6b-cb67b539769f | -13.70538 | -48.62914 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44edfdf5-b339-373e-b28b-e47b21be9286 | -15.94629 | -48.1159 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84c0da4a-1b99-3e26-b669-eba1353e9855 | -12.24053 | -47.80468 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f0d53db8-461f-3644-a191-375d4c9a3edb | -10.90481 | -47.62426 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8706ef19-5df1-3f42-a595-84610d07daea | -9.39896 | -54.7124 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70219e9d-c7a7-394e-ad7d-200ced291456 | -15.48096 | -48.54679 | 2025-10-01 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5eed6ab5-5305-368b-becb-372c6e696b41 | -11.15538 | -54.1261 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1914e0fc-901b-3736-acfe-af2e962d23d3 | -9.56332 | -50.77773 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2563f67c-ce03-34ad-94e1-eb1f959abdd9 | -11.80069 | -46.61554 | 2025-10-01 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54e73cf7-9417-3f88-9d84-8dfe73aecc63 | -14.18407 | -46.11715 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4de0a85-02af-314c-86f3-b5600f0982cf | -14.05941 | -44.37418 | 2025-10-01 04:51:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 485df25b-490d-3876-8d1f-0f8a4c52c816 | -12.1743 | -51.41629 | 2025-10-01 04:51:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87eaf5da-b811-3b8e-892e-454d47bb5946 | -11.52005 | -43.54924 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7806404a-c16f-38a7-ad14-ab2b0cef0ccf | -11.81981 | -44.97783 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbd025ee-d1cf-3ff2-a3dd-4772055bca6d | -11.99838 | -46.57965 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f63706bc-9f63-3da3-b125-d62a8807e038 | -14.72072 | -48.1454 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1090873a-e92a-33d9-a908-2c45c8d21194 | -14.19317 | -46.11776 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8f4cb756-5a27-3e63-a80e-f20390b74f61 | -10.70726 | -47.99124 | 2025-10-01 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa37c9ca-3164-35e0-b25e-481b0e21334f | -15.24411 | -48.73959 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a3a6356-fe44-3c27-95bd-f9f3650611fa | -11.06588 | -47.83771 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3fd14df-4bd2-3f4e-8d44-8f7d769ae305 | -15.27092 | -51.47623 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c705c6f7-0e22-3b4d-a73d-bbc2b43c42d1 | -14.65472 | -48.13734 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bf55b2e-78cd-3a6a-afca-5d3ab03dfc25 | -14.35128 | -45.90487 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ba1cbd6-096d-3e93-bf3d-fa07a537bf74 | -9.47301 | -45.48391 | 2025-10-01 04:51:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c60c159e-38b4-316d-aeed-c22a95ba2cbd | -14.60676 | -48.2207 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b28d149-f28e-3f71-aa57-cf9583bbe1b7 | -13.7655 | -48.40005 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed7dcb7b-9133-36bf-a566-abd4eac9671a | -14.9879 | -50.75733 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01af2104-b93f-3165-a3be-bf0e9b3206f3 | -14.85306 | -48.33704 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76427df2-acec-3838-ad45-f32f851645bc | -12.24774 | -47.81055 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 90c1d254-0686-31a1-9dd1-8397d0bf661a | -9.40612 | -54.71365 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34d8c661-6b5b-3e69-b797-205e31cb772f | -13.76278 | -47.96257 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 11ce1fe2-9e55-3f44-b878-bf9dc194952a | -12.46273 | -50.24974 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcd5ca71-67bc-3efc-a646-3333e6bb7e24 | -10.78886 | -45.35783 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5b1d342-087d-3730-8bd0-61a45df16716 | -12.23007 | -53.87661 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d171f47d-65e5-3d66-bd93-16a6675c7cb3 | -14.68691 | -45.27704 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| adc2e326-c081-3ff6-a860-38a98f0cb368 | -11.85347 | -45.01313 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c54c7582-f6d8-3664-8629-fac7d718a696 | -14.79747 | -45.78984 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db95dbc0-7bab-39b7-9298-e2e8da4320d7 | -10.75297 | -45.37378 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 053baef2-558b-31cf-b5bf-58b3928f611c | -9.55996 | -50.7772 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 415ab915-9643-372e-9e0b-9bc030970177 | -15.01115 | -46.97153 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11b81c73-6144-38c2-8c65-11ad0347f75c | -9.41243 | -54.69778 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d23a688-e418-30ae-8e61-dda0bd0676e8 | -14.98441 | -50.75677 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8778db14-e086-3e37-9d6b-3c22c06c809a | -13.28776 | -47.23503 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6716846e-1286-3619-9776-c9b1e25bfc0c | -12.82364 | -47.01167 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60d9fa55-7580-35b8-92f1-2eb540af0260 | -16.05344 | -51.01573 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19819740-cf01-34a1-9505-41decbff6709 | -11.99315 | -46.65044 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a92a5b0-4ef4-3205-8e7b-dc0425c31fec | -11.38202 | -45.05696 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83acd1e3-5448-315a-b3ea-fbb10926c9da | -14.09796 | -49.74519 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4da04560-e79a-36f4-8b1a-9409bb740234 | -14.03255 | -47.99029 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a73a8cf1-6c0b-3bbd-99aa-38fde2e0c6ae | -12.71429 | -46.90346 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5df6287-70b6-3c1e-bdd8-b7054229cf38 | -14.96607 | -46.87875 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80007636-d6bf-305f-b9d8-1e0939db7e85 | -11.08518 | -47.84062 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2c4001f7-f17c-3e2f-b515-24ec2c84b2da | -13.30067 | -50.65793 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb07158f-9a22-3640-9868-3d5b2e11fccb | -11.83658 | -44.95997 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2d29f99b-792a-3733-964f-ddeefc028291 | -14.8716 | -49.71411 | 2025-10-01 04:51:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b6f5146-b730-35c0-b037-8abb23656654 | -12.78975 | -46.88339 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac5206bc-3043-38fb-aa95-9d7463e00adb | -15.17335 | -49.08765 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15be2e9e-8ca4-380e-b24a-0b53a1e32e59 | -12.85125 | -47.02718 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9a12d9d-38dd-31e7-bdcc-7ef8331b04d3 | -11.63895 | -47.49203 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe29c872-1314-358c-b5a0-14f4147d25ee | -11.45565 | -45.02337 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8242e691-f8ae-3d45-87e8-67c9c36281e8 | -9.92874 | -43.67975 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd901633-29b2-36c8-9656-eb6f69d4750b | -8.95978 | -50.32719 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00adb24f-22d5-3b68-a277-ec1cbd68635c | -13.28961 | -47.23605 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f12c2357-52fe-32d7-9cbe-8a3eabe07d4f | -9.77931 | -54.37565 | 2025-10-01 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 606e9734-b481-3e40-acf7-adf995a71a7f | -14.69572 | -48.12026 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20d0bb36-81c8-3c89-86fc-8040d3e61678 | -11.42526 | -43.49854 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01ae07d1-d5c0-3226-aab6-1d6f7b0c0fc6 | -9.31797 | -45.72397 | 2025-10-01 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37f3b126-1c59-3b6b-8988-07a187ab857a | -15.33122 | -46.2739 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76a5e5de-a6ca-399f-820b-0c5c9d0d6a60 | -13.7648 | -48.40496 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ecc9e09b-736f-3f02-93ad-e57aafb922b0 | -10.91915 | -44.33812 | 2025-10-01 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4425634b-9743-3bd2-b0bd-8a7ce4a395b4 | -10.08355 | -45.62297 | 2025-10-01 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README101.md)
