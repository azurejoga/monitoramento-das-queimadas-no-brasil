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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57f758cc-6bf2-3167-9619-ed3eb3f66767 | -15.99116 | -55.98005 | 2025-09-05 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4b0281fb-6120-3666-9c5e-60c03da58c1e | -12.91497 | -57.00624 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9457cfe8-ad84-32be-a5ba-fe866254aba0 | -13.51053 | -50.80758 | 2025-09-05 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f6c9248-e3e8-3d2a-a62e-8e691ed8ef93 | -12.99133 | -54.81931 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e82c2f21-17b4-3733-be85-bd561010a6f8 | -12.98788 | -54.8147 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4eb9b12d-9d0e-33da-93c2-f1e758ee3d91 | -15.62307 | -52.9014 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08681131-8ef1-3fcb-93c3-7eb31f7506ad | -15.05031 | -50.08354 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37ab7c7a-21b8-3308-9cdb-9499e8296c56 | -15.34314 | -43.0876 | 2025-09-05 04:38:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a221e66f-2b88-3542-be33-694227581627 | -17.66438 | -52.28362 | 2025-09-05 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 016a9a1e-8461-3822-925e-5a088f15873d | -20.24141 | -51.30827 | 2025-09-05 04:38:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 926082b1-9eca-3ef9-b1d0-ef7aaf2374ce | -16.4596 | -45.25788 | 2025-09-05 04:38:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 591e2df4-e502-3095-a1e3-977a7e5a10c6 | -20.52607 | -46.10908 | 2025-09-05 04:38:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d7bf0cf-3953-3298-9da7-afe1971496ca | -14.57931 | -48.02905 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7491f259-e9be-32ff-ba2b-a3a6b1ebf06c | -13.75447 | -49.10587 | 2025-09-05 04:38:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c48dee1-2a38-3f96-a57c-8ecb8b957fd1 | -14.03741 | -49.68881 | 2025-09-05 04:38:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab5d9b7f-6bec-36c6-b352-f86ea3741645 | -14.52328 | -48.07675 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 49bd0268-e58e-38e0-a32c-b12676fc3322 | -13.88491 | -47.98997 | 2025-09-05 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a1d679d-bc80-3513-af73-dcb56e3e8d82 | -15.05412 | -50.10257 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 840da36b-2235-3042-a9cb-9b9d48411bac | -15.61446 | -52.90861 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ead2f6f-970b-3e62-9367-00ab7f43f25d | -15.05469 | -50.09899 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e3b2875-0079-3637-becc-57c5bf2cbc12 | -14.58104 | -48.01765 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d83d5939-aede-35be-af4b-524cddc6a911 | -14.57989 | -48.02526 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2120b37-0aec-3032-98ca-efd546aaca7c | -15.31961 | -52.75055 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66431203-c1d7-390b-8382-857de2cd98fe | -14.52386 | -53.07859 | 2025-09-05 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b8a5617-691b-3513-9809-95b64ed800ff | -16.29757 | -45.69082 | 2025-09-05 04:38:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 461a4a3f-ca40-386e-ba39-49e14474dd1b | -15.54774 | -48.40055 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eec372df-c59b-3b13-99ba-cbb0b28e31d1 | -14.52021 | -53.07792 | 2025-09-05 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b1d5594-750a-304a-8683-dfd8a7a6a76b | -17.66096 | -52.28299 | 2025-09-05 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e98a530-d88a-3bdb-b463-dfc75447f54e | -15.00012 | -50.04245 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9cf59dd-f58f-3c0a-978c-dc0c4ebb99b6 | -16.3247 | -52.95578 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88d7f67a-a8d8-3f18-b95c-71d941d155e4 | -12.99614 | -54.81631 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 94dd56db-2c2e-3479-8f62-23290e798787 | -14.58046 | -48.02146 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27f13520-19fe-3454-a5a9-91387562f818 | -15.14226 | -52.34716 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e02d04c-8a2e-3732-8a0a-6f217af6258d | -20.45593 | -54.51572 | 2025-09-05 04:38:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd681311-1040-3a15-9f3e-1a0ed1e183ae | -16.319 | -52.94635 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 01ed333b-8520-3269-a4a3-bc4b09c711ca | -15.05927 | -50.07029 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb4556db-c158-3355-92ff-d025d5c174a6 | -15.21855 | -52.36702 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25acc932-22b5-39b1-adb4-ee84921155e7 | -20.24533 | -51.30518 | 2025-09-05 04:38:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 8f237ce3-3507-3739-b352-3a466adca0dd | -15.20005 | -52.36895 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c708b779-3bd1-3e42-8c12-758e5cfbf725 | -15.55512 | -48.42079 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07574600-7606-334f-9c00-a60e1d681818 | -15.17842 | -52.3901 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce3b0502-fe0a-36aa-bb25-b39124924538 | -16.60003 | -50.82608 | 2025-09-05 04:38:00 | NPP-375D | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37a8903a-3dcb-35f5-8dc0-8a9bf0aa92cd | -15.20575 | -52.37809 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 652199e9-be70-366e-875c-3fd90050ca54 | -15.05593 | -50.06974 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26ff5cc3-61ae-39ff-a63d-06dc7fad7219 | -12.35169 | -63.64223 | 2025-09-05 04:38:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a83002a3-1516-3e77-826f-79b3481d1188 | -14.59189 | -52.18393 | 2025-09-05 04:38:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e476b9ed-b247-38b4-9048-f76a835a2467 | -15.13254 | -52.34053 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2d11976-4e0d-34e9-a5bf-46597dec7a84 | -17.62016 | -46.70806 | 2025-09-05 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e68d1112-0cbe-3122-a653-ae89183bb7b5 | -12.35008 | -63.64972 | 2025-09-05 04:38:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a55b065-3442-3f6e-a70b-503142baf152 | -12.60663 | -56.99949 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1193c63e-007a-37fe-b379-985d51336f42 | -15.21923 | -52.36305 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7a76510-1b3c-3a6d-8435-4fa683df8ea0 | -12.35288 | -63.64283 | 2025-09-05 04:38:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c25ed48-9387-36cf-9c65-84c5e640039c | -15.61877 | -52.90498 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f74bb79-b5bf-308a-9046-68845dbf4d83 | -15.16292 | -52.39616 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8828be61-f7bb-34b7-a0ff-b9ed50c79572 | -12.99201 | -54.8155 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c0cd60e0-5e13-3a61-bf97-1b6e10085884 | -15.02222 | -48.11916 | 2025-09-05 04:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75e9aba8-90df-3d7f-b945-1aa9da6c2ae8 | -18.45937 | -53.03272 | 2025-09-05 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1911688d-f9a2-35ce-87a3-934e0aab900c | -17.66161 | -52.27911 | 2025-09-05 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f88e0619-4bce-3398-9307-b4665e24f47a | -12.98165 | -54.80181 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fafeb9aa-4d23-3425-a48a-382b8044d4d3 | -12.99546 | -54.82009 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3b6bc201-b36e-300b-b046-f9559968f893 | -12.97064 | -54.79186 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fba16b62-5340-3d3e-a783-2f3fdb15eab0 | -12.96308 | -54.78646 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dae744cf-13a9-30de-925c-13ac49e60097 | -12.96995 | -54.79564 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 62d441be-2e8f-30a4-b0d7-c07b953a3783 | -15.06765 | -50.06062 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b0d4ec4-4725-34fd-9344-d019122b9e8a | -14.28036 | -45.2236 | 2025-09-05 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4b21fa07-e093-3128-8945-5a0e69e2eb3a | -12.99823 | -54.82852 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5c631486-d7c7-3553-9ae2-d00b2ef612cd | -15.32104 | -52.74214 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 844b6991-f98c-35a7-86a1-045942333d45 | -15.58307 | -52.87672 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 282a7bfa-3d1c-3b97-8708-6ad07ba872c9 | -14.56409 | -48.08349 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b2735af-fbbc-343c-8680-ea81a4693bde | -17.66373 | -52.28749 | 2025-09-05 04:38:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f99ea6b6-6854-3164-a8b2-1128f493c937 | -15.54379 | -48.40371 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3586a137-58b5-3361-80f7-56baff93088f | -13.27745 | -51.79208 | 2025-09-05 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa081c60-a6cb-3cdd-aa20-49cb576a964c | -17.5832 | -49.77859 | 2025-09-05 04:38:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bfbd867-9bb6-3afe-ac1d-971a0d1b8020 | -18.23837 | -42.66875 | 2025-09-05 04:38:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cb5fe552-4d21-3b4a-9484-2f5346b6ecab | -15.20315 | -52.37245 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c2e5dc61-11b7-3e8b-90cb-eb53700fc95d | -15.73921 | -53.61919 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d33bfddb-9297-31cf-8154-83eb39d1fa89 | -15.60803 | -52.90313 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a207e7a1-6919-3c74-9a91-061bcb467a81 | -14.28878 | -45.21978 | 2025-09-05 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3cdc4bc-6070-3555-91b5-6a98ee01d618 | -15.2029 | -52.37352 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c484c17b-d7df-3c07-9e7d-44f731176c95 | -15.54267 | -48.41115 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15cad783-a90a-39a4-9ca7-4adc1ee23265 | -12.91018 | -57.00533 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a044a5c8-3baa-35b6-95f6-3e324b0b2c93 | -15.70832 | -53.59932 | 2025-09-05 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da224682-a35b-37af-831c-12159104cd44 | -12.63933 | -56.9841 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81fb339e-4ff4-3b41-aaa8-2a5c1bd7b67f | -13.33874 | -54.38753 | 2025-09-05 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb798b6d-e88c-3755-8fa1-6550b4e059fe | -16.90656 | -45.7474 | 2025-09-05 04:38:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bb99f30-fad6-3348-b41a-7a13ca5dddea | -15.07098 | -50.06118 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d997550-c75b-3047-90fd-99fd267a568c | -12.91117 | -57.00006 | 2025-09-05 04:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3f21ddf-7780-3e3c-8094-c9d5dd26956d | -15.20247 | -52.37641 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 92a47e09-5911-3ce3-b695-8bb25666b609 | -17.24158 | -46.71643 | 2025-09-05 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d2a16a5-dea0-3276-bbf9-3ace642e96c5 | -17.5336 | -46.60852 | 2025-09-05 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6392eff3-069b-30a5-98bf-ded2e0ae6fa5 | -12.99754 | -54.83237 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 573f121d-f0be-327a-8a18-813b7ebdd05e | -12.95963 | -54.78193 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e5133b2-adb4-38c5-8f8e-f8cd229e24a6 | -12.97408 | -54.79646 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48402f15-99bc-39c7-b532-49643d17064d | -12.99337 | -54.80792 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b14a0fc1-7c26-32fd-92f1-335ac228544c | -16.32542 | -52.95164 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c60310c-e3bb-39d1-a884-425410ae58a6 | -19.60862 | -43.16108 | 2025-09-05 04:38:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c3eeb536-b02d-3ff5-9b0a-4275ec0d5d24 | -17.97205 | -46.9043 | 2025-09-05 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0ca6d18-b4af-3000-b64f-cef34cc2f59a | -16.32186 | -52.951 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd71ce0f-72e1-3faa-8902-95701c9865bc | -15.54207 | -48.39198 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a20e568-4705-34b8-b60d-5e059c0368b3 | -15.54889 | -48.416 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README37.md)
