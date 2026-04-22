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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a612ccc-d3fd-34c8-a370-73cf95b5dd35 | -11.77796 | -43.64809 | 2026-04-22 12:02:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 1c76a43c-b986-3af3-8e19-005a6eed5afa | -12.23496 | -44.19261 | 2026-04-22 12:02:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| df144016-393b-3fd8-b880-1ee3656a3ff8 | -11.77517 | -43.65423 | 2026-04-22 12:02:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| ec88d7ba-fa14-3c08-8180-b393e0e44739 | -11.77796 | -43.64807 | 2026-04-22 12:02:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c5aae7d6-d314-3b9e-aa0a-0e62689acc41 | -11.78667 | -43.65581 | 2026-04-22 12:02:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a76dc933-55b5-3a53-bfaa-793b38a1cf7c | -12.23684 | -44.17795 | 2026-04-22 12:02:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 8e63f0b5-5b3d-381f-bd7d-1683d61c19fc | -13.39015 | -45.33065 | 2026-04-22 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 26efad6b-619d-3dbf-b430-d1e2efa513e9 | -15.27544 | -51.29119 | 2026-04-22 12:04:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 37141af5-f94c-3fb8-bf77-5b0719a537d9 | -13.37345 | -45.32192 | 2026-04-22 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a9d65380-ee2d-3fa2-add6-bdf9b0f9f198 | -15.27693 | -51.28136 | 2026-04-22 12:04:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 34a1425f-cb61-3366-9a2d-331c77b62df2 | -13.45148 | -43.79271 | 2026-04-22 12:04:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 016632d4-2c06-3a81-af7a-082475efd956 | -12.3977 | -46.63147 | 2026-04-22 12:04:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a0975302-0e43-3200-b010-de9e0c9b9e6c | -16.23706 | -52.37241 | 2026-04-22 12:04:00 | TERRA_M-T | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3528e075-e5f0-35ac-a7dc-005fdfff00a5 | -13.38217 | -45.33594 | 2026-04-22 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| e4ec7916-f6f7-3c6f-a079-aa9f2d6c1b52 | -13.39172 | -45.31793 | 2026-04-22 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e204bb6a-9f73-3fd8-a1ec-3a2d43f7d33b | -19.19354 | -48.49318 | 2026-04-22 12:04:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 324f539e-1dd6-355d-b4eb-0c8d256063d8 | -20.7275 | -48.4115 | 2026-04-22 12:04:00 | TERRA_M-T | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3744ecda-4c9f-3000-a38f-e476ff15b23b | -16.32966 | -49.51442 | 2026-04-22 12:04:00 | TERRA_M-T | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b96f9859-671e-3675-9bd1-2f5bb167f011 | -17.81393 | -52.66926 | 2026-04-22 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ed231424-592b-3703-b726-94bd7115f9d6 | -12.39634 | -46.64176 | 2026-04-22 12:04:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fb9df0b4-4e87-3a53-be72-5a6498c749e5 | -13.38383 | -45.32326 | 2026-04-22 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 184.6 |
| f1a32d95-aaa9-30ec-9ebd-e1945e5f970c | -17.16621 | -46.82951 | 2026-04-22 12:04:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cca7038f-5a40-3f30-a87f-88a54fb4f012 | -15.85687 | -46.54055 | 2026-04-22 12:04:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b910e177-d835-3efe-84a1-ac1f14bf7387 | -17.76801 | -43.99544 | 2026-04-22 12:04:00 | TERRA_M-T | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d034773b-9674-3d5e-aca8-a5549d7fe829 | -15.27693 | -51.28135 | 2026-04-22 12:04:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cdf07dc8-d476-365f-bc88-d0cb40c35f3e | -12.3977 | -46.63145 | 2026-04-22 12:04:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5acaf37f-04fa-3ce5-be41-c5c2c84866ed | -13.37345 | -45.32191 | 2026-04-22 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7cdcbcce-a50e-3870-b809-a1c22ebd6249 | -13.39173 | -45.31791 | 2026-04-22 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0ab0c027-3181-34b3-8c7a-761525993ea4 | -19.19355 | -48.49316 | 2026-04-22 12:04:00 | TERRA_M-T | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 21583262-ae14-3094-89a6-d8c6e129c473 | -15.27545 | -51.29118 | 2026-04-22 12:04:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f7c89e11-fab8-36a2-aa86-a7b0381e654c | -13.38383 | -45.32325 | 2026-04-22 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 6989bff8-4f06-3185-9595-96a3b9acfc37 | -12.39634 | -46.64175 | 2026-04-22 12:04:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 94d95cc7-593e-3d07-8e07-aa4208e90c12 | -15.85687 | -46.54054 | 2026-04-22 12:04:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 20.5 |
| a71c9bb3-8653-3608-8327-14ad05070f4e | -13.39015 | -45.33064 | 2026-04-22 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| a7719611-096a-336f-bf74-762edbea613b | -20.7275 | -48.41148 | 2026-04-22 12:04:00 | TERRA_M-T | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7f9af03e-877d-3acb-ad55-a3f9edc0b3ab | -13.45148 | -43.79269 | 2026-04-22 12:04:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| de80607c-7682-30b6-8359-a1577c538397 | -13.38218 | -45.33593 | 2026-04-22 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 5b5a723e-eead-331e-b50f-854b985556ea | -16.32967 | -49.5144 | 2026-04-22 12:04:00 | TERRA_M-T | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a9ad4a1-c0a6-38fb-9a00-ff79c96ac577 | -17.76801 | -43.99543 | 2026-04-22 12:04:00 | TERRA_M-T | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9cc1dd59-4fac-34d0-b837-aabe138e75e0 | -17.81393 | -52.66925 | 2026-04-22 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8c17b76d-ebba-38e3-96e6-6db3467d110a | -16.23707 | -52.37239 | 2026-04-22 12:04:00 | TERRA_M-T | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 155c216b-3f80-3bbe-a8e8-cbab38d61c24 | -17.16621 | -46.82949 | 2026-04-22 12:04:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| db53eb47-693f-3657-be25-22f40e555608 | -24.95764 | -49.63258 | 2026-04-22 12:06:00 | TERRA_M-T | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| fc5e46de-6672-3784-b11c-e2652b3b0a65 | -28.56496 | -49.33153 | 2026-04-22 12:06:00 | TERRA_M-T | URUSSANGA | SANTA CATARINA | Brasil | 4219002 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 79e7b738-e478-3e67-a5f8-c5f4a6b2d613 | -23.30732 | -51.36385 | 2026-04-22 12:06:00 | TERRA_M-T | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| bb4d9e45-de67-3df9-ae24-fa4a85019ad6 | -26.99364 | -51.99926 | 2026-04-22 12:06:00 | TERRA_M-T | IRANI | SANTA CATARINA | Brasil | 4207809 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 39bce928-d7de-3a47-bf5e-e163b547a96d | -25.20803 | -49.40503 | 2026-04-22 12:06:00 | TERRA_M-T | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| cdaf9c07-86fb-3a65-821f-875688477d65 | -22.96364 | -52.69362 | 2026-04-22 12:06:00 | TERRA_M-T | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fa7dc857-ffd3-3ad4-9159-08cb0325f9e4 | -25.24849 | -49.15958 | 2026-04-22 12:06:00 | TERRA_M-T | COLOMBO | PARANÁ | Brasil | 4105805 | 41 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| 2ee0874b-b682-3bb3-858c-9c96877500a5 | -28.56649 | -49.31889 | 2026-04-22 12:06:00 | TERRA_M-T | COCAL DO SUL | SANTA CATARINA | Brasil | 4204251 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 46c7e909-ef26-31df-9ffe-f1b86d1cf59f | -28.56698 | -49.32494 | 2026-04-22 12:06:00 | TERRA_M-T | COCAL DO SUL | SANTA CATARINA | Brasil | 4204251 | 42 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 6b484d85-cf2e-34fb-87c5-8708e376c598 | -22.60721 | -49.29718 | 2026-04-22 12:06:00 | TERRA_M-T | PAULISTÂNIA | SÃO PAULO | Brasil | 3536570 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0ef3af5-8339-32cf-a8a8-787ef3ce49c1 | -24.95089 | -49.63588 | 2026-04-22 12:06:00 | TERRA_M-T | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 6e11462d-9626-3652-a137-775a43cceebf | -22.96364 | -52.69361 | 2026-04-22 12:06:00 | TERRA_M-T | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4be29b37-7588-3945-a396-a060960412d1 | -28.56698 | -49.32492 | 2026-04-22 12:06:00 | TERRA_M-T | COCAL DO SUL | SANTA CATARINA | Brasil | 4204251 | 42 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| e47ac612-3b71-3b5f-be72-837912f298fa | -25.20804 | -49.40502 | 2026-04-22 12:06:00 | TERRA_M-T | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 3f50d101-c751-3530-9361-474002ad99ed | -28.56496 | -49.33152 | 2026-04-22 12:06:00 | TERRA_M-T | URUSSANGA | SANTA CATARINA | Brasil | 4219002 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 6d20eb3a-82d9-3298-b82e-d20832615196 | -23.30732 | -51.36383 | 2026-04-22 12:06:00 | TERRA_M-T | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a5d1b9f7-a35e-3039-bb20-0e69a6a5313b | -24.95764 | -49.63257 | 2026-04-22 12:06:00 | TERRA_M-T | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 0dd56d32-46e5-33b7-9554-34ecada63db6 | -26.99364 | -51.99924 | 2026-04-22 12:06:00 | TERRA_M-T | IRANI | SANTA CATARINA | Brasil | 4207809 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 05fb955b-9403-3239-809c-506d1327e743 | -25.24849 | -49.15956 | 2026-04-22 12:06:00 | TERRA_M-T | COLOMBO | PARANÁ | Brasil | 4105805 | 41 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| 742f4579-6534-3dc5-9812-d3718513171e | -22.60721 | -49.29717 | 2026-04-22 12:06:00 | TERRA_M-T | PAULISTÂNIA | SÃO PAULO | Brasil | 3536570 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a6e4814-7ef2-3688-a193-cca7f8587aa3 | -28.56649 | -49.31887 | 2026-04-22 12:06:00 | TERRA_M-T | COCAL DO SUL | SANTA CATARINA | Brasil | 4204251 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| d271b46f-6881-3094-b295-2ff0f35ab216 | -24.95089 | -49.63587 | 2026-04-22 12:06:00 | TERRA_M-T | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 15679f4f-0ddd-3256-8e4b-c425fd090084 | -13.3761 | -45.3243 | 2026-04-22 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 78b0b4d7-03da-3314-8ccd-34119fe99fa5 | -13.3955 | -45.321 | 2026-04-22 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 9cb5ae59-6f2a-36e6-87fb-ca2f746a39e6 | -13.3955 | -45.321 | 2026-04-22 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 7778cd0e-a430-36d1-84e2-a75971ea38f8 | -13.3761 | -45.3243 | 2026-04-22 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 5ee40397-b17d-3f2f-9318-33a0b6b9a146 | -13.3955 | -45.321 | 2026-04-22 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 895c8abd-1c03-3314-b2bc-f197de995f4a | -13.3761 | -45.3243 | 2026-04-22 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 093effcd-b925-3bc7-9c09-4ba7322460d3 | -13.3955 | -45.321 | 2026-04-22 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 7610e3d2-741d-3a0d-abfa-a5780b74ff53 | -13.3761 | -45.3243 | 2026-04-22 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 0f07dd67-22e0-3834-b751-6df8ea86c875 | -13.3955 | -45.321 | 2026-04-22 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 4c6906b3-0c1c-3f44-ab52-d0a91d9901dd | -13.3761 | -45.3243 | 2026-04-22 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 15f47724-d75b-382a-930a-0970c71c8ad7 | -13.3761 | -45.3243 | 2026-04-22 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 50ca3d70-ac9f-316e-9b61-a2913af96302 | -13.3955 | -45.321 | 2026-04-22 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 12b7032a-c614-3611-9255-3c310482722e | -13.3761 | -45.3243 | 2026-04-22 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 59116108-a31b-36ca-8b10-6ff235ef971e | -13.3955 | -45.321 | 2026-04-22 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 12933919-6af5-3f48-96cf-1da82ba3c529 | -13.3955 | -45.321 | 2026-04-22 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 766f07ee-32f5-3b1c-8e51-aec2131d85f9 | -13.3761 | -45.3243 | 2026-04-22 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 88923e74-1625-37a1-881b-d84341a39801 | -13.3761 | -45.3243 | 2026-04-22 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 579a7027-7eff-346e-9b09-80abe48cdab6 | -13.3955 | -45.321 | 2026-04-22 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 80693342-c4b4-345b-a3a5-7f0dd7bd3752 | -13.3761 | -45.3243 | 2026-04-22 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 5d6d1e0a-2d6a-37f3-9b2b-5f2a4ed9c3eb | -13.3955 | -45.321 | 2026-04-22 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 0dbc49b0-cfd8-3bf7-b071-5f3c10d89191 | -13.3955 | -45.321 | 2026-04-22 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| c71a117f-9ec2-35b9-91a7-3fcd5fa47882 | -11.772 | -43.643 | 2026-04-22 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 84c15222-4b41-3190-b247-2836eeb117e2 | -13.3761 | -45.3243 | 2026-04-22 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| c02ab837-3fe9-3639-afe2-8deed385cebe | -24.9702 | -49.6296 | 2026-04-22 13:50:00 | GOES-19 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 96.9 |
| ef406a19-5c00-3f91-9052-ddfc642a7ccd | -13.3955 | -45.321 | 2026-04-22 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| f4afaf16-2ee2-31e3-a2ed-866d7f1ec9b8 | -11.772 | -43.643 | 2026-04-22 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 782d367e-baaa-33d1-b6ac-654decb94473 | -11.772 | -43.643 | 2026-04-22 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 0bac8d44-7c82-3b77-9c91-76451ef3150f | -11.772 | -43.643 | 2026-04-22 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| c80537a5-be4a-3331-aa01-0144c7d81e4e | -12.2421 | -44.1807 | 2026-04-22 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 036f4d3d-4e28-3910-b11b-526b34c25144 | -11.772 | -43.643 | 2026-04-22 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| af6edab0-fbdc-3791-8113-b5abe9522ff9 | -12.2421 | -44.1807 | 2026-04-22 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| fb2df262-a804-3cfc-b0c2-36dbcb9395e2 | -11.772 | -43.643 | 2026-04-22 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| fd12cffd-1e1e-36ea-9721-a39459add68d | -11.772 | -43.643 | 2026-04-22 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 6f86e19a-e764-3f4f-b230-7e46438836ef | -13.3761 | -45.3243 | 2026-04-22 15:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| b7779830-3bb9-3eb3-a179-7187d8dc3a7e | -11.772 | -43.643 | 2026-04-22 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| cb47f8c5-ec9e-33ea-8aad-7764791df7a1 | -13.3761 | -45.3243 | 2026-04-22 15:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |


