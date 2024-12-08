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
| bad37fdf-97d6-3a78-b3ed-cdd02514077f | -16.83967 | -40.18098 | 2024-12-08 03:51:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1a5c5291-bf71-384d-b700-f9241103ee94 | -15.35434 | -39.8727 | 2024-12-08 03:51:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 22641df3-3519-3676-beea-c02d48271c2b | -16.19811 | -41.05124 | 2024-12-08 03:51:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 29e545d9-e99e-323d-896b-d010beef4f57 | -12.5397 | -48.32278 | 2024-12-08 03:51:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 061e8684-d3e6-3195-9599-bba8ff57319e | -15.95318 | -43.4056 | 2024-12-08 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f694b20c-a6ac-33fa-ae35-b4786a2ab115 | -15.36683 | -53.12959 | 2024-12-08 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 009ec5f4-830f-3664-a95f-2ce9c3a7b856 | -16.68184 | -43.88611 | 2024-12-08 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd9bd054-1de9-30c4-9b30-9dbd947b4987 | -12.86353 | -51.93461 | 2024-12-08 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a228e374-c7cf-3b13-a662-6260abc7a485 | -17.8117 | -42.94211 | 2024-12-08 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0437c8cf-dd7e-34e6-bb82-13457c34eff6 | -20.75539 | -41.75008 | 2024-12-08 03:53:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9b24c07b-6365-3d46-ae54-dfc83058c6e1 | -20.77254 | -41.89865 | 2024-12-08 03:53:00 | NOAA-21 | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f514ed41-90e5-3b86-a16c-708d7d7c3ed4 | -20.75204 | -41.74944 | 2024-12-08 03:53:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| eb921ec9-62fd-3d3b-a5ae-aaf8176631e5 | -20.20067 | -41.78766 | 2024-12-08 03:53:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2a79b02a-773f-376b-9351-092aab427bf3 | -18.71158 | -43.21458 | 2024-12-08 03:53:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f23d3a79-658a-362b-b9a7-905807bf95d8 | -19.14673 | -52.6484 | 2024-12-08 03:53:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7db6ec3c-2cd2-3a07-a667-1ad10150786b | -20.75937 | -41.7469 | 2024-12-08 03:53:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2eb5115a-53c1-3cbe-852b-e2a007d92311 | -20.20405 | -41.78825 | 2024-12-08 03:53:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f0280ad-19dd-3f64-a594-da5f5ab525c1 | -20.26917 | -41.32864 | 2024-12-08 03:53:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eb1a78de-db08-3d11-b114-4a7b0b4ce9fc | -19.83805 | -40.08366 | 2024-12-08 03:53:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b18e00e7-d420-3e60-972c-3f6748d32df9 | -19.31708 | -39.89301 | 2024-12-08 03:53:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| be2603ab-2ea9-3420-adfb-2b3d7cf509d2 | -18.95066 | -53.6951 | 2024-12-08 03:53:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cc2023e-4129-3a26-a5ef-ce5fdc4868b8 | -20.26612 | -41.22077 | 2024-12-08 03:53:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2d5bd720-d7f1-39c4-bf4f-fe50a287bdcf | -20.13575 | -40.20251 | 2024-12-08 03:53:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 89a56385-ac8e-31f5-af8d-b6fc6af0e494 | -20.75602 | -41.74625 | 2024-12-08 03:53:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1fa8a8f7-d70b-33e0-8d11-a5ee1f95a3d9 | -19.26582 | -40.11243 | 2024-12-08 03:53:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f9df5576-cd65-305a-a423-d758d894c2dd | -19.36325 | -41.51534 | 2024-12-08 03:53:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f7eba42c-229b-3f4e-891e-8d136f9bfaa7 | -20.27252 | -41.32924 | 2024-12-08 03:53:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9038b574-769d-3ddf-8bd9-43f6dad35230 | -17.82173 | -45.3177 | 2024-12-08 03:53:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e872f31-1ac4-30d5-af21-8006bc484b8b | -18.95732 | -53.69684 | 2024-12-08 03:53:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51c38126-5c2d-3e40-9cb8-4dc07028d036 | -20.20467 | -41.78447 | 2024-12-08 03:53:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fc3e06f2-4343-37b5-9f93-6c630564c78f | -20.51204 | -44.0873 | 2024-12-08 03:53:00 | NOAA-21 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 15d69cd9-1c30-3bfa-98e9-dde8ae3bed19 | -20.41875 | -43.5525 | 2024-12-08 03:53:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ef76bce4-1589-37c0-b904-8aa81f5bfa9d | -19.41704 | -44.74195 | 2024-12-08 03:53:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c41a0038-9dba-3b8e-a453-b2eed895cede | -19.26308 | -40.10822 | 2024-12-08 03:53:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 396ff408-645d-3d69-92cf-a5b57568764a | -20.8805 | -43.85386 | 2024-12-08 03:53:00 | NOAA-21 | CRISTIANO OTONI | MINAS GERAIS | Brasil | 3120409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fc1f66e7-5d35-36de-ae52-1d654346dc6e | -19.26251 | -40.11185 | 2024-12-08 03:53:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8c4384e1-3a60-3649-a8e5-85f34c1ca0e5 | -20.27314 | -41.32541 | 2024-12-08 03:53:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a101835f-1ffb-363e-ac10-51e9e41c25c0 | -19.3037 | -45.54593 | 2024-12-08 03:53:00 | NOAA-21 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd7d0940-a8cb-3798-986e-6bfc379dcc33 | -11.752 | -54.7255 | 2024-12-08 04:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| f0fa99d9-8866-3a78-b859-7a79f5b0faa9 | -5.4784 | -39.41829 | 2024-12-08 04:12:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c3a9642e-4410-38ab-9552-ed4d942b81f0 | -5.6965 | -39.40287 | 2024-12-08 04:12:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93ed224d-7217-3e48-8fa0-2fd2b630a3f4 | -5.24832 | -37.50337 | 2024-12-08 04:12:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f1d272f1-654f-3951-9eb8-e9b0ee22f57f | -4.92322 | -40.52277 | 2024-12-08 04:12:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f914d548-ca33-38df-aaa5-59c8e6255541 | -2.63961 | -44.94009 | 2024-12-08 04:12:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d475db7-6786-3f0b-b634-94a319c9c7cb | -5.25371 | -37.50703 | 2024-12-08 04:12:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.1 |
| aeca1328-254d-33ff-8855-e8f6d3766813 | -4.54466 | -40.51778 | 2024-12-08 04:12:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 327963e5-fc52-3e1f-a06e-b145931a289b | -5.3634 | -40.86304 | 2024-12-08 04:12:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 46a9ccff-349d-3acd-bf08-a74dca8ce5b2 | -1.64707 | -45.91258 | 2024-12-08 04:12:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| add09c83-34b4-37d1-a54d-256642e550ac | -5.25012 | -37.50268 | 2024-12-08 04:12:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 541b0abd-27b0-36bb-8756-f4a95384cb66 | -5.00732 | -40.7016 | 2024-12-08 04:12:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1480c5bb-9135-3273-9979-30e2a0f579ff | -5.47538 | -39.41338 | 2024-12-08 04:12:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5552d418-df06-3171-b642-3f45b1d2a601 | -1.6485 | -45.90351 | 2024-12-08 04:12:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0041dd93-ea93-3e87-8c9f-0fb56d748c0c | -4.91267 | -39.01345 | 2024-12-08 04:12:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 838839a9-c6c4-3117-b1ae-198d89b6c209 | -2.23592 | -45.5807 | 2024-12-08 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71bab82f-c9aa-30ce-bf8a-90b7018e5203 | -4.35099 | -40.63511 | 2024-12-08 04:12:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f776e91d-ddc2-3061-9575-b51ea548a8e2 | -5.00674 | -40.70536 | 2024-12-08 04:12:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a81de9e6-3c0f-313b-97dd-956a2dde5d56 | -3.85718 | -40.44696 | 2024-12-08 04:12:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 61565217-c9b3-3740-afdb-7eb9a424fec0 | -2.02154 | -46.63353 | 2024-12-08 04:12:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7abbe43-2a77-31ad-92c0-61a0bc6ed997 | -2.64315 | -44.94065 | 2024-12-08 04:12:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3365b39-701b-3a84-9939-beb3f591c06c | -5.47907 | -39.41395 | 2024-12-08 04:12:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e4615c46-8841-3aef-ad80-1b799389d331 | -1.77601 | -46.49212 | 2024-12-08 04:12:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e0e7864-8bb9-3cee-a997-464285d13429 | -4.91206 | -39.01102 | 2024-12-08 04:12:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| baef4c9e-f231-3df2-a3a1-af8101845cf6 | -5.44194 | -39.43484 | 2024-12-08 04:12:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b35f1c56-48c4-3831-853b-bca81f3a8b29 | -3.86064 | -40.44749 | 2024-12-08 04:12:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b90ac1ee-2cce-3738-a923-95d4a5feb171 | -5.25425 | -37.5033 | 2024-12-08 04:12:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e4761096-600c-3329-be05-ebbdd1e8990e | -4.91581 | -39.01159 | 2024-12-08 04:12:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d43b654-7897-34a4-a406-15931bf710ed | -5.47471 | -39.41772 | 2024-12-08 04:12:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c641a026-ec2e-39e7-9797-d956d10ff0f8 | -1.65156 | -45.90865 | 2024-12-08 04:12:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc73a109-94f3-319f-a3af-45cc13a7edb5 | -5.23642 | -39.36692 | 2024-12-08 04:12:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 51e3bbe2-c836-352c-aea2-7cf14a764323 | -1.64779 | -45.90805 | 2024-12-08 04:12:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2138210e-c9f3-3fe9-b442-69f846eed8fa | -5.53744 | -42.88044 | 2024-12-08 04:14:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d030487-e81a-3099-8e17-29d0da9728d1 | -4.58326 | -48.01626 | 2024-12-08 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| aba767f6-66ce-37da-9cdd-468f264182f7 | -5.91984 | -48.0295 | 2024-12-08 04:14:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bec3cde7-6447-3ab7-a4bf-9915532e4bc0 | -9.9958 | -36.33779 | 2024-12-08 04:14:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 31be55c9-4f7d-32a4-9646-6b50cafd6f2f | -7.88063 | -44.20148 | 2024-12-08 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a7683b0-749b-3c92-92da-9e6317b7381c | -5.42502 | -44.7085 | 2024-12-08 04:14:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7042a0e-67c0-3189-bb63-d05d6cd2944a | -4.56838 | -48.02919 | 2024-12-08 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bce7f7e-271b-33a6-ba52-0102ee33e5db | -4.82418 | -48.09741 | 2024-12-08 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36477725-73b7-3ed3-ac42-5627a0f36f98 | -5.53467 | -42.87645 | 2024-12-08 04:14:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8a45f642-da53-37c1-b198-083166074788 | -7.99142 | -45.79181 | 2024-12-08 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0594bb45-73c4-3b67-aca2-ee69ec7fa5be | -5.52408 | -46.96185 | 2024-12-08 04:14:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 325823d4-d7e8-3e36-a828-b7bcb82cb4c9 | -10.00134 | -36.33308 | 2024-12-08 04:14:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ccd2c0a2-b5da-38c8-b314-42dd97bb2cf2 | -7.88397 | -44.20201 | 2024-12-08 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8f6cab3-245d-31d3-8a52-46149ba4d009 | -6.29436 | -43.85175 | 2024-12-08 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 898ee1c2-f043-3244-9e8f-9c2eef6d9ec4 | -9.99505 | -36.34327 | 2024-12-08 04:14:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 76f47c5b-7855-3a2b-be85-25ad2b1515a6 | -4.89343 | -48.05155 | 2024-12-08 04:14:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75c9252b-32fa-3631-82f8-80619f406fdd | -7.52908 | -47.29509 | 2024-12-08 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb0c8189-dca3-3555-97fd-bcef572373c3 | -6.68538 | -47.66323 | 2024-12-08 04:14:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e543a8d6-bf87-3745-b43d-a67ee60f16af | -6.20566 | -46.06665 | 2024-12-08 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2fde7d5-2e01-33b6-992d-f8930cb123c2 | -8.05289 | -47.89871 | 2024-12-08 04:14:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b43ce3d2-9e79-381b-8ae1-f14949ce3f4e | -11.34523 | -38.14367 | 2024-12-08 04:14:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 036b433e-ddd7-3392-a412-b041efdc1bde | -12.40188 | -46.5978 | 2024-12-08 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9c658af-63d3-3a99-9e97-22ee5d793617 | -6.45328 | -43.74084 | 2024-12-08 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ce1a00af-216e-3826-b301-c2f31dc92b01 | -5.90767 | -48.02768 | 2024-12-08 04:14:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c531622-8946-3c84-89e8-e6d8f07187a5 | -9.21965 | -49.4799 | 2024-12-08 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c14b63fd-8bcd-3619-8538-bac2e6212c03 | -5.9065 | -48.0347 | 2024-12-08 04:14:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df216ca9-2365-3945-b365-9293c79abbd5 | -4.89403 | -48.04798 | 2024-12-08 04:14:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8e85046-637e-306c-ae64-622f6e6fb713 | -6.42648 | -46.47416 | 2024-12-08 04:14:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d392d44-79a9-3104-9051-723cca73ecd4 | -7.9783 | -50.69904 | 2024-12-08 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a86a05a2-1f5e-370d-a2e2-28ec98831892 | -9.11408 | -49.46657 | 2024-12-08 04:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README6.md)
