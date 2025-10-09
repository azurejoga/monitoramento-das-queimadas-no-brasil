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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 246447f2-55f2-3af8-afdd-ed43f5091f6e | -15.2813 | -47.87714 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fb28f38-7770-3d65-8660-4c7ccb9d1463 | -12.04892 | -43.50232 | 2025-10-09 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76b1e696-0912-3ce3-801b-3f0523d08f43 | -14.91315 | -46.80642 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9263a1ca-4e00-356e-83c1-25d8d34e3be5 | -13.79298 | -45.84213 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f467652-c64e-3285-bbe7-b68603427189 | -15.2024 | -44.4932 | 2025-10-09 04:00:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23a4bbc3-7f1c-3025-b80c-14e49f7b79ed | -16.39953 | -46.3574 | 2025-10-09 04:00:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9b1cafd-fa1c-319a-90f7-dfc67afc8de9 | -14.94486 | -46.78146 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ba4d348-bb2e-3d29-8cf7-9d62790a4c1e | -10.85617 | -49.94189 | 2025-10-09 04:00:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2e5e5b6-fcd9-3129-a9cf-158ddf3d219d | -13.79229 | -45.87032 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5587270e-e30b-393f-89cd-9be8e56dbe25 | -14.41509 | -43.98919 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa0f6538-a9ed-3758-a57b-903fcf71178e | -11.52058 | -43.312 | 2025-10-09 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e2e5511-d1c4-36e0-af21-1d61359df359 | -15.71931 | -43.94864 | 2025-10-09 04:00:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d3a12f3-51ca-3ee8-a6c8-9c04c209e8db | -15.48544 | -46.8597 | 2025-10-09 04:00:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e7abba1-aa77-3c59-bd4e-4973fc7268df | -13.80545 | -43.93472 | 2025-10-09 04:00:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db9c6c60-27cb-399d-9a17-0d758fac129f | -14.41588 | -43.98465 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d260be9c-49a5-3a9e-bab3-c8b5fa7673c5 | -14.25666 | -45.86649 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3ae8438-cdce-32cf-8de3-879e09494a11 | -13.82883 | -45.81268 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c4ade802-4ed0-3296-bc1d-aec9cbb953b4 | -13.79159 | -45.84991 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f8fbf10-97cd-394b-9150-97e3beafb887 | -13.78672 | -45.8529 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 172bdaa3-3735-3926-b240-4559178398b7 | -11.23601 | -40.34568 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a3036ebd-17c7-3d08-8a3d-4754fa449005 | -10.53032 | -50.02755 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c83b4fd7-4de3-3055-9eef-5cce32ea455d | -15.22575 | -46.37145 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c09b8f5b-c48d-3a43-813a-c54a436b4137 | -15.79932 | -43.78712 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6ee16f52-a6ad-36a8-932d-89e1ec8edda3 | -12.1451 | -47.75093 | 2025-10-09 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d35d39f7-75e9-38b4-9f47-ee0afada85f8 | -14.8523 | -48.43743 | 2025-10-09 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9059b10-5904-3598-9ee5-cef71fab1185 | -10.51866 | -50.02516 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c70e06b4-d4ac-3fce-91fb-2466a831019d | -15.39482 | -48.05341 | 2025-10-09 04:00:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a256e44-4cfa-32f0-a4f8-38535f601690 | -13.12546 | -43.90322 | 2025-10-09 04:00:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a7408b0-6a8d-3dc1-b188-5a9764d191e1 | -13.79785 | -45.83909 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22bdcfe8-9a94-3e7a-ba07-fc7bf83edbde | -11.76651 | -45.14156 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4a83fe0-ce13-3f94-a5d5-fd10216dd825 | -13.7916 | -45.87422 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8cf10836-0530-34aa-a8c4-509536364660 | -11.86854 | -45.51292 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f8e849f-105b-35a9-a23e-4a7b355e8cef | -10.87564 | -50.95394 | 2025-10-09 04:00:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d76df019-01ad-39aa-b260-3b7695979149 | -17.89774 | -44.26117 | 2025-10-09 04:02:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd7a3829-8890-358a-a5fd-651ddc1a495a | -18.03892 | -44.99029 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a724b70-272a-31e2-83f3-9b1b6221f0b7 | -16.28685 | -47.13828 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d48999d-dc4d-3916-8112-a879d31b803e | -18.08919 | -44.44842 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09a164a0-2fcc-3d48-a30b-ca31e04ba65e | -17.21034 | -47.65403 | 2025-10-09 04:02:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 18eefbdb-f182-3712-a0ac-133d74218800 | -16.70166 | -47.59902 | 2025-10-09 04:02:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5af4f57-808b-32db-979f-3e19a3507d3f | -17.52771 | -46.75401 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 161fa4ef-00bd-3bf1-8fc4-6e2855c63239 | -16.26144 | -48.63532 | 2025-10-09 04:02:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b112eb2e-3898-3c7f-afb9-57bf8e35b966 | -16.72834 | -47.61581 | 2025-10-09 04:02:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfa7cb66-916c-3243-ac5a-2261d3012f5f | -18.08672 | -44.46241 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1924b3c-d97e-3c25-8a1b-9f72e69111e0 | -18.03227 | -44.98428 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 37590ef1-5e93-30ca-a9ae-89b1cfea351e | -17.99444 | -45.62386 | 2025-10-09 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 4f244457-401a-37b3-b6ac-e9195fe404fa | -17.32917 | -46.84216 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0b75f18-da4b-3952-a274-7de9de74a1af | -17.60303 | -47.18248 | 2025-10-09 04:02:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bed18e29-65e3-3331-92fe-e26aa367e253 | -19.5062 | -44.08531 | 2025-10-09 04:02:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1944e7f8-28cc-36d6-b66c-a20afb888b24 | -18.03897 | -44.71006 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4460494-fcae-31c3-a0f4-fce0aecdf816 | -18.09476 | -44.45934 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e098116-e1b7-36af-8494-47c628b75d75 | -17.15223 | -45.79409 | 2025-10-09 04:02:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20ff31a7-2f9f-3366-a8a7-a884129ec450 | -18.0331 | -44.97962 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f84be7a9-2e37-3c37-afb2-eea558c09c06 | -17.65451 | -44.43055 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07326faa-f8ed-3692-8c31-df9f6d4836a2 | -18.5449 | -45.06822 | 2025-10-09 04:02:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8ce17f7-8008-3863-9b49-e08ee229d49f | -18.39528 | -46.87848 | 2025-10-09 04:02:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35704049-876c-3ff2-ab99-49420a29e2df | -17.37857 | -46.88128 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3e373ad-3c8a-3fb3-8050-6f9cb5da56fa | -17.37591 | -45.08135 | 2025-10-09 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72afde47-63a5-3d6f-bf91-f30ee22dca1a | -17.96309 | -45.00414 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc77aef2-5afb-3092-9c93-c80f45e5192a | -17.99059 | -45.62304 | 2025-10-09 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 3699f87a-f621-3602-a873-b4b214b34eeb | -18.41693 | -45.24056 | 2025-10-09 04:02:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c752431d-565f-3bc8-8e16-29184c78a733 | -18.06479 | -44.41825 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76484865-a7ec-31c0-a96b-b0a34e2d2235 | -16.28603 | -47.14258 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec998fd7-f16f-3c8d-866a-751d3f329457 | -19.50139 | -43.84019 | 2025-10-09 04:02:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1cf1027-c46c-3fa4-8cdd-67c4cae3293a | -18.25136 | -46.99452 | 2025-10-09 04:02:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbced84f-4d77-30a1-96de-fa829350124d | -16.27288 | -47.14027 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 853e9cd6-c0b7-3cb8-9875-1522448c65b0 | -18.28902 | -45.43655 | 2025-10-09 04:02:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e70c9f82-ccc8-3352-b1ee-47e5562971ac | -19.7438 | -42.20435 | 2025-10-09 04:02:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c82338ce-097f-3f1c-af81-15366bb16979 | -18.24733 | -46.9922 | 2025-10-09 04:02:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26bc041a-f077-3712-99ef-0af752691cf0 | -17.37977 | -46.89829 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f8278a9-34d5-31d6-b27c-e7ce5d15cc22 | -19.50557 | -43.83677 | 2025-10-09 04:02:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0130990f-d1de-39f5-a8de-9820569a8871 | -16.70973 | -49.7559 | 2025-10-09 04:02:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0844ec51-8e8f-3932-a00a-3deb9c8b8006 | -18.09199 | -44.45383 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cb4f077-9e9f-351f-9270-179cbd79cd8a | -17.15874 | -43.43657 | 2025-10-09 04:02:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a9a62ba-89df-30eb-91d6-e5ede1750212 | -18.64903 | -43.91764 | 2025-10-09 04:02:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c76bd5e-d2fd-3faa-9b09-28c82b33839c | -18.03977 | -44.7056 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f46e2768-c9d2-3dff-8947-8312597b7f08 | -20.56276 | -54.66059 | 2025-10-09 04:02:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c17aa080-3f89-3de4-8963-97732c9a1e1f | -17.35874 | -45.06798 | 2025-10-09 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7230444-0f2d-3602-8fb4-c3ee11a5ec48 | -18.00105 | -48.32346 | 2025-10-09 04:02:00 | NPP-375D | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39403b9a-2e2c-3243-8316-dd33efd91ed3 | -18.03976 | -44.98555 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7a9075e-34cb-34b9-99b2-0631ab252e36 | -17.63051 | -47.20143 | 2025-10-09 04:02:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c4497203-ee7e-3ec3-b6de-d6897abc6637 | -17.92682 | -44.60383 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffbe8be0-1c70-3a91-89e6-ed4baa83af9b | -17.9847 | -44.96999 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c9b3b1c-f054-3968-ba2a-3bb1e8f33156 | -18.05507 | -44.96429 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dfa27b83-6e40-3bb3-a129-697b4218d406 | -18.41778 | -45.2358 | 2025-10-09 04:02:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 99628ebc-3417-39c5-a7bb-2a54d0520884 | -18.02891 | -45.00327 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9c80463-40ed-340f-86f0-a07de6266499 | -17.26903 | -46.90951 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 62e56a5d-88cd-3234-8ded-a5d7140ed9cd | -17.37214 | -45.08054 | 2025-10-09 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0094270-9069-38f4-a048-b88028201a63 | -17.53247 | -46.75505 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 51fa0e2c-717e-3809-9f8a-b274dba6dea4 | -18.64615 | -43.91328 | 2025-10-09 04:02:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 42ad603e-bba6-3132-bfa9-58b4058276e5 | -17.97439 | -44.96303 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f98ecf32-c6a5-3128-ba85-03ed1230f1a9 | -16.62255 | -46.76943 | 2025-10-09 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be273f8a-1da9-33bd-82ac-90a17e042ff8 | -17.98767 | -45.61715 | 2025-10-09 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1152dfa9-f47d-3ed0-ba0f-91bda42b5077 | -18.24721 | -46.99352 | 2025-10-09 04:02:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c58e439-d8ca-326f-91de-4948b2832e02 | -17.37677 | -45.07652 | 2025-10-09 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76ff63cf-bfe9-3ab7-8702-3e14184b6793 | -18.41115 | -45.22935 | 2025-10-09 04:02:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29c8fc27-97be-30ef-836e-c78c9287d3ee | -19.17843 | -43.52502 | 2025-10-09 04:02:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5f2d43b-3569-3916-bfd8-7452c8064d64 | -18.04763 | -44.96283 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e10501c-33f3-389d-83b0-510f8acd07b9 | -18.09033 | -44.46321 | 2025-10-09 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e11d08d8-1278-3e6a-9190-1f6bc81e327c | -17.25286 | -46.90223 | 2025-10-09 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecd9008e-5fdc-38e3-82cc-c4649dd7f9f4 | -17.95671 | -44.41544 | 2025-10-09 04:02:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README29.md)
