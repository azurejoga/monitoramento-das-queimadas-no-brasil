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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d608e1f5-f254-3a5a-bfdb-89926079af51 | -13.51026 | -47.0333 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3244fba-e137-3990-9e4a-ded02dedb7aa | -12.92614 | -57.00539 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c1d8119e-0ad3-3fc5-9397-cdf65805a272 | -15.5993 | -52.68246 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29aeaa89-d68d-3d2e-87fd-8c677aa5eb9d | -15.12403 | -48.15698 | 2025-09-03 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54199abd-e6e5-31b1-8f21-c57a54d3931c | -14.74216 | -46.97146 | 2025-09-03 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e1cb611-3983-3811-b83e-d0f1b4e816ee | -15.55125 | -48.36073 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c98da0bb-858c-328c-83c9-e0e03a031eea | -13.52867 | -47.02374 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3500fe7f-af8d-3ec8-aa4d-93c7f4f0581b | -15.55317 | -48.37712 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1aec3c55-7a64-31b4-9de6-d9f0601cdaa9 | -13.28251 | -46.83032 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 19d04642-3b46-327c-bdec-9c349ec3c346 | -16.37808 | -45.24395 | 2025-09-03 04:49:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fe482b7-3fa6-3823-b618-ace3aa0200e8 | -12.88086 | -48.02781 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1c5c693-d181-364f-af4e-e236404b0db6 | -13.58534 | -46.92187 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53ce3c10-b772-3926-9c51-2edfaeb3141d | -12.94482 | -56.98872 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8c77f768-67c4-3023-aceb-39039b13d0f5 | -14.34104 | -52.79525 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3ea1804-ceb5-336d-bac2-cf1d79d60993 | -16.30382 | -52.96335 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f700d3ec-52c5-3ec7-a2ba-3490d1e962a9 | -14.57887 | -48.04499 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 297e2854-fa89-32ff-b780-7a07d8d5e814 | -15.55396 | -48.38051 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eda76480-68cd-30fe-993d-325e8fbb2b61 | -14.59773 | -54.5836 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e99aedc-ab85-32b4-9d5a-b3089a8fbdb5 | -12.63635 | -56.99569 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d815cb8a-ac6a-388a-a1fc-d846d578bcf4 | -14.84546 | -60.04824 | 2025-09-03 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fde86900-bc11-35e3-94ba-d32b0ad164c1 | -14.77825 | -47.51606 | 2025-09-03 04:49:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a727d1b-f62a-3a7e-ace4-e13b58222b76 | -11.87264 | -52.42181 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afae1145-a3cf-381a-92d0-cf468b860bab | -14.30008 | -53.10093 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7faca260-ae61-3e6b-bead-54a477d7a376 | -15.59875 | -52.68606 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fc3e515-4cd8-35cb-af49-11e5aaa3f9b9 | -12.89265 | -56.95636 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cec15a3-9827-3f53-9237-541ecc237588 | -13.81719 | -56.60393 | 2025-09-03 04:49:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cf75106-659e-341b-a43b-e5cb1cb24f46 | -15.14216 | -52.33929 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86aa7293-3830-39ec-9169-fbb5180a4d87 | -11.86934 | -52.42128 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b6cc4e0-1bb2-36dd-9351-7f455d1f1b77 | -14.82769 | -48.36533 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cab16c89-2b96-3a1a-bdc0-f41264bc6168 | -14.57007 | -53.02909 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e299b9cc-7663-318b-8fb8-9ee24d23edf3 | -12.8685 | -48.03065 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f0a318c1-2a29-3172-a27f-d9265814676b | -11.85093 | -51.53055 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d717af9f-6467-34cf-b279-e4c656dba4ff | -12.92424 | -57.00163 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9f50ac2e-42ef-3399-8716-3be21f312351 | -13.70377 | -46.93853 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2df5690-3e69-3e27-a6aa-da1f7ea777da | -17.19068 | -46.0595 | 2025-09-03 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 600bfb46-a561-32ca-a24a-0984a229113e | -14.5686 | -48.06087 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bf4da97-fbfa-326f-89f3-917731ec22aa | -13.31592 | -51.77215 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8046039a-e2df-3ee6-a5c9-eb4e344e400c | -12.62784 | -56.99917 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e813d81c-ee0a-3ad6-9a97-d74c41f642a5 | -18.06979 | -45.98883 | 2025-09-03 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7066b87b-b3b7-3e24-a6b5-d1a5a876dce3 | -17.19005 | -46.06483 | 2025-09-03 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3306b8a-da09-3ccf-aec9-fd6887c463e9 | -11.42318 | -55.18181 | 2025-09-03 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 464aeef4-4ecd-3416-aadc-696daadbb1ea | -18.13495 | -48.57323 | 2025-09-03 04:49:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0e945cd-cbaa-3ae2-b9b9-1cc5ca02bcdf | -16.29498 | -52.95452 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34bd2e8b-3dad-35d3-8eaf-aa9ca3ffc9ff | -13.31983 | -51.79122 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96e5b8aa-27e5-3e6f-81a3-221e05b30231 | -13.49872 | -46.92416 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5537d0d0-5caa-32b8-bc48-79c539cc039d | -15.58225 | -54.32518 | 2025-09-03 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0ce25d1-3afa-3ddd-802a-0612b050a4ce | -14.7767 | -48.14945 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a687f479-60c8-3de8-89a6-5fa63d817ccc | -13.18441 | -50.57689 | 2025-09-03 04:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af252221-659c-35ec-a34f-a5c2f80bc3b8 | -12.91582 | -56.93563 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 057580e8-29df-391c-b3dc-212a4d540f90 | -14.6106 | -48.02144 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c82703c0-b017-32e6-9ef1-a1abd4248089 | -15.02814 | -50.06033 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e553bca-1e3c-375a-b0f7-023fc28fde21 | -14.25692 | -51.23128 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9a01181-71ae-307e-9110-a40a594ec3d1 | -15.89943 | -48.16075 | 2025-09-03 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e9ae0e4-49b2-39ba-bfcc-e9e8226bc77d | -12.02456 | -50.60176 | 2025-09-03 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64da469f-84ca-3388-9f76-cfffca4a4fe2 | -15.55701 | -48.40971 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 431af198-8bd5-370d-ad62-f968982ea468 | -15.56892 | -48.41118 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8ad775e7-c413-38a9-8009-225d1876d3c6 | -14.91071 | -49.61926 | 2025-09-03 04:49:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfe596a4-dcb2-3886-ba66-ccee5db19991 | -12.85358 | -48.0232 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35b8583e-7a18-3443-a619-89d7996f0215 | -12.5158 | -49.56822 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cd4b85b-637d-3311-938f-0e02b44c8230 | -12.9427 | -56.97839 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29b02707-d32e-32fc-b15a-26cadae7ba3f | -13.50348 | -46.81983 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81a4c446-0e60-332c-91fa-8068d8065029 | -15.16823 | -52.34716 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6c3c431-76da-375b-b4af-54ebf1490d2b | -12.63252 | -56.995 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a96c9fca-b77a-3642-ab20-832f35f53443 | -12.93847 | -56.95774 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 01d45874-4e22-3d1e-8e85-812123413a5d | -13.21361 | -51.81881 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 780f907d-df08-3bf6-bc28-a0f2389fbfc8 | -15.74914 | -53.6848 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5fff722e-bbdf-3e3a-bcec-1f6af0e75eb8 | -15.28337 | -52.77057 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21429b3a-73b4-31ed-933c-400ba91fcc17 | -16.3945 | -50.40833 | 2025-09-03 04:49:00 | NOAA-21 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0003cd22-59b5-3325-a99d-830758c84017 | -15.89894 | -48.16437 | 2025-09-03 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cdb942db-10af-3844-b9a5-a238a8dd869e | -14.58175 | -54.55423 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c07e792-d472-3bae-bcde-2297ded78c9f | -17.93775 | -47.21499 | 2025-09-03 04:49:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9af83af0-85eb-3fe5-8e50-7b8a6cbe6e85 | -12.18364 | -53.89004 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b971747-56b1-3531-95b4-f57fbf6c993f | -12.99639 | -48.09325 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4f3098a-25db-37fe-9362-c28e88816d85 | -12.98293 | -54.76422 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b039edc-f83a-3beb-bb5c-4e2e319fe74e | -13.50656 | -50.81191 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7eda00c0-582c-3eaa-bc7e-833bab8abe86 | -16.54843 | -55.08278 | 2025-09-03 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d49c07c1-caf0-3dc2-b926-8276b9ad1e33 | -13.71877 | -46.9213 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 28633cc4-1b09-317a-af28-cc6b0f0799af | -11.84408 | -51.41971 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| afdddc85-637e-3617-b107-284f676989c6 | -13.30895 | -46.82669 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 401c1b42-c392-35ce-b848-40fab1466cf0 | -11.31455 | -55.22316 | 2025-09-03 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9918868b-3741-381b-ab2a-d9a85a467347 | -13.00401 | -48.09175 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b73dbcd7-1b60-3eae-a7d7-605963f2f19e | -12.84428 | -48.06166 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 741d446b-5827-3706-8fae-4cc631ed4669 | -13.44778 | -58.07449 | 2025-09-03 04:49:00 | NOAA-21 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 886813d0-bf91-3c7c-9efd-6f39ece84e1c | -14.57899 | -54.54995 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab077280-cabf-3da1-8c90-e426c983cda7 | -12.94736 | -56.97422 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a640ca2e-206e-31bd-830c-e6b00c73371d | -11.85442 | -51.52727 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a02367d2-5a83-3811-bbfe-f8df519dacc1 | -12.93369 | -48.08239 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 541a901e-5ac8-3cf7-bba8-9e14dbbc7e10 | -11.66357 | -57.34946 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a4f7498-3e16-37d5-aa0a-bb729b267a44 | -12.62484 | -56.99367 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3096819d-d0c2-3657-8b30-2d5c6420f3e2 | -13.28819 | -51.79721 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 493d191f-36fd-3087-9b77-7464e4d13b88 | -12.99618 | -48.09083 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 238eeda8-aaab-366b-b4f6-6b77d9462f8f | -15.15548 | -52.36372 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d743c8f-d00c-345b-9764-235db1ef8678 | -13.00653 | -48.10207 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc96b328-4a7c-3f52-b09f-801a47f5f05c | -16.30713 | -52.96391 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 072fdfd5-2f25-328c-9b7e-4c58030f1d03 | -13.28583 | -46.83802 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 400a0eab-271f-3f4e-8e69-245feba11828 | -14.40576 | -51.66397 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ee05d71-77c6-358b-bde2-5f24de47b726 | -15.70695 | -47.66901 | 2025-09-03 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3a92952-a28d-33da-b6ea-c4aceb7030a0 | -14.80518 | -48.20842 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 363df566-2997-3708-8e81-e3a65d9f3fd3 | -13.29898 | -46.83677 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3ac36cb-a7b9-3c42-9a2b-9fe81d2a1b8e | -17.25207 | -44.8624 | 2025-09-03 04:49:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README75.md)
