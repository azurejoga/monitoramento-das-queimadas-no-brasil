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
| e11c8d85-1c1b-3627-810b-1e59f0c5eabb | -16.45552 | -50.04994 | 2025-01-19 04:29:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30d92288-feb9-35ee-9d44-4f33ab8ea449 | -17.8849 | -40.11526 | 2025-01-19 04:29:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 68a569ad-3b8d-32a7-a647-0629a4eebffc | -19.13512 | -40.40701 | 2025-01-19 04:29:00 | NPP-375D | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f5cd542f-a942-308c-aaa9-5e0cf3deee15 | -19.92485 | -44.09127 | 2025-01-19 04:29:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 43f15f0d-fb76-3708-b3da-fe53b7e29486 | -15.07849 | -48.94398 | 2025-01-19 04:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55f9b8de-7eab-3678-993f-f44eb074a89a | 4.5177 | -60.6982 | 2025-01-19 04:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 352967aa-0793-315e-8e72-2f539fc405f1 | -27.38425 | -51.5114 | 2025-01-19 04:31:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 196c9a25-8508-328a-97c3-2e69ade8d6a8 | -22.90294 | -43.75502 | 2025-01-19 04:31:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c1e3f0b8-005b-3d30-ac7e-20e728b61557 | -22.90306 | -43.753 | 2025-01-19 04:31:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cd401213-a809-384d-bb0d-d7fa460422ff | -22.90253 | -43.75751 | 2025-01-19 04:31:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a9646a7f-ae64-37cf-bec4-0037df2ab7d5 | -26.31999 | -52.25991 | 2025-01-19 04:31:00 | NPP-375D | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4593c845-6a02-3e4d-9bd4-e2912f731b44 | -22.67696 | -42.85363 | 2025-01-19 04:31:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9d6b20ad-c2c4-39e8-880a-eb08e0f2932a | -26.32064 | -52.256 | 2025-01-19 04:31:00 | NPP-375D | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7bcd4af0-3a7d-3b8c-a193-7ec2a239e5cc | -30.03924 | -52.66928 | 2025-01-19 04:33:00 | NPP-375D | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| 0dd61790-2a89-3097-8ffa-f2e2325ce552 | -30.03526 | -52.67258 | 2025-01-19 04:33:00 | NPP-375D | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| cb6f5ff7-b97e-3337-b78b-0aba4f57c927 | -29.52906 | -53.30733 | 2025-01-19 04:33:00 | NPP-375D | AGUDO | RIO GRANDE DO SUL | Brasil | 4300109 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 924b4ade-ff31-3ea6-b8f0-a99513c29b97 | -30.44907 | -53.81208 | 2025-01-19 04:33:00 | NPP-375D | SÃO SEPÉ | RIO GRANDE DO SUL | Brasil | 4319604 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| bbc22ed4-546b-3c68-9979-48cd02ab8b03 | 4.12949 | -60.00071 | 2025-01-19 04:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3342551c-5c12-355c-944c-4e41e9630826 | 3.27727 | -59.95184 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60255104-f4a9-3d5f-a953-1e85dd584649 | 3.86911 | -61.24248 | 2025-01-19 04:48:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 748c9b96-27e7-3e8a-963d-b8867551f21c | 3.27625 | -59.94477 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0f58346-996b-3283-af38-1a6488f29907 | 3.11788 | -60.73909 | 2025-01-19 04:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e4114a7-eede-3c95-8954-40d41a57d08c | 3.87188 | -61.24546 | 2025-01-19 04:48:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ff01ad2-3841-338d-b490-481f2e7058c8 | 3.26634 | -59.95356 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41f54200-db0d-3723-b17a-fe3043bfc6e9 | 3.28668 | -59.93962 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6004ea00-9f4f-3f01-9bcd-01f9435dc392 | 4.51759 | -60.69534 | 2025-01-19 04:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c88938ab-440b-3fec-9c82-1debf4900dd5 | 4.12861 | -60.0004 | 2025-01-19 04:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 530a1085-c9d0-3e66-923b-394e89b1ec4b | 4.50912 | -60.71953 | 2025-01-19 04:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd7ff79c-48c0-3111-a8f5-3877f5369cdb | 3.11847 | -60.7431 | 2025-01-19 04:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87edb63d-6ab3-3fe0-9791-e2b3d0281535 | 4.52336 | -60.69392 | 2025-01-19 04:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fca75269-7aa8-307e-8730-123c4b46c8bb | 3.62509 | -60.09908 | 2025-01-19 04:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4097347-b083-33cd-8b10-919b5b0f34e5 | 4.51182 | -60.69674 | 2025-01-19 04:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4e4e7095-bd93-354a-b0f0-7d0acb5b3bda | 3.97886 | -59.62255 | 2025-01-19 04:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd671a0a-bc9f-30e6-894d-561e12dd9572 | 3.11628 | -60.768 | 2025-01-19 04:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d36349b7-eb4c-3593-b399-aa1108873c03 | 2.90495 | -60.58934 | 2025-01-19 04:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29b5fff7-32ef-3ca5-97e2-50c093401a46 | 2.90437 | -60.58551 | 2025-01-19 04:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aab9dc03-5073-3f46-bd1a-35ecffbe9b50 | 3.27676 | -59.94829 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3c7d31c-4b56-3e84-b32d-5fea1ca6dd2f | 4.50682 | -60.70353 | 2025-01-19 04:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 84eaa7e7-585d-3b73-8b46-0b00be1fe5c6 | 4.50277 | -60.717 | 2025-01-19 04:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e347b4ac-82ef-323d-a062-57902c2f85bd | 4.1342 | -59.9998 | 2025-01-19 04:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dac89d27-764b-32dd-95fc-d1ee03eef4f0 | 4.51242 | -60.70087 | 2025-01-19 04:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8901f27b-b8d2-3af8-954a-79035a49ba6f | 3.26609 | -59.95778 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 053bb515-c3bb-3de9-91fb-dee491fcea26 | 3.12144 | -60.76306 | 2025-01-19 04:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e3ec1de-8f37-3e50-aa2b-c0e46ca559e9 | 4.51477 | -60.71719 | 2025-01-19 04:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ec14136-5d38-35e3-a6c6-b73babba086b | 3.28121 | -59.94043 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1514364-86a9-3a5f-9b39-37781f6c0024 | 3.27129 | -59.94917 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33d434ef-55fa-38f4-a762-ef6646897043 | 3.12025 | -60.75507 | 2025-01-19 04:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 42671b73-d8a3-356e-b212-5fd6aef258df | 3.86978 | -61.24699 | 2025-01-19 04:48:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 729bae15-cb5c-37f9-955c-09d1d1394eef | 3.12084 | -60.75907 | 2025-01-19 04:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 23f464a4-628d-399e-b962-b4a9a78222fc | 4.5061 | -60.69853 | 2025-01-19 04:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8f21ddf2-7099-3286-a5f2-87c2348fa9e3 | 3.11907 | -60.74709 | 2025-01-19 04:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2b1796c-4b72-30cf-85a6-d234a4851ad5 | 3.27181 | -59.95269 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c28f979d-2d08-32d8-a4b0-e542f813567e | 3.26556 | -59.95426 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ced89115-4735-3f41-8026-d49923077af0 | 3.27049 | -59.9499 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f08117f-b115-36e8-b3cb-8aec21954ea5 | 3.11687 | -60.77203 | 2025-01-19 04:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eced4fb6-562f-3299-b157-1922e3157a51 | 3.97931 | -59.62563 | 2025-01-19 04:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a307a272-723c-34e9-8f68-1372293c1047 | 3.11966 | -60.75108 | 2025-01-19 04:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a296fb4-cd75-3b4e-970c-55dbc3dfcfdf | 3.27102 | -59.95343 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7de0f84-e1a1-3c34-8078-4e1fda17ada6 | 3.97842 | -59.61946 | 2025-01-19 04:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4580bd7-6a56-3c56-a14a-4346f3677b18 | 4.51821 | -60.69959 | 2025-01-19 04:48:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 238579cb-2ff5-32d3-80f8-3fe68acd4d0b | 3.28172 | -59.94393 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb1a168d-1bf2-3cb6-9764-55a13c4ddc79 | 3.26685 | -59.95709 | 2025-01-19 04:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1569a02-f34a-3605-9eb7-9d52f3007ef6 | -11.0339 | -45.05066 | 2025-01-19 04:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d53bbdf-2c5c-383c-8f32-db32db908274 | -11.02874 | -45.05016 | 2025-01-19 04:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c412e142-1028-3d26-b61d-c16d6df4a705 | -16.45683 | -50.05415 | 2025-01-19 04:53:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e22f48ba-798d-315f-8957-46e7739858dc | -16.4559 | -50.05072 | 2025-01-19 04:53:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02e519a6-7fd0-3cc0-9380-b7b2c0ccdd35 | -15.26566 | -51.47713 | 2025-01-19 04:53:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 100ac663-a501-34c8-8f13-eec17614d62a | -20.3228 | -47.73411 | 2025-01-19 04:55:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a46ba1c-e89f-31f0-a903-c5963e4fcb35 | -20.32767 | -47.73472 | 2025-01-19 04:55:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea7b2456-dd72-31c9-af66-c47b9c17ea91 | -20.65705 | -49.99396 | 2025-01-19 04:55:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c0b2b85-bdf5-3df0-921e-b7f5cf5d165c | -20.65753 | -49.98989 | 2025-01-19 04:55:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d654ccee-83b9-356c-aa5e-85cd839da7de | -30.44937 | -53.81251 | 2025-01-19 04:55:00 | NOAA-20 | SÃO SEPÉ | RIO GRANDE DO SUL | Brasil | 4319604 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| a704693e-1f62-3843-8906-767093fbc517 | -28.23448 | -54.85232 | 2025-01-19 04:55:00 | NOAA-20 | ROLADOR | RIO GRANDE DO SUL | Brasil | 4315958 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 09f610c7-9473-3ba6-91be-1fecc4bae12d | -26.31935 | -52.25698 | 2025-01-19 04:55:00 | NOAA-20 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 52b09cb0-574c-3f84-8d5b-cf66e879e2d7 | -20.65742 | -49.99131 | 2025-01-19 04:55:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6b8acbf-2eea-3c14-9303-04842d86ba96 | 4.50195 | -60.70078 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 306d53ac-ec27-3eae-b99d-f122ec88cd0a | 3.1158 | -60.75376 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 538d55e6-20c1-32a5-bfa2-d2560a81169f | 3.41796 | -60.39345 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 0b0854ee-76c3-3a11-9999-6bf5a541ed55 | 4.13189 | -59.9989 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5f9964f2-1cf4-34b6-a10c-ce289e746a1c | 1.12111 | -59.41114 | 2025-01-19 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 305d1193-ba5c-399f-8e19-b28a485347b8 | 3.11927 | -60.75322 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d8716b0f-6923-35d1-949f-0d1a8c917b22 | 4.5214 | -60.69045 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2b53855-c5be-3343-9c4a-3d16b1ade7a6 | 4.00923 | -59.82423 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68ec339b-2ec9-3a18-9d25-5a4e360be514 | 4.51171 | -60.69584 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5f976476-d140-314f-9a7b-761061e4ceba | 4.0233 | -60.49833 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d339bab-d82d-3b5f-88a5-dc29113884c5 | 4.00858 | -59.8202 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e393d56a-2537-3fd1-bef6-af7c1e4fc109 | 4.50485 | -60.71891 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e466fcc-7165-3ea4-bbbd-7da97aefb62b | 3.74786 | -59.69883 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1bab5b8-4e62-31a8-bf18-fa320903ea2b | 4.12844 | -59.99803 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 812c6543-0a6f-34fb-973e-a6176c6b75da | 3.80008 | -60.0547 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5c8eca8-4de8-368d-a836-bb42ca35d161 | 4.53349 | -60.70024 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a6963a1-7653-3719-8862-efd54b5b69a4 | 3.26431 | -59.9541 | 2025-01-19 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 552860fc-129e-3fa9-a05d-dd8f8ccdff73 | 3.11414 | -60.76581 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c4cbe0f-394f-36ac-a9b0-ef5d4373a5e9 | 3.27376 | -59.9441 | 2025-01-19 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c3e42b87-43ac-335a-99ad-f9765b9eb047 | 4.00495 | -59.82053 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c4cce11-0218-3801-b202-7bf0c3601389 | 4.51453 | -60.69148 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1fabb798-2473-3460-bd38-1e8fc8f96ae6 | 4.1249 | -59.99868 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4261f630-1602-3b64-b3b3-9889574b8654 | 3.42086 | -60.38894 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8cd75397-1c5f-34f3-9611-24027ca0cec4 | 4.53122 | -60.70805 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 58549cf4-a545-3f57-9e34-70572a1df463 | 3.27443 | -59.94825 | 2025-01-19 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README4.md)
