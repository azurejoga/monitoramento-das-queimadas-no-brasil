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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 858dede7-14d3-3ff0-a690-3039deddb3ad | -11.22443 | -60.5826 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71dcc4e4-9669-3009-b89b-636e332d1a20 | -11.22224 | -60.57504 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3946cb63-58dd-3db0-a70e-f3faf510f9aa | -11.186 | -60.48279 | 2024-10-11 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a2ae530-87d4-3094-b34a-1d01bc07be70 | -11.18409 | -60.62289 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cc631b94-ece3-3b00-bc31-cba067f7d6e3 | -11.17361 | -60.62479 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79b7834e-0a5c-39ba-9143-c1bf705b77f6 | -11.17086 | -60.62074 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cd49630-b552-31c7-bd32-da2e4d524835 | -11.1703 | -60.62425 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e48e91a3-41f3-39b5-b813-2fdefe154f40 | -11.16591 | -60.60914 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d2a9330-fdcc-3ebd-8a7d-86fc5a958937 | -11.1626 | -60.60859 | 2024-10-11 05:21:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2c12c1c-7b26-350a-9731-a48fe2a57cd7 | -13.74607 | -60.60327 | 2024-10-11 05:21:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29461e58-57b3-3c3d-a207-f0b7e79ea1bd | -13.74277 | -60.60273 | 2024-10-11 05:21:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1db52d9-ddb3-38e8-80c6-65879cd77373 | -13.73947 | -60.60218 | 2024-10-11 05:21:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 299a62cb-80cf-3b45-9937-d748c03a87f4 | -13.34957 | -60.57423 | 2024-10-11 05:21:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad13c424-9a0a-3c2f-b969-cd33fb08927f | -12.97779 | -62.79811 | 2024-10-11 05:21:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5021d66a-ae3b-31f5-a38b-e9cb0c6da046 | -12.97434 | -62.79752 | 2024-10-11 05:21:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f56b9555-6550-36a9-ac6e-66fbc178a101 | -12.97255 | -62.79399 | 2024-10-11 05:21:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e228346-b78b-3ace-882e-bb546c3a71e7 | -12.97153 | -62.79304 | 2024-10-11 05:21:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 861ae62d-2d19-3c74-80ae-b77a01cc3ae5 | -10.58302 | -64.5055 | 2024-10-11 05:21:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 785b31c6-2ed4-3168-97a7-2a77c46c6fcd | -10.60172 | -64.96077 | 2024-10-11 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32a6a516-39a2-3f3a-8b46-cc0e1307c8fe | -10.59772 | -64.96007 | 2024-10-11 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd0c7bc0-d51e-3cbc-9562-207acee0c6ba | -10.37717 | -64.83324 | 2024-10-11 05:21:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b22e34cd-1c31-3db4-8387-64330bfa5702 | -10.37656 | -64.83676 | 2024-10-11 05:21:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91584a1a-9f7a-3b3c-b672-c83c424db5b0 | -10.71092 | -65.32021 | 2024-10-11 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c88fd48-f38e-38c9-bc1a-401646047286 | -10.70617 | -65.32321 | 2024-10-11 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4660810-8741-3aee-b472-1424fd4e578e | -10.60233 | -64.95724 | 2024-10-11 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 607d4a69-4429-3c9e-a10e-a5fbee974551 | -10.59833 | -64.95654 | 2024-10-11 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f2add03-2d67-35a8-b823-abd378351225 | -10.47066 | -65.28485 | 2024-10-11 05:21:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c01b812e-d3cf-37c9-822e-58216dd6316e | -11.68205 | -65.2252 | 2024-10-11 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8a5cca80-6994-3b57-9bc3-00ad520bfdf3 | -18.20014 | -56.45396 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d551da35-e161-3010-ab3e-a777e8af487a | -17.67435 | -56.32093 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 46d0f702-6821-3605-829a-a5127ddb7540 | -17.67221 | -56.30556 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fe7a3382-7cf1-3e25-bcbc-bc3954145ece | -17.67173 | -56.30927 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 28e8f1e7-71d9-37d0-8d81-5b287680e578 | -17.67126 | -56.31296 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 66c30e48-7090-360f-9695-eb1429c2d57e | -10.10209 | -67.34931 | 2024-10-11 05:21:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a36b63d3-be11-32e4-8436-c89532d537c0 | -10.099 | -67.34589 | 2024-10-11 05:21:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17d2f73e-c010-3aea-8a2a-0a2129f6fff4 | -10.09806 | -67.35098 | 2024-10-11 05:21:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8258edfb-551d-34c3-be31-0d81797d330c | -10.09737 | -67.34837 | 2024-10-11 05:21:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9725c04a-88f0-3f4a-95d7-dae84e75c241 | -10.09123 | -67.13903 | 2024-10-11 05:21:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87de9c13-d4c9-3ac7-b5b5-6f42bf99a1a5 | -10.08657 | -67.13818 | 2024-10-11 05:21:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d065aa9-eb9c-31ef-a331-cd3ffcbcb75f | -10.85395 | -68.28519 | 2024-10-11 05:21:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10304a75-76d4-36e5-b897-02e70b50d5f4 | -10.48494 | -67.79586 | 2024-10-11 05:21:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9b61388-3822-33ca-b343-877124a39869 | -17.7055 | -56.30285 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f5ce4861-5766-38a4-a2fd-fc0a49965851 | -17.70502 | -56.30656 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| e10d2268-1c1a-388a-8d7a-ddc0b616ea51 | -17.70146 | -56.30227 | 2024-10-11 05:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e7d48d87-25a4-305b-ab72-2a9280a94bef | -13.02756 | -53.63843 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bc4d69d-e708-30c6-9656-7b05546f0a3c | -13.02305 | -53.63779 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cea2650b-366f-302d-bfb5-bfdf898579c5 | -13.01341 | -53.64113 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66633d4a-426c-3e32-a496-7e23af2461ff | -12.99105 | -53.49475 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97a70ce8-54e8-3868-99c9-fdb9b3176ae7 | -12.98649 | -53.49413 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e0af5427-3d2d-3c1b-9e49-9fde43422a74 | -12.9807 | -53.50303 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38dfc0af-6e05-35e9-af51-6e5142007b28 | -12.97554 | -53.50712 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 382cab49-a1c1-38fd-9941-e13f44608a1c | -12.97099 | -53.50647 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fed420cf-49d0-3437-8e9e-5e67b3e45617 | -12.97038 | -53.5112 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd194d4b-a930-35ce-87a5-27a6d2e90887 | -12.96704 | -53.50109 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2049e004-01d3-3b28-acfd-0045977f15cf | -12.96644 | -53.50583 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 24e6b620-4dc1-3603-8fe0-9851ec5c35fe | -12.96584 | -53.51055 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ed2f27bd-3f71-3727-a8a2-cfc25b8c92f0 | -12.96189 | -53.50518 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f05b0c71-0462-342c-a9bf-2695aa4b1e29 | -12.96129 | -53.5099 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| dcc0c1fb-e058-3e04-be8a-3f4ca2c866d3 | -12.87427 | -53.49589 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a29caf68-84e2-358f-bc3a-5a5ce730698c | -12.87366 | -53.50057 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4909cd6-bff3-34b9-8021-3e7426c59f94 | -12.86972 | -53.49527 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ad3f9aa1-c302-3ab7-a068-107d12ab2bcf | -12.86911 | -53.49996 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8482c67-825b-36e4-907b-2352833cc9c8 | -12.86517 | -53.49464 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3addb08d-f2f6-36de-a7f3-01878e8d1689 | -12.86456 | -53.49934 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12bd4751-e724-3cde-9e55-399c972d9319 | -12.86062 | -53.494 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d7ba2d44-2234-3b4c-9c6d-0bc90ed7e684 | -12.86001 | -53.49871 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d687ea1c-ea10-346a-a976-8963d4965a13 | -12.85547 | -53.49807 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7932940e-feac-3f0b-bae2-f9b520f86e4f | -12.85486 | -53.50278 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83f757bc-b070-346d-8234-8ad26e897309 | -12.85092 | -53.49742 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 982e6557-acbe-3c72-a4f6-ad234593ddb2 | -12.85032 | -53.50213 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b4ad6951-6c27-3a62-b46c-3c306ca8e197 | -12.84972 | -53.50682 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6892ebe1-2e16-3a50-a818-87d243b23c17 | -12.84638 | -53.49677 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a63a71f7-081f-314b-be81-9a2c19755207 | -12.84577 | -53.50148 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 17ac91db-d677-3589-9a16-ed039792cd36 | -12.84518 | -53.50618 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd2cb11f-af8b-3d51-9c91-963cd157d49f | -12.84183 | -53.49611 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| f4d9e553-f854-377c-aa27-d1ecd6e51fdf | -12.84123 | -53.50082 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| a88245d0-65c0-3eec-bdf5-15a601092294 | -12.84064 | -53.50552 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65fd2417-5e6a-37ba-8b0d-a1235381f9db | -12.84004 | -53.5102 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad30a035-1699-3894-8bd0-146e0a877faf | -12.83728 | -53.49546 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| eac1e9fe-3a82-3c70-ab24-340622857140 | -12.83669 | -53.50017 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 67e071f4-adfc-3b2f-a5e1-f67337e2eb44 | -12.83609 | -53.50486 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2153737f-2f6f-31d2-b6f9-3f49a5cb35a3 | -12.83582 | -53.49761 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6f8a9ceb-8eef-3beb-bb83-1fd335b529dc | -12.8355 | -53.50954 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86516534-6cca-3b1f-b2e9-16340f0619c8 | -12.83519 | -53.5023 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 89c1d30f-b34a-3bd7-b122-8d69f465645f | -12.83456 | -53.50698 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e876539e-a3c3-3b30-bc9b-4733d1455e03 | -12.83393 | -53.51164 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b997792-28f8-3d15-bbda-8cbafb1a21ee | -12.83274 | -53.4948 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5e88df99-3df8-309d-b7c7-325bdafcd2c8 | -12.83214 | -53.49951 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8df7380b-f04f-3355-b0a3-6257012dde7f | -12.83155 | -53.50421 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da747318-c88d-37e6-846a-4dbbdd714779 | -12.83127 | -53.49696 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8ef645c2-7914-36a0-b6ed-69258e9e2a8a | -12.83065 | -53.50166 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2b3d7674-b211-3d4e-a1b0-c7d459f66705 | -12.83002 | -53.50633 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d26067b-0463-3d97-acc5-1062a6c8b8a2 | -12.82819 | -53.49414 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 75f77f79-8f81-3032-b0d2-f6c54a9970ca | -12.82673 | -53.4963 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1828977d-1fa1-350c-9247-ca73b96d4ae6 | -12.82219 | -53.49563 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3c2f551-04b1-3410-aa96-1dea7d30d6be | -12.62636 | -53.49967 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f90d533-7a5f-32ae-978b-a8e57b465a16 | -12.62576 | -53.50429 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba8ec7d5-0034-35a5-afc1-3f00cfdd2dde | -12.62517 | -53.50895 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cdeb3d3-e28a-3146-bc9a-e7187b9020ad | -12.41186 | -53.53157 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38269954-5e18-3f86-a6a2-92164070e175 | -12.99932 | -53.46671 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README98.md)
