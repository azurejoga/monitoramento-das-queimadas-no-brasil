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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd670730-fc94-3f62-acf1-a307c6adb8c0 | -10.75282 | -42.09717 | 2026-07-28 03:55:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3b592002-ae0a-3eb5-9718-befe6c6b432b | -10.38626 | -49.57802 | 2026-07-28 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6bcc6e68-868a-3f3f-a4c7-1b75cdb800f4 | -7.2968 | -45.28419 | 2026-07-28 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21d56e4a-4242-3203-92db-fc6efbedc606 | -11.89031 | -43.82634 | 2026-07-28 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08612a08-4f4c-30c3-b4e2-ce4ead63fcb9 | -5.82556 | -43.49329 | 2026-07-28 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed0a6026-d5e4-3926-a2ac-a22bb5919fb3 | -7.62332 | -38.79776 | 2026-07-28 03:55:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2cd6ad2c-3dec-3f0c-99ae-1ade6cfb531d | -9.92784 | -47.89986 | 2026-07-28 03:55:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97f262af-4c0b-305f-be5f-86938fa29225 | -9.36407 | -44.72524 | 2026-07-28 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53aa839c-416a-3198-8268-a99b54b81eea | -10.38551 | -49.58198 | 2026-07-28 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6844cc44-be86-389e-869a-fb4f51938d6a | -10.94621 | -43.05814 | 2026-07-28 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 75591c5f-8286-317a-a138-21d865984249 | -11.77966 | -47.08994 | 2026-07-28 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0040d017-d9ff-3d5a-af4f-55b76ebc2e7f | -9.77709 | -49.19677 | 2026-07-28 03:55:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f96c0141-1a29-317b-9aed-1585f2a228a2 | -7.00937 | -45.42321 | 2026-07-28 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0652433d-1fd3-311b-99e8-8e989d4041b2 | -15.44168 | -41.37865 | 2026-07-28 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| e28b2b83-5b86-33fa-86e8-1504f9903673 | -15.76772 | -48.39133 | 2026-07-28 03:57:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4439a93d-5c37-366f-b8ca-cc1deb262aaa | -18.37749 | -50.68578 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 46fcf9f9-fd99-304f-909c-acb4e30cffda | -13.29439 | -45.10466 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d1652502-fb39-3b3a-982c-8c9dc5e129f6 | -17.33633 | -43.63403 | 2026-07-28 03:57:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0869b1a4-1dd2-3870-928d-13ddd8451f4d | -18.37895 | -50.67863 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec6f2ce6-4a1e-3e87-825b-49f6f801d691 | -15.44834 | -41.3798 | 2026-07-28 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0c92a6ba-ce7b-30a9-88c5-7696a13547d7 | -13.30579 | -45.11059 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a827bf6-beca-391b-b841-068513275bc6 | -20.7271 | -40.59772 | 2026-07-28 03:57:00 | NOAA-21 | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2647b6c9-8ab9-38a0-8b5c-c793762a3988 | -13.29164 | -45.09676 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 2c21e129-e667-31d0-b905-731840903b5b | -13.30242 | -45.1062 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4548ef02-1070-300b-baf3-d472a411f23a | -18.37712 | -50.66078 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72b32586-6681-3c5a-90e2-46aa2b646bd0 | -15.77247 | -48.39237 | 2026-07-28 03:57:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2fdc60a5-018e-3082-be8a-a05ffb897aa9 | -19.35438 | -40.19728 | 2026-07-28 03:57:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e419e34d-3dbc-34d0-a1c5-217ba7ebfdb2 | -16.45762 | -42.43759 | 2026-07-28 03:57:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9e8a991-58b0-3006-872a-cbe535a8e8a8 | -18.36605 | -50.66133 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebe54c3a-b987-3d8e-aa0d-c51b0472e4ee | -18.37125 | -50.6627 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b95ceee-5a81-306c-9962-361a6acfb6e7 | -12.32467 | -46.73946 | 2026-07-28 03:57:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0127496-2a21-3b05-961d-318addd79f77 | -13.34803 | -54.28555 | 2026-07-28 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| da99f535-d6af-36ec-85a8-6abfa42f0a80 | -20.20681 | -44.40942 | 2026-07-28 03:57:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9c2be573-5da2-3a56-9920-dc4f5dfe34f0 | -18.36745 | -50.67796 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 22a9f73f-9a75-3c6c-9bb7-6264d4acc4ee | -18.58196 | -40.11802 | 2026-07-28 03:57:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 59c626a8-fa10-31f8-ad63-677cfa48dc40 | -19.16862 | -42.99098 | 2026-07-28 03:57:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d1e30904-261b-34d9-9bca-c9b98be2aa9d | -12.83741 | -44.35288 | 2026-07-28 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5be01d5b-ad28-37b4-a21f-2853292f476f | -12.84678 | -44.39045 | 2026-07-28 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4dce88af-05e1-3dfb-be47-ece33be0382b | -18.85894 | -43.45578 | 2026-07-28 03:57:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6dbabb79-d34b-3b52-85bf-381f91ccb4ab | -13.29903 | -45.10187 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 71070589-c4fd-36f2-8b63-08b6ecbe8983 | -18.37372 | -50.67736 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d7aad7c-cf17-3d36-a582-6fb594bb1cc4 | -18.36819 | -50.67448 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a9e4cf13-b048-3c8f-b09e-e205a5d4e6f8 | -18.37644 | -50.6641 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d16ec13f-840c-3186-894f-ec2057e63f06 | -12.32379 | -46.74422 | 2026-07-28 03:57:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6926ebb7-a5c5-3f3c-b0c0-933c8815084a | -13.02232 | -43.62039 | 2026-07-28 03:57:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7271df3b-fb34-3752-b619-fd2197380fea | -18.37103 | -50.66114 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bfba50a-7bd8-3944-aba2-700ea54c2275 | -18.38166 | -50.66537 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d2848d37-1fa5-35d8-9ff4-e20c11cc1ddc | -18.37791 | -50.68039 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4d9d30e-99a9-3685-8b9e-0da177c0d846 | -20.19293 | -41.94636 | 2026-07-28 03:57:00 | NOAA-21 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 45e60955-3190-3d78-a036-c6e950ab4428 | -18.37117 | -50.68629 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ba5d059a-6de3-392b-92e6-c5e53215136e | -12.72703 | -52.06129 | 2026-07-28 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92a0974c-111e-3e4f-998d-5066184bda4e | -13.29714 | -45.11257 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d711c70-2fbb-3450-ba69-3a8442388682 | -13.30516 | -45.11418 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f6978ab8-dea9-33df-ba06-1746b1679973 | -13.29564 | -45.09755 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| f3f14cb6-a89e-38fb-bd57-7978127abd63 | -17.39865 | -47.32721 | 2026-07-28 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdc46154-fab8-3f0d-8d89-102ab1939a8c | -15.81453 | -41.89622 | 2026-07-28 03:57:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3c829008-17ca-3897-8a35-263fed132e5b | -18.37414 | -50.67232 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 922b402d-0774-3882-92f8-708dfa7cd7f4 | -13.29101 | -45.10032 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 4b006745-ef22-362f-a746-3442599a80fe | -19.04033 | -40.40843 | 2026-07-28 03:57:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4098bef2-9ec2-38fa-b1bf-3d851124e7c5 | -17.31182 | -42.6715 | 2026-07-28 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 30a2a231-4d0a-36f3-ae59-f66e34766aa7 | -19.89467 | -41.61599 | 2026-07-28 03:57:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a4474d32-fe43-3aea-9077-1e5a7fa7899e | -12.84978 | -44.39612 | 2026-07-28 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a90e5d10-6f27-3c96-b6b9-c1e5ed8cb08f | -17.35992 | -47.08434 | 2026-07-28 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07c91454-c5d0-3fe2-a3b1-19ec41ed8302 | -18.38143 | -50.66381 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 717e106c-51e3-371a-b215-a63f7c559c97 | -15.4411 | -41.38228 | 2026-07-28 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 50a43d42-22af-384b-bdcf-a9e25f6ded38 | -13.30052 | -45.11697 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f35f588-f868-32a4-bb46-e97a1e3b26d2 | -12.34211 | -48.22676 | 2026-07-28 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6fe377f4-979e-37da-928b-9f9a4bf49e5e | -16.868 | -49.57777 | 2026-07-28 03:57:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5afd7e3-054d-3527-897d-95828626f984 | -18.38074 | -50.66705 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a61f38e-96ee-3e46-b01b-93754d9db1d3 | -16.86738 | -49.58084 | 2026-07-28 03:57:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d045742a-d5b9-3e74-98dd-f4b3fcb17aa3 | -12.34078 | -48.23101 | 2026-07-28 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c38953cd-c5de-3c84-bb2f-4873a70943ca | -17.31458 | -42.67594 | 2026-07-28 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1e003a44-2410-38c2-9715-ffe4e13654cc | -13.29966 | -45.09832 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| da2326e0-8a2e-3e8b-a813-bd6bed4ff706 | -17.31395 | -42.67976 | 2026-07-28 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1c8bbbd-df60-3daf-ba48-a54ebae40a73 | -13.29502 | -45.1011 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| f27ceccc-0b8c-3e83-babc-ada9f3d5035f | -13.30115 | -45.11338 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b67cf423-e299-31e2-a7ce-c1c2e5f0d331 | -18.37568 | -50.69088 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8a4a59b6-5e33-3fb4-a890-cd3fe0159418 | -15.76298 | -48.39026 | 2026-07-28 03:57:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ea5fbd3-f110-3010-9887-92577e7060a0 | -15.44443 | -41.38285 | 2026-07-28 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3070665f-0c1b-3080-bd3b-5126ad6c022f | -13.15593 | -42.31825 | 2026-07-28 03:57:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cdfdc9f3-caa1-350c-80a4-6f47ed40019e | -13.30028 | -45.09475 | 2026-07-28 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| fd0dba7d-837d-379c-8c0f-90dcb0f03655 | -12.34156 | -48.22977 | 2026-07-28 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9364a11a-8237-3f4b-b67c-5ba3fdd8ac31 | -19.16799 | -42.9948 | 2026-07-28 03:57:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 00d9c358-000d-3d12-956e-f8a32f24cdd9 | -18.37269 | -50.67914 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c9e1adf9-2151-3c8b-abbd-e2b0364283ab | -17.40037 | -47.32629 | 2026-07-28 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d75978ef-7ab4-30f7-8bd6-e137f7c64cc2 | -15.24642 | -48.57748 | 2026-07-28 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1a332ed-dc56-388f-81ed-3deef6ae5f50 | -15.44501 | -41.37922 | 2026-07-28 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 8cd9dcb1-4e04-30bc-9eff-320fd2e8e47a | -16.86343 | -49.58047 | 2026-07-28 03:57:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3262ca26-e5f7-3920-9324-a478db415273 | -15.43777 | -41.38171 | 2026-07-28 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fd82cfb3-4c47-37d3-bdbf-9fcb5034654a | -17.33282 | -43.6334 | 2026-07-28 03:57:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6e1ac8d9-e6ef-33d7-b134-1eb20df6c017 | -15.32762 | -43.02217 | 2026-07-28 03:57:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f19eb322-b653-3888-a8ff-1844f90d296e | -18.36849 | -50.67615 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a5ff1bc9-098b-30bf-bc16-bbf2bd00a971 | -15.89223 | -48.13128 | 2026-07-28 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16e07bb4-7b2c-3123-9715-f08393c268a6 | -20.23949 | -40.37893 | 2026-07-28 03:57:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| deade55a-d38f-3711-8bbe-93652bfbde9b | -18.37342 | -50.67569 | 2026-07-28 03:57:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d2e01d19-171f-33ae-b087-b72b9ef94213 | -12.34136 | -48.22801 | 2026-07-28 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80f44ccb-a0ba-35d8-b969-414a1f03443a | -12.46184 | -50.54859 | 2026-07-28 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27e15985-2845-3adc-9f30-78f92430da3e | -17.39784 | -47.3316 | 2026-07-28 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05572683-488b-3bcd-8952-5dd3e724296d | -15.44892 | -41.37617 | 2026-07-28 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ce88316c-b00e-32d6-abbf-2737af3c55f5 | -15.77204 | -48.39532 | 2026-07-28 03:57:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README11.md)
