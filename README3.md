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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93ab89c4-6314-337d-a1c6-cd4f37c66f80 | -22.70658 | -54.62711 | 2025-03-22 04:44:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| de78de37-a7c1-3a1c-8999-5b7d1fc13dff | -21.2376 | -56.46582 | 2025-03-22 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74519bcb-7261-367a-a365-81ae5f08b6b8 | -25.19249 | -49.32818 | 2025-03-22 04:44:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2a15b981-d6b5-39f8-931f-8c775c3e4c4a | -21.1791 | -53.08184 | 2025-03-22 04:44:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef3cef5a-8c86-3491-b3be-be1a8ac41077 | -20.996 | -51.79361 | 2025-03-22 04:44:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 73e5e3b4-433c-38a8-9884-8bfaa0731d44 | -20.78073 | -49.84602 | 2025-03-22 04:44:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 10c0670f-d584-3a7b-963b-a3f128804558 | -21.15935 | -53.20734 | 2025-03-22 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7b0fec3-c5cd-3e95-a1f0-fb7bcbf1a7ea | -22.54136 | -48.81344 | 2025-03-22 04:44:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b47ddb3-f75d-33ad-95b6-5b0b9c0745fb | -23.51149 | -54.74976 | 2025-03-22 04:44:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 43372690-e117-3b83-ad07-a4e5a464f9e1 | -20.9083 | -56.54015 | 2025-03-22 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea80d4e3-2d76-3289-97a8-6f25fd476ef0 | -23.27172 | -51.20826 | 2025-03-22 04:44:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| aac231fc-0939-3d93-abf2-14b8bc773414 | -21.18241 | -53.08243 | 2025-03-22 04:44:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 316fb796-a311-3c9c-adc6-0958df00533b | -22.61869 | -54.98177 | 2025-03-22 04:44:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ba292120-b992-3ed7-80bc-b0b06dd9158f | -26.54901 | -53.14957 | 2025-03-22 04:44:00 | NOAA-21 | SANTA TEREZINHA DO PROGRESSO | SANTA CATARINA | Brasil | 4215687 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a5c65c17-1c88-3f3e-9e98-4eb17010a7a1 | -22.68791 | -54.63543 | 2025-03-22 04:44:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e55521d2-4d97-36cc-a9f1-72c6f771c035 | -20.78013 | -49.85031 | 2025-03-22 04:44:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 93d7ae6c-42de-3825-9f73-43b183f78f26 | -26.52733 | -52.91144 | 2025-03-22 04:44:00 | NOAA-21 | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| aba1a732-b14c-3227-8a18-a26507b1de90 | -20.47863 | -53.67623 | 2025-03-22 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7cacaef-0a9c-3e9e-a940-262975b7d919 | -21.89415 | -53.46349 | 2025-03-22 04:44:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 57c27b44-8fbe-3051-a740-6760d3cb97c7 | -21.95077 | -47.42125 | 2025-03-22 04:44:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f8b90a8b-55c4-331f-9101-6167e4caae67 | -20.55633 | -55.34129 | 2025-03-22 04:44:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9bc3336-e184-3688-a110-8466b67b03d3 | -20.35232 | -55.82783 | 2025-03-22 04:44:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 68950e30-d214-327e-972b-41afa951bf68 | -22.68727 | -54.63927 | 2025-03-22 04:44:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fc144e67-7c99-392c-aceb-e1a512b7a4c8 | -22.73006 | -55.57694 | 2025-03-22 04:44:00 | NOAA-21 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 27543049-429d-3e7c-ba7e-599dedd9c0b3 | -21.14234 | -53.63425 | 2025-03-22 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc260043-533c-3ad2-8f64-78b5edd2a1a2 | -23.94352 | -53.42653 | 2025-03-22 04:44:00 | NOAA-21 | PEROBAL | PARANÁ | Brasil | 4118857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 42bdb686-59fb-39b7-b060-4e452fff584b | -21.9599 | -57.58646 | 2025-03-22 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cb9d33d-5789-3362-abdb-7b0dc58bfbe8 | -21.15877 | -53.21103 | 2025-03-22 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 885a3e59-4242-34fd-8f0a-5443f0256b4b | -21.95051 | -50.5148 | 2025-03-22 04:44:00 | NOAA-21 | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 97c56b9e-0622-30c8-a1b3-3e1623eafe3b | -25.19055 | -49.32677 | 2025-03-22 04:44:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f0507542-7c74-33a7-8711-af5232cd20df | -23.51484 | -54.7504 | 2025-03-22 04:44:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c5f75317-b2ed-3a7d-bdd0-ee9b20449273 | -24.24282 | -50.74084 | 2025-03-22 04:44:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 717af8ee-4395-3222-8b0c-acd268732a20 | -22.68854 | -54.63158 | 2025-03-22 04:44:00 | NOAA-21 | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 798115b7-e813-3ab9-8c57-b3c5fab0dee9 | -21.24202 | -56.46203 | 2025-03-22 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bc56bc2-5d7e-3e83-8fa5-c7fb97e6e333 | -29.08244 | -49.60717 | 2025-03-22 04:46:00 | NOAA-21 | SOMBRIO | SANTA CATARINA | Brasil | 4217709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 12e21d70-e948-3ab9-b063-a3f453710af8 | -28.86748 | -50.87432 | 2025-03-22 04:46:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3da4c0f5-51c3-39bc-b22e-0f72ace2424d | -28.81695 | -50.70246 | 2025-03-22 04:46:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4d0c5901-8b5f-3f6e-a743-5cc03ee0b506 | -28.62592 | -50.16153 | 2025-03-22 04:46:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3af5ef49-696f-3d48-bd6d-6bb0a6174947 | -28.8681 | -50.86951 | 2025-03-22 04:46:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4acc5fc1-4470-31ae-a571-cba6e315f0ed | -28.93708 | -51.40419 | 2025-03-22 04:46:00 | NOAA-21 | NOVA ROMA DO SUL | RIO GRANDE DO SUL | Brasil | 4313359 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1c0a1afd-f9ee-3097-8a29-fddb75f93db6 | -28.93768 | -51.39951 | 2025-03-22 04:46:00 | NOAA-21 | NOVA ROMA DO SUL | RIO GRANDE DO SUL | Brasil | 4313359 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 679111ac-b61c-3fc6-bc4a-8e64319863e7 | -29.51988 | -50.67804 | 2025-03-22 04:46:00 | NOAA-21 | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7a76633d-3a8a-3db8-8cba-2eabebc0ea02 | -28.86981 | -50.87197 | 2025-03-22 04:46:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 66170762-cc1d-3887-905d-ad606252be26 | 2.8612 | -60.18031 | 2025-03-22 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd62b339-9c8a-34c9-97b5-63ff31491cf7 | 2.53199 | -61.6296 | 2025-03-22 05:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0144b361-17ea-39b2-b2c6-d3fecb814ffb | 2.51904 | -60.99248 | 2025-03-22 05:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc2985df-8bbf-36d0-92ef-c30f45799086 | 2.46188 | -61.31364 | 2025-03-22 05:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7216c8d4-be4c-3e9f-b402-8330111378f7 | 2.53283 | -61.63524 | 2025-03-22 05:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16c1ed76-2bc7-3898-a9a5-abbea3bb0ae6 | 2.53863 | -61.64012 | 2025-03-22 05:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3819e8b4-ddd3-3453-979d-46317f42d287 | 2.52703 | -61.63034 | 2025-03-22 05:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a05b3be-54ef-326c-b948-d8f2ced5e06e | 2.51959 | -60.99045 | 2025-03-22 05:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff0ab936-506d-31d4-ac59-1454e35f2d68 | -5.1224 | -56.1148 | 2025-03-22 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d00301ce-3973-30a2-8701-7fbf86e37903 | -5.12185 | -56.11829 | 2025-03-22 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70c36d26-b43c-3126-8080-2e08e87edbff | -12.93969 | -55.9421 | 2025-03-22 05:06:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef5176c5-115e-3836-b359-8b06f6659e58 | -12.56071 | -57.76025 | 2025-03-22 05:06:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7827d340-d987-3742-bbb6-aaa43fdcd391 | -15.59833 | -57.33188 | 2025-03-22 05:06:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9da15418-e27b-3fcc-91e0-fad511f6811c | -12.94306 | -55.94264 | 2025-03-22 05:06:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7598680-11ed-3e2f-a423-65e442674880 | -12.9425 | -55.94628 | 2025-03-22 05:06:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49500484-685c-392b-8dba-3455b1954099 | -15.59777 | -57.33548 | 2025-03-22 05:06:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c9645ed-cd38-39cb-b330-88c90f2167b7 | -16.30614 | -53.83984 | 2025-03-22 05:06:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b28ae453-6566-3023-b5ea-ffc6ba26937e | -9.92502 | -59.93959 | 2025-03-22 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 72d054df-d634-3554-9cf6-6307c3a68799 | -15.595 | -57.33133 | 2025-03-22 05:06:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d07f8ca6-ba0c-347c-863b-c9e0fe4bea13 | -12.93577 | -55.94521 | 2025-03-22 05:06:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55703a2a-4272-3852-95a4-804e1c010a91 | -12.93914 | -55.94574 | 2025-03-22 05:06:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ef61cfa-99f1-3f4d-aa23-a7a16e68e491 | -13.93842 | -50.57876 | 2025-03-22 05:06:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08b02bf4-a73e-332f-8b44-2221a1c88103 | -12.55738 | -57.7597 | 2025-03-22 05:06:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3794fa3a-f39e-36a3-b344-9a4fadd4c5f3 | -10.11352 | -54.99545 | 2025-03-22 05:06:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67c4ecd3-f25f-3a5d-8487-e3708c5a0df1 | -22.61582 | -54.98153 | 2025-03-22 05:08:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aba37252-289e-3466-b4ad-526808aa37c7 | -20.14337 | -50.72117 | 2025-03-22 05:08:00 | NPP-375D | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bdae453c-a2a3-35ca-a2e7-480c626b2e80 | -20.13847 | -50.7206 | 2025-03-22 05:08:00 | NPP-375D | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 63580970-0d92-3c08-aa80-dfe6f7967eb2 | -21.23634 | -56.46199 | 2025-03-22 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f926819-ef5d-3211-8481-5d5e7c540879 | -20.22535 | -46.67427 | 2025-03-22 05:08:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a12334bd-e7c7-366f-978e-c7ce0a857b5e | -19.44053 | -54.78712 | 2025-03-22 05:08:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 80768582-ae77-35eb-82bc-a0babf015e82 | -20.21851 | -46.67962 | 2025-03-22 05:08:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ea42881-63c9-3d5a-86fb-bd655f3a36f3 | -20.90935 | -56.54191 | 2025-03-22 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9a106c2-dc1d-3317-adff-b8cf8bb07a4f | -23.51402 | -54.74905 | 2025-03-22 05:08:00 | NPP-375D | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 94d27622-d609-3918-b564-cb1be9712020 | -23.26892 | -51.20692 | 2025-03-22 05:08:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e2c0141c-cb30-3f9f-8803-8658dd84fbfa | -20.22253 | -46.68238 | 2025-03-22 05:08:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce88d9c3-11ba-34f5-8a91-ccbe3aa11fde | -22.68677 | -54.6391 | 2025-03-22 05:08:00 | NPP-375D | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c8dec836-4e97-3e78-acfb-15f18239880d | -21.94936 | -50.51463 | 2025-03-22 05:08:00 | NPP-375D | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 07581e6b-8b5f-3ed1-82df-56fc82351928 | -21.94708 | -50.51397 | 2025-03-22 05:08:00 | NPP-375D | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0f6d4b22-43c1-3db5-b97b-c0bf30787dd2 | -22.73022 | -55.57751 | 2025-03-22 05:08:00 | NPP-375D | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 24265bb1-4807-3963-9642-9fda46f51870 | -19.4374 | -54.78194 | 2025-03-22 05:08:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 738d691d-00f8-3f47-8540-5a6e904245c8 | -20.78062 | -49.84706 | 2025-03-22 05:08:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f55beaef-f2e2-3041-83d1-9d8b955cc5ed | -20.22299 | -46.67739 | 2025-03-22 05:08:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 590f511f-6008-3e33-b4b1-0a413e691157 | -15.92435 | -58.42118 | 2025-03-22 05:08:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 61901988-305d-3142-ab3c-e4c96d0c9dfc | -15.37352 | -60.09106 | 2025-03-22 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e72c484-f51d-3725-b056-34856596cf54 | -23.27041 | -51.2075 | 2025-03-22 05:08:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 35ce6fa0-bf83-3085-b47c-bd19cfa475e0 | -22.72648 | -55.57692 | 2025-03-22 05:08:00 | NPP-375D | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 30d48bd8-593c-30ce-99c6-9903e6894519 | -16.30509 | -53.84153 | 2025-03-22 05:08:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e02b8528-288c-3677-a857-14061258803d | -20.35215 | -55.82594 | 2025-03-22 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cf4741be-ab49-3d21-9ca5-6428c7193a12 | -22.70456 | -54.62532 | 2025-03-22 05:08:00 | NPP-375D | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 266c5b33-22b7-3ada-8d09-863d2ed527ad | -20.99587 | -51.79423 | 2025-03-22 05:08:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 200a36ed-307a-3ffe-ad24-5bfc0ea74614 | -15.37419 | -60.08711 | 2025-03-22 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e84c6caf-2203-3dd4-b1d9-333d79db36db | -20.78028 | -49.8504 | 2025-03-22 05:08:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d4c29cee-4bd8-35de-ae5c-71ec8698942e | -21.23987 | -56.46256 | 2025-03-22 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15e6bbe1-f903-3569-b359-c8d3d0db7a92 | -21.96892 | -57.59274 | 2025-03-22 05:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2d41478-064e-3c85-a895-1f4d6140e08e | -15.60518 | -59.94123 | 2025-03-22 05:08:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29d9ed6e-111d-350c-9f54-3e84774c0ccf | -18.31237 | -54.58116 | 2025-03-22 05:08:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 292e380f-3cbd-3185-9d71-20bcf1d9ad92 | -21.95926 | -57.58701 | 2025-03-22 05:08:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README4.md)
