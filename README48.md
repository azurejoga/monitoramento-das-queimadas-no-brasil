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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| decde408-c2aa-3c27-929b-24c0cf899c0a | -13.71841 | -52.01501 | 2025-08-26 04:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d38106c9-8f48-3f2e-b0ff-81cb2cc9b258 | -9.16774 | -59.54851 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 11371946-1bd3-32b6-b5fc-6445358bdcce | -11.29537 | -53.9612 | 2025-08-26 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9be23a1f-c941-3b5a-9ba8-6355ce963b9a | -12.77277 | -48.12414 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b1780e1-0741-38ce-be0e-6e2f0257a07b | -9.18013 | -59.52257 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c1a145d5-8cce-3642-911e-42a70bf975ed | -14.29221 | -60.35462 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8cc1f620-fe51-3559-bb75-88d6e450f8a3 | -14.72592 | -45.37132 | 2025-08-26 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0c37d35-63b2-3746-834e-a1a29bac716b | -15.17478 | -48.18879 | 2025-08-26 04:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc8b97d7-1653-3e21-9ee2-33b7bd94bc21 | -13.35295 | -54.39539 | 2025-08-26 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 669347cf-9171-30ec-ac5c-78e2dc1eb6fb | -13.44387 | -46.86545 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64d0dfe4-ebf4-39bd-92cb-375f9e18e29c | -13.64171 | -45.70128 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a09818a-d437-3f7d-b81c-f3df733fbab3 | -11.30902 | -55.11214 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7a75bf93-61ae-33cd-87b4-682ede4715e4 | -10.54377 | -57.96343 | 2025-08-26 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c325b41-af9b-3b95-b0b7-722ead12b36e | -15.04787 | -48.5139 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec0651b9-c510-343f-9206-ee58d8868d84 | -13.43635 | -47.01878 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9961d4f8-4e63-31f0-a639-25cabf73eec5 | -15.02448 | -48.16758 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32fedbad-a00c-3b06-b09b-0dffd1d6d12a | -13.63556 | -48.15058 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8935e93f-3502-350f-9b44-cd62a3827626 | -13.52494 | -46.90836 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d730ead6-4d1e-3b0e-b391-c469e1dc5843 | -11.55163 | -52.11024 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b923fde-3768-3396-8b8a-a23f5068121c | -15.06463 | -48.54085 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f52bf8d-571c-3ee1-bef6-cf657241687b | -12.7754 | -48.10844 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38fcc785-4dfb-3b37-95ff-b59d5eb97aa2 | -12.74876 | -48.15249 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0094eef1-fdaf-3c12-9c96-3d52afb6a080 | -10.87292 | -55.79155 | 2025-08-26 04:23:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 627e2660-b540-3a8d-bb18-9323996ce210 | -14.27616 | -49.13156 | 2025-08-26 04:23:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6675efeb-3442-3e85-8d13-5ad220d8af73 | -13.49944 | -46.88228 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b57c1d96-6b71-31bc-8a28-61ec5f9f4441 | -14.239 | -44.11832 | 2025-08-26 04:23:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8d6a9c6-4e3d-3a8c-b103-f9356f9020b1 | -13.82169 | -45.89088 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa701189-b0fd-3552-8d26-ce12e9f94eaf | -11.54646 | -52.11373 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7061cf8-50b8-3338-a960-77b2f1e0b0d1 | -13.52102 | -46.91141 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b074bab-4920-3f86-896b-7ed2c6c93e5d | -14.34553 | -51.94805 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 094b7d57-de27-320c-8a25-122c344dad37 | -16.74464 | -47.6017 | 2025-08-26 04:23:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bda2337e-dfe9-3798-b138-91ac93509a4d | -14.24474 | -53.04637 | 2025-08-26 04:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9084bbdd-d9e0-3552-8419-f3509cd180ed | -9.184 | -59.50563 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67ed9b99-240b-305a-bfac-05a154ff1585 | -17.21383 | -47.22435 | 2025-08-26 04:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26836376-941e-31b4-8321-7c4c34c84083 | -14.72033 | -45.38538 | 2025-08-26 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 251d10bc-d1d5-368e-ac5f-8e9dfc13f056 | -14.30785 | -53.06513 | 2025-08-26 04:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5477028b-b09d-32da-874e-095035dc132f | -14.30696 | -53.06982 | 2025-08-26 04:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86d674f2-f336-3ce2-9738-c5a50818c5d5 | -15.32016 | -53.84203 | 2025-08-26 04:23:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77dbbfe5-25fd-3792-9c02-42f2594daae5 | -14.29668 | -60.35446 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f43f0da-a870-380e-81a5-83abb52aa0cd | -12.43907 | -48.71571 | 2025-08-26 04:23:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcd20c54-91c8-37ba-8b69-d79c8dc72f49 | -13.42086 | -46.90196 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b95a4992-6e45-3ad5-a39d-9cbbc04a2ca5 | -15.02386 | -48.17137 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 004a8205-f1c5-3337-8292-61f5513be3a2 | -12.94621 | -46.33775 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c1fb828-637d-39ea-89d0-00e9dd611571 | -14.72145 | -45.37807 | 2025-08-26 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8007e7c1-494f-3bce-94cd-95d3af542591 | -15.82489 | -45.77027 | 2025-08-26 04:23:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0327ac13-1504-3148-9a0a-c7916f1bee83 | -12.02515 | -49.70989 | 2025-08-26 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fbea47e-f156-39fe-a7a3-70c0dade4b34 | -12.37729 | -46.55038 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53e83b9c-625e-38c8-976d-38134cf95527 | -15.14027 | -48.67303 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeae79a4-86b0-3c68-95cf-7737ebf8a0c7 | -15.10794 | -48.73904 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48d878e2-dd21-3c31-9c23-533b0a84de86 | -14.10871 | -53.98236 | 2025-08-26 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 569c5ab5-2b20-3670-ac12-99ea566296b3 | -9.17722 | -59.53738 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a9c7f84a-fd02-3faf-a88f-ca57545943c6 | -11.52416 | -52.13636 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6de55efa-a5d8-3411-a039-d6db3baf768a | -12.75096 | -48.16072 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02ba107e-298b-3907-aaee-0ca6615bfd6d | -15.02851 | -48.50289 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 314027a0-b853-3531-8834-d085092ccf1c | -16.6249 | -49.36824 | 2025-08-26 04:23:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f62d429-6c9b-38dc-aa70-74896ff5a775 | -14.11346 | -53.98329 | 2025-08-26 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 38e17fdc-73b5-3021-a8a7-6f6d480e0fc9 | -13.06163 | -46.31282 | 2025-08-26 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 617a0b8f-8c27-31f7-aef1-044caafd906b | -14.29535 | -49.14761 | 2025-08-26 04:23:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd562777-48e0-3d29-9852-798972e1f23d | -12.954 | -46.33171 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6670e810-7551-3922-8dd7-061429814cd5 | -11.62615 | -46.21602 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c2e63c4-7a79-3a2b-a143-d6d0e0e973b3 | -9.16651 | -59.51752 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 360b5559-35cd-33b6-8be9-de68afe27e1a | -14.42927 | -48.36642 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dee87523-e73a-38c8-a6fb-327faae8b915 | -12.76673 | -48.1078 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 621cbc12-df0c-3148-a9b8-90ccedd8e39f | -11.50163 | -52.13817 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 06c736c9-75e8-379b-a159-b5dca452a7e3 | -16.32009 | -43.62141 | 2025-08-26 04:23:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97f2d2a3-3c14-35f5-a39a-0a8c7c5393d6 | -15.03272 | -48.69073 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 889f58fb-1bf9-3a62-acbc-e7b17cb4b11f | -10.61515 | -54.89281 | 2025-08-26 04:23:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b63869fb-d99c-3a67-a6de-7bd55806a6a0 | -15.64716 | -52.7319 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf9cd344-5a3d-3539-9657-0f1aa9451688 | -12.76197 | -48.14616 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| deb60f15-9b8f-35d7-8e59-104c93738d13 | -9.17577 | -59.54478 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7c86b878-0d20-3669-b007-216f34a8cb98 | -12.95343 | -46.33528 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e91f17b-7d62-38c4-90a7-ee2494ef105d | -13.64504 | -45.70183 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcb09ec1-af3f-3e8d-b3e4-e2c38cdb1c40 | -9.17278 | -59.44985 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2edb6326-16a2-386e-8bf0-f61da65c9812 | -11.53972 | -52.12579 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1032204b-4c3d-32f8-bd0c-eb63204898fc | -15.13618 | -48.67633 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 922bc7ab-f325-38a5-92c2-7badcfeb5a10 | -12.42064 | -46.81425 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d909df44-512b-3da5-899e-0aa45dc7a70b | -14.30855 | -60.36667 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d174a32a-39c7-3e1a-9f62-753a11f11aac | -13.44259 | -47.00132 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee1b8825-194f-3df2-8d7f-9ff3732e9e3e | -14.71808 | -45.37753 | 2025-08-26 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2989527-9091-3bca-b273-afe92553d11f | -13.58383 | -48.19358 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d15f6be-ceff-34f3-9d6e-a004033b89a0 | -15.10813 | -48.63164 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d620dc57-cc10-36d4-9fc9-42a46893ce9b | -15.03312 | -48.15743 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3a70320-f8cf-394b-8699-d803ba581539 | -12.7315 | -48.14931 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c48ed2ed-ae56-31b6-8b60-28a85a59604d | -15.62184 | -52.70182 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f03c5d2-5874-3217-bffe-e50c1aab1bcb | -13.43604 | -46.87157 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02a036d2-a7c1-3305-bb54-b47ee11cd6fb | -13.00599 | -56.89164 | 2025-08-26 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7c0fe3f-b420-3050-b0c5-b430bec614ae | -11.63004 | -46.21303 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61cf9126-6984-3ac3-963a-422af77871e0 | -14.34966 | -51.94887 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d339093-2a6f-3c44-b319-25a50a723d3d | -15.0654 | -48.69564 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6762ad5c-8ac6-355d-b68a-43b85f26300a | -9.17143 | -59.52851 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 33d5d537-0802-3e22-82fe-94aca45139f7 | -13.05888 | -46.30873 | 2025-08-26 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 397f0ff6-8bb0-361b-93f6-c333e59cbeb3 | -11.31049 | -55.11348 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8cdb8269-5dc6-38c7-96b2-2d83086788a6 | -13.26309 | -43.54256 | 2025-08-26 04:23:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 390a6654-266f-368b-b810-0861d197fb1a | -14.25351 | -48.03291 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2a129d1-c7ac-36f2-aafc-25c5324b9a65 | -14.76028 | -59.72461 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8f99204-11e4-38c4-b951-73c3ab22841b | -12.94415 | -46.33402 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2393401f-837e-3687-bef6-fa540a687123 | -13.05831 | -46.31228 | 2025-08-26 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89e94501-83a5-3995-ba1f-35024e05690b | -13.16484 | -45.29139 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cdfc8e91-b492-31a9-b4a4-cf5f212a324f | -13.42131 | -46.92046 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c93a92ec-7a75-30a9-8ec6-912e71129428 | -11.30445 | -55.11589 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README49.md)
