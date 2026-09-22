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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ed88fa6-53e3-33be-b71b-ad6882987780 | -7.87931 | -54.7315 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 450ceded-e5c9-3a9a-87aa-f44e739b1dae | -4.35247 | -55.64853 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d30efabe-f5b5-3c06-8f24-26d645e30c9f | -6.58711 | -44.14669 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f654f52d-de88-3ab6-bbb6-7632723c52d9 | -4.65617 | -42.09737 | 2026-09-22 04:46:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a0eeee39-dda2-3eee-96ec-ece586d680ae | -6.65453 | -50.93429 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 934e90dc-bc27-3ca4-bdc3-d982b61ae948 | -10.21976 | -53.90075 | 2026-09-22 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 443fdb8f-d2fc-31b7-8402-a2f23aa54ddc | -6.33791 | -59.94862 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cab160d1-654f-3eb1-9f3f-63142de09791 | -5.20642 | -56.07839 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1d85f62-7986-312f-adde-9ae4cd901a35 | -6.13829 | -59.8833 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3f71de9-a1bb-34e1-af29-e27969a3373f | -8.59887 | -54.63206 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be7b22e5-49e7-374c-a910-efd0d9ced71a | -7.52277 | -46.21775 | 2026-09-22 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e44773c-6c2a-3110-801e-dead04515f82 | -6.73524 | -55.07726 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 262a435a-c550-3811-acb9-8c4f0f84b264 | -6.13882 | -59.88019 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50526af8-8b4f-3b0a-9334-2ac7f6084522 | -6.649 | -50.92636 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0838452b-2ae2-3def-b979-8a4e42d13010 | -6.81076 | -55.82743 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03f3274f-7684-3c79-b8e6-7d175156c1e0 | -10.6837 | -48.7218 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c892a06-72c1-3303-9deb-5a8689dc10d0 | -7.41364 | -44.73497 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37e7aabc-6bac-344b-8d64-80a52c2167d1 | -9.95293 | -53.98407 | 2026-09-22 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cd64438-5e23-3c61-9bc2-d287fd3a94cb | -6.4671 | -59.98976 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 37d29774-3a6e-3099-bf0a-fb654197ef88 | -3.23987 | -53.95449 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 89a75bd8-0bb4-3f65-a17c-0e1627c879d3 | -7.95345 | -45.65248 | 2026-09-22 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66eb5fd1-d459-38e8-acd3-e6496dc9def2 | -3.5206 | -52.74171 | 2026-09-22 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5c99933-1f93-39b2-8e87-077870d7e57c | -8.24923 | -55.24951 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1385d4cc-60cc-3e5f-b075-53f3ad0710fd | -5.93796 | -59.98317 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4a2f9c6-0806-3938-885a-9704f226b571 | -2.78843 | -54.02986 | 2026-09-22 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27149cc9-5653-3df7-81a8-27f0aa65129c | -6.20296 | -47.51163 | 2026-09-22 04:46:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20cfd9bf-bb41-3f03-8931-6708e6b81dca | -3.0616 | -54.39914 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c8d67fd-6c7f-36ea-8a8a-ad1f088c09cf | -10.48025 | -51.30648 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf76483a-1c69-353d-a98f-923e10a88fc4 | -2.99877 | -54.16823 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4ac2cbb-46aa-352c-b5c7-12966121d301 | -10.24994 | -45.4945 | 2026-09-22 04:46:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4864d39-bdae-3952-aadc-f7317d322189 | -7.05209 | -49.92029 | 2026-09-22 04:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fc8b63a7-8af8-349c-aabd-20847b85c8c2 | -8.24573 | -55.29443 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6ab9757-7474-356f-9f01-d1a7295f77ae | -6.46098 | -59.98463 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cf54abeb-ed9e-3e53-848a-e90219c52ae6 | -5.95187 | -52.22724 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bc2a4e0-8939-37c3-86be-18c126955e0e | -7.57267 | -57.69056 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4070b764-c7b1-3ad3-bb5c-a09e758eac7b | -8.63509 | -54.63382 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 667536e1-d991-3436-ae33-86508a2289e0 | -6.72847 | -55.07183 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cffe227-e921-39a3-ab6f-abbcadf952e7 | -3.05125 | -54.41599 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd1fa330-956e-3544-85ca-bdad9a356870 | -6.35377 | -55.8391 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28b0cde8-d429-3f88-8243-7c3c0f112295 | -8.63221 | -54.62916 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12a96d2b-6567-3d64-88b8-b9828c2c4b24 | -3.05676 | -54.41019 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79dd1229-48c6-3f90-9063-a8f4498bb771 | -5.8089 | -57.74313 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10c5cb80-8ae5-3667-97d8-f0b494ca3a3a | -6.12766 | -55.81843 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4816e546-c5f3-3f13-9e73-32d4a1430001 | -7.87638 | -54.72676 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3763c7f-9eff-3475-a6a1-4cf31e39a9c7 | -9.67811 | -54.3147 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8e261f7-797e-3e56-affe-3293b1b72d1d | -10.45468 | -51.27341 | 2026-09-22 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c4a06ed-7022-3616-b787-018a214c3909 | -4.34391 | -55.65089 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5eab1d04-9720-3f2a-944c-bb9143cfd892 | -8.59955 | -54.62799 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b048fe0-4a37-3f96-b7e5-a00c1c3a4736 | -8.80157 | -44.28519 | 2026-09-22 04:46:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53e08380-5f9f-3cb3-95ed-a32f5e72f9c8 | -6.85051 | -43.72259 | 2026-09-22 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6dd219ae-9c2c-3d1a-b8aa-3c76dfb9f422 | -8.60666 | -54.62913 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65322cbe-2c86-39d7-b695-7812051c3c72 | -9.6225 | -43.946 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 0dff8949-26be-31fc-9271-6b71753e980d | -10.12156 | -45.54622 | 2026-09-22 04:46:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c675a7f6-30c8-3a63-bbd2-e2bdb8c8bb3c | -9.23641 | -46.1732 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5eb555ca-d6b9-34cc-872a-69237144863b | -5.82312 | -57.74083 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d67eb5fe-c065-393a-8ec1-2cb1fcd88550 | -6.46309 | -59.97227 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1e6d3e3-9f02-3c2f-92ea-077878cd174a | -11.15099 | -42.83831 | 2026-09-22 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8a4cb6aa-3e8f-31d4-82db-dba61a195ca0 | -9.88904 | -48.45285 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9380f66c-6b37-3e75-a9b3-3a420b27cbb7 | -3.36871 | -61.28671 | 2026-09-22 04:46:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 15d1f221-fe79-3f8b-ac9d-6272b1ddcf2b | -3.19107 | -60.43302 | 2026-09-22 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfe5f17f-e9f3-3c84-9686-1004e76e5542 | -8.36844 | -45.61702 | 2026-09-22 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b2449df-5ab9-3248-b65b-15d97ceeecee | -10.52121 | -44.8731 | 2026-09-22 04:46:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c609fc0a-c4b8-369c-84dc-43367149a6d7 | -2.41384 | -58.27421 | 2026-09-22 04:46:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea6af22d-8d0e-3fad-a085-9583d9e7c121 | -6.10003 | -57.68298 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1c39de11-37ae-35d8-9b14-cd8495cdfabe | -4.5136 | -54.9815 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1af7718f-7e2a-3fee-8809-7960b5156a94 | -6.82985 | -49.0974 | 2026-09-22 04:46:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 632d879a-ee72-33a8-a0d4-c936e5048dec | -3.62408 | -54.5271 | 2026-09-22 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bb9a9c3-a19e-3690-be41-02651a4110e7 | -11.10428 | -48.31199 | 2026-09-22 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 178a2818-edcf-3d0f-b1dc-cda38b16d56e | -6.18955 | -45.3249 | 2026-09-22 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ad47013c-50e2-31b0-ab0c-e2a356ddbf84 | -6.46875 | -59.97024 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6eee6f55-39ec-3cf0-8772-c00390eacdc9 | -3.69224 | -60.58278 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3254dea9-a675-3d1f-9119-ff0f34419b69 | -10.26003 | -49.98582 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb5ae0eb-677f-3445-81b4-cf5dd553e70d | -7.42436 | -49.84372 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e6d37bf-8837-3fad-aa79-89e9ceb425a1 | -3.90019 | -60.59234 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c429033b-a272-3c46-912c-6290555ed220 | -6.09411 | -55.55599 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5868f0f2-8037-3852-8da6-1029a0321d05 | -6.40989 | -51.24191 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37139f71-683e-3aca-9613-0b3a9b2327e2 | -9.82378 | -48.43993 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0deb61e1-b3f4-3f13-945f-65f98952775a | -5.7583 | -45.08168 | 2026-09-22 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 116995ae-3e78-3873-9ddf-1ce84c38c481 | -9.87328 | -55.73293 | 2026-09-22 04:46:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69c43ae5-6442-3f8e-8f1f-748625d92496 | -7.59066 | -43.42279 | 2026-09-22 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cff19c4e-1b4e-3607-bf79-efb719a34016 | -3.36798 | -61.29099 | 2026-09-22 04:46:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 765ca32a-c0ad-3001-b8e0-4a591e4bdcd4 | -5.89517 | -53.64508 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56757b1a-0126-381e-9e34-c00669708158 | -6.44774 | -48.44642 | 2026-09-22 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 407af175-54fc-340a-9b07-a4660d67f5c6 | -8.316 | -44.74999 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9097bea1-84d0-3f42-9cb0-3f79926ef9c5 | -6.40935 | -51.24536 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1d6466f-e024-3ced-b5a2-276ed5eb7892 | -6.3126 | -60.00251 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d07d9bfc-5cd3-3ac8-a65d-41a33f03df0d | -6.64312 | -59.93495 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2214e9e2-3c9a-3910-85fc-d6ceb27c331f | -10.4784 | -46.27591 | 2026-09-22 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 369babd3-f8ea-3260-9d88-dbe0c2033685 | -3.43499 | -50.664 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da62a10a-7379-3755-a4ee-1a6e2b6bd928 | -7.875 | -54.73526 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48313046-1065-3c5c-ab37-ad786e16e5b1 | -3.43392 | -50.67086 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13fb6f05-54fc-39e1-b6af-e6864ab80e75 | -7.32619 | -55.60052 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc5185d1-09a4-3b4f-ba55-330a6e0ba17a | -3.55258 | -51.53978 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98a4c51c-c728-30ab-8803-5554fb40cc7a | -6.47678 | -42.78262 | 2026-09-22 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0f94312b-b219-318c-a003-627588a19e5f | -5.37284 | -56.05485 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 220fe46a-7c36-32eb-a584-35796c7f3888 | -5.98238 | -55.69725 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56f07ae4-fd50-378a-9460-8af956394e5a | -5.18708 | -49.33764 | 2026-09-22 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73c735e2-b618-36f2-b824-fe33ed8a20af | -7.32877 | -55.60362 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 95012ff6-a176-3797-b118-9efc6a93ff2e | -6.40658 | -51.24139 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecbd8cc9-eb97-39e2-b9c0-493788d9607c | -4.18038 | -51.24646 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README64.md)
