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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5195dc1-8bf0-3e2e-820c-7ed301b5573a | -20.51912 | -46.30962 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76a03e97-f95f-36e8-8711-3f0ca4af03ab | -20.51827 | -46.31343 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9c84e81-a7b2-3410-8c9b-cf87dd24d39a | -20.51748 | -46.31694 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82d9d063-b730-3217-9a9b-767718bed5d9 | -20.51666 | -46.32058 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e27b4399-d7cc-3733-9d37-45355c96f3c9 | -20.51572 | -46.32475 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3768927-b2d9-308c-91e1-80b441eccf1c | -20.51476 | -46.32901 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a5f7a93-b41b-3e7f-a814-98d6abb0f253 | -20.51383 | -46.33315 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cc22253f-9449-379e-b5ae-b73d6ad5652e | -20.51336 | -46.30842 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8614d896-dea6-31c6-879b-7c0019eba963 | -20.51248 | -46.31233 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6ebed55-f923-356e-803e-5ed9d47a0d15 | -20.51162 | -46.31614 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 199f7fec-4253-3317-8d8a-884d24f44c5b | -20.5098 | -46.32423 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcbd4da3-32e1-3deb-b8b3-71d373f77e07 | -20.50758 | -46.30726 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7ab0a559-d6c8-385a-bf69-511c6bb10ed4 | -20.50667 | -46.3113 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c2fc47e9-131b-3909-b429-34ad765f60c8 | -20.50183 | -46.30598 | 2024-10-02 03:32:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b236e930-afb0-3155-a8c8-a08c2faee46a | -20.41121 | -42.9073 | 2024-10-02 03:32:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1809a943-1697-3c3a-b6ec-68c5f0a3eb3e | -20.41021 | -42.91229 | 2024-10-02 03:32:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ac6c1218-f7bd-380b-a9b8-1abc9e895a77 | -20.35713 | -41.66726 | 2024-10-02 03:32:00 | NPP-375D | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 22b375e6-d960-3aed-b538-981751bb0362 | -20.35665 | -41.66443 | 2024-10-02 03:32:00 | NPP-375D | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aff2bdf4-d32d-3c90-b6d7-427d553efd52 | -20.35526 | -42.76332 | 2024-10-02 03:32:00 | NPP-375D | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b594ce25-4b45-31cb-b617-9084b1714d8d | -20.35395 | -42.75938 | 2024-10-02 03:32:00 | NPP-375D | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 4a30e4a4-0fd8-34c0-93c6-31a32af956bf | -20.35289 | -42.76455 | 2024-10-02 03:32:00 | NPP-375D | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a111fbed-61ab-333e-8103-47430eae99e9 | -20.35167 | -42.75708 | 2024-10-02 03:32:00 | NPP-375D | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b6b48373-5c8f-3e56-89b8-a0bf2fd3f13c | -20.35063 | -42.76231 | 2024-10-02 03:32:00 | NPP-375D | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 13d24ab7-e03a-3a84-8fc8-7771ccbfd72c | -20.33527 | -42.14753 | 2024-10-02 03:32:00 | NPP-375D | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 846163c5-03f6-35d6-9b1b-41766bccde28 | -20.32994 | -42.15104 | 2024-10-02 03:32:00 | NPP-375D | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0321795e-64c2-39ac-9ff1-23c296de12e9 | -20.29486 | -44.03519 | 2024-10-02 03:32:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1350dc7c-70d6-36ed-a955-fac62da59313 | -20.29416 | -44.03855 | 2024-10-02 03:32:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| af4010a4-f563-33a9-9d4e-a92c4b3f780f | -20.23236 | -44.23376 | 2024-10-02 03:32:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 921f92ce-36a8-394c-9bf5-8ba3f5169a97 | -20.23168 | -44.23697 | 2024-10-02 03:32:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7b59f853-a03b-3832-a07f-21da692fd2b9 | -16.68716 | -47.8289 | 2024-10-02 03:32:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cde0f783-a56d-34a1-9565-8b715337e418 | -20.22662 | -44.23573 | 2024-10-02 03:32:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f0c50cf3-c769-382e-9f2b-7ba1a38f4cde | -20.0177 | -44.53155 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a85e5804-b2c9-3fb5-837e-036cde496918 | -20.0146 | -44.52057 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c8bd963d-6e5f-379d-99a6-0f34c6cf9d7c | -20.01393 | -44.52372 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bf677d98-b997-3b12-8fe9-ca84705601a9 | -20.00952 | -44.5189 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8eba0a4b-a1e3-3811-afd4-0fd0732706bb | -20.00884 | -44.52205 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b07843d7-1600-3a2a-a76d-c385e81ad0d7 | -20.0037 | -44.52057 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 342b1ac7-5790-32f7-9d33-1bb08fc7fa55 | -20.00299 | -44.5239 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4ddaab68-1fbb-30fd-a831-519aa5a7b853 | -20.00225 | -44.52734 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3ad1d736-65c0-33f1-b04d-8c8ce08d6c5c | -20.0015 | -44.53078 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 34acd6ae-5e95-3060-a2b5-d91309b21820 | -19.99781 | -44.5232 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 34074235-f87a-3810-a8c7-4da5928d1a0d | -19.99769 | -44.52319 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7312a491-40f0-3595-a44d-f032d1a4460a | -19.99708 | -44.5267 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ccfbbad8-3b80-3196-a43d-ec964860f90d | -19.99694 | -44.52668 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec90694c-5860-3f0a-a074-5037b6e1a878 | -19.99637 | -44.53013 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f90c4ffa-c4cf-3ea3-8058-4725be2e4431 | -19.9962 | -44.53011 | 2024-10-02 03:32:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| afc57041-27e7-3408-bae4-ef64b99364b3 | -19.98933 | -43.53975 | 2024-10-02 03:32:00 | NPP-375D | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b7a62720-87c4-3d54-9baf-faad7c4c3d0b | -19.90962 | -43.16689 | 2024-10-02 03:32:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1d094961-7835-37bb-b0f6-c534376b4ba3 | -19.89655 | -43.15741 | 2024-10-02 03:32:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 99295908-2cc7-304d-b7a7-2dd72d0e97e0 | -19.89178 | -43.15628 | 2024-10-02 03:32:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dd3db051-ec7e-3fe0-8f0c-5e835168a5b4 | -19.88232 | -43.1537 | 2024-10-02 03:32:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bb7b1978-4568-3a09-83f9-98dd9cea42bc | -19.88125 | -43.15889 | 2024-10-02 03:32:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 642d0458-1815-3a52-9a17-4e3f36cef46d | -19.87148 | -42.34443 | 2024-10-02 03:32:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b90d253c-3210-34b9-9aec-0ceb654a2e8c | -19.87056 | -42.34912 | 2024-10-02 03:32:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 581ba844-be90-3efb-932c-e36d248c5a5a | -19.76384 | -42.00673 | 2024-10-02 03:32:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 81945c4f-d4b2-3455-8734-e04db4451f9a | -19.73993 | -41.64902 | 2024-10-02 03:32:00 | NPP-375D | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0492a2e9-bd20-3fe9-a729-e33059619c13 | -19.73647 | -41.64352 | 2024-10-02 03:32:00 | NPP-375D | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cf2c2780-7c67-3251-a6dd-882952281da0 | -19.7356 | -41.64797 | 2024-10-02 03:32:00 | NPP-375D | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 976edce6-13b1-3ee2-8039-21d6b9bb3397 | -16.68556 | -47.8278 | 2024-10-02 03:32:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01d01397-10c6-37d4-b422-09bb6132e0f2 | -19.71736 | -40.35373 | 2024-10-02 03:32:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0fe2e993-9270-352c-b072-7968b3dedcdf | -19.67593 | -42.93081 | 2024-10-02 03:32:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b5998c9f-3000-3b63-b6cf-e315d9658263 | -19.67113 | -42.9301 | 2024-10-02 03:32:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ab5310f9-c2aa-3489-aaf7-ad3630dd7681 | -19.62324 | -44.10831 | 2024-10-02 03:32:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a2a5b64-d26a-30d0-9ec9-014d0da161c0 | -19.61817 | -44.107 | 2024-10-02 03:32:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0aa9594-1cd9-3b77-ba21-551604616104 | -19.61308 | -44.10575 | 2024-10-02 03:32:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff1e0c09-df46-350f-ad38-1944cb7f066e | -19.61244 | -44.10884 | 2024-10-02 03:32:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54b1f8c7-ac6f-37c3-b4e3-29d4138e82db | -19.54997 | -40.22347 | 2024-10-02 03:32:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a4dbf698-9c0c-30fc-a2a4-5c4b8009891b | -19.51419 | -42.87624 | 2024-10-02 03:32:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 7c8cf2ad-1574-3c03-897d-950192d8e4fd | -19.50952 | -42.87492 | 2024-10-02 03:32:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 3a67fc30-554b-30cd-ab02-d160cdc0ae26 | -19.50453 | -42.33435 | 2024-10-02 03:32:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0c58b5c7-55f8-340f-849c-7ee66720d34e | -19.50014 | -42.33245 | 2024-10-02 03:32:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 75a231a8-51cd-3167-a3e6-7adf1ec4d8ea | -19.4978 | -42.34417 | 2024-10-02 03:32:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a6b3bd9b-e4e6-316d-b5c9-f31f123a4733 | -19.49677 | -42.3493 | 2024-10-02 03:32:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 126a4521-dc18-3581-a114-4ee8b547ae14 | -19.47636 | -46.88759 | 2024-10-02 03:32:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62547205-a08c-3ecf-a35c-7b19ab4aeaa3 | -19.4762 | -46.88946 | 2024-10-02 03:32:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dfb4d5e-8077-3b25-bdca-24b03757d190 | -19.47528 | -46.89245 | 2024-10-02 03:32:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abdbc527-f4ee-31a4-ae29-419a722ff7d1 | -19.47144 | -46.88241 | 2024-10-02 03:32:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31c08196-871f-3677-9a3e-247fae487dfd | -19.47044 | -46.88556 | 2024-10-02 03:32:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd5a5099-93dc-3f18-97c6-83a39877931c | -19.44219 | -43.05842 | 2024-10-02 03:32:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2876d322-a27d-30e1-b30f-69cf434903bb | -19.441 | -43.06419 | 2024-10-02 03:32:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1dfc11cd-c593-35db-a86a-6aeda58fa308 | -19.43451 | -41.35861 | 2024-10-02 03:32:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1c9122ec-8eca-3108-8a43-6b16b7ad3d30 | -19.43376 | -41.36244 | 2024-10-02 03:32:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bf874e63-8896-3c74-92fb-1c27b8baf5d0 | -19.42956 | -41.36098 | 2024-10-02 03:32:00 | NPP-375D | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 03cad3e6-6330-3306-878b-1bd38ebd6034 | -19.39605 | -46.39943 | 2024-10-02 03:32:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14e5abe2-f9c3-30ec-87e2-d1e1fbd041c5 | -19.38916 | -46.4025 | 2024-10-02 03:32:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cab4560e-1488-3e16-9278-341b994bd636 | -19.2967 | -44.4244 | 2024-10-02 03:32:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f58a6b35-f9f8-39b4-a4e4-9973d72a2ad4 | -19.29143 | -44.42338 | 2024-10-02 03:32:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a9761173-ba97-3d2d-9932-bd6c5f8fc775 | -19.26025 | -43.76392 | 2024-10-02 03:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91cfdb6e-be4b-3291-bd47-951a2c4724f7 | -19.25961 | -43.76706 | 2024-10-02 03:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aeef3c37-2d6a-3a51-a7c1-3bd0ee6855d4 | -19.25021 | -43.33197 | 2024-10-02 03:32:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ce03fe8d-1537-30ce-8cb8-932b72cd7d44 | -19.25 | -43.36182 | 2024-10-02 03:32:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 629d895b-36f4-3e33-b8a5-8f2541cf3cf0 | -19.24889 | -43.36713 | 2024-10-02 03:32:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e10195d6-dff0-3889-bdb8-7dda5c248034 | -19.2484 | -43.3663 | 2024-10-02 03:32:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef1d9d91-bcda-3b60-84e0-2f3223edfd85 | -19.24777 | -43.37249 | 2024-10-02 03:32:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97f8791b-1b0e-333e-98d4-aa859823f18f | -19.24732 | -43.37164 | 2024-10-02 03:32:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e9c45f4b-c63d-3ea6-b69c-4524e2bde2b0 | -19.246 | -43.33197 | 2024-10-02 03:32:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3784c45f-96be-38b7-b7af-6c3c406e8d97 | -19.24529 | -43.33102 | 2024-10-02 03:32:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1e47795-ba10-39af-9054-c74714ab6497 | -19.24515 | -40.62804 | 2024-10-02 03:32:00 | NPP-375D | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5068f421-eaec-3f9e-a316-111aa4ae5a71 | -19.23969 | -46.86449 | 2024-10-02 03:32:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| feb318cf-6900-3609-a13e-01eb5727c198 | -19.23907 | -46.86664 | 2024-10-02 03:32:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README54.md)
