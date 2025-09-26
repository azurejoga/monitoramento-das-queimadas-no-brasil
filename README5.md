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
| 8b08d27e-6f34-36d6-a032-5e238b7b432d | -5.93059 | -42.91974 | 2025-09-26 03:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e736403c-16dc-3076-a603-9a244504d874 | -5.46839 | -43.0748 | 2025-09-26 03:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| f2c27fbc-de40-3df9-961d-059f7520b319 | -4.7503 | -43.27266 | 2025-09-26 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ba299bb-765e-323e-860d-b2cfeb58abb2 | -8.34519 | -41.36169 | 2025-09-26 03:21:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c527e04e-cb85-3b7e-b0bc-93c10bdcb790 | -6.31365 | -41.88614 | 2025-09-26 03:21:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f8c969af-a42b-3d5e-98cc-9d1f05db348e | -6.67333 | -43.59933 | 2025-09-26 03:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b4e9ff4-5eac-3a65-ab92-1a4ee9799301 | -4.7434 | -43.27145 | 2025-09-26 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c314ce6c-05ac-3e87-b59c-844c6c9574ca | -5.74965 | -42.55849 | 2025-09-26 03:21:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5bec55f7-d767-3cdf-b11a-0e74202de0b8 | -6.25106 | -42.48444 | 2025-09-26 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 21ad7cf6-90c5-3c7c-89c5-bd796da8d6d3 | -5.46164 | -43.0736 | 2025-09-26 03:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| fe581908-5774-3ab5-a2f3-397890002ef1 | -3.81396 | -41.56583 | 2025-09-26 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 649841fe-7325-318c-a34c-038646b1577a | -3.80585 | -41.57499 | 2025-09-26 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3cd8783f-ec01-30b3-975f-ca3f1909e159 | -4.74968 | -43.27715 | 2025-09-26 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84d06f22-f0c5-3755-9db8-1f947a79f1b2 | -9.44673 | -40.38007 | 2025-09-26 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ce0a8788-9e49-3c20-b423-aac83f6b07b0 | -6.32077 | -41.8822 | 2025-09-26 03:21:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 79c98276-4400-31d6-a0bf-9325150d2d11 | -6.86639 | -39.26733 | 2025-09-26 03:21:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8cf9656a-a85a-318d-bd66-e1661c3aa53d | -6.88193 | -44.50679 | 2025-09-26 03:21:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ea138d7c-85f2-3943-841b-1fb0e3ff5c48 | -6.96015 | -43.24276 | 2025-09-26 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| bdb3b529-602e-31a5-ad91-ec6b7b5f5346 | -6.25762 | -42.48491 | 2025-09-26 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4b199563-f5bd-32ef-a991-870ddf9f219a | -4.8177 | -42.75111 | 2025-09-26 03:21:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbf1b062-6260-3455-acbf-36e3327d3cad | -4.82436 | -42.75242 | 2025-09-26 03:21:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d49c318-21a7-36a6-ad5d-5d10ea45b805 | -4.80944 | -43.54241 | 2025-09-26 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d3c7de15-12da-3ccb-b97e-e50ac70ac60e | -10.06147 | -36.16389 | 2025-09-26 03:21:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b8c7c2f7-121c-3375-9c1c-4d4aabb93613 | -6.25658 | -42.49046 | 2025-09-26 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d15515d7-9e11-34e3-a895-3d6e2132fad7 | -6.26138 | -42.49807 | 2025-09-26 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d629fd53-4ff3-3431-ad22-eba7bdeefe82 | -8.14089 | -42.37923 | 2025-09-26 03:21:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d29757d3-5198-3592-997c-7618c2480dec | -6.3774 | -35.20897 | 2025-09-26 03:21:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 50.1 |
| dec05210-9cf3-305d-bb26-3cc6dae3791d | -6.37226 | -35.21514 | 2025-09-26 03:21:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 54.1 |
| 8639ab12-08f6-3152-aa7c-127c087dec48 | -6.42208 | -43.07668 | 2025-09-26 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc70e7ed-b3df-3a50-8e8b-60d749e6cf1a | -6.59185 | -41.92236 | 2025-09-26 03:21:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2fb0b411-e4f6-3858-9de7-52a875846b67 | -5.3127 | -43.14346 | 2025-09-26 03:21:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f2f9f8a-e954-3876-a574-81bff8e7c46b | -5.45484 | -43.07271 | 2025-09-26 03:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ddd3f24c-3033-3120-b4a1-902874b22191 | -4.38589 | -41.92542 | 2025-09-26 03:21:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ba72797d-5205-374f-ab85-d29ee992eb6e | -10.06208 | -36.16039 | 2025-09-26 03:21:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5db88af3-436e-357f-a35b-cf407ac1270e | -6.59792 | -41.92418 | 2025-09-26 03:21:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f8a58291-6755-3b29-9fce-ba2d3de7e127 | -6.87721 | -44.50727 | 2025-09-26 03:21:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c9c3ef9a-0bac-3d5a-9b8f-f96c13497a77 | -6.86692 | -39.26443 | 2025-09-26 03:21:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 579412e8-dc1e-3203-bd96-7f2f56f602b6 | -4.8188 | -42.74512 | 2025-09-26 03:21:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ce94d65-1c11-31a1-9168-3370d5bad28e | -5.4638 | -43.06175 | 2025-09-26 03:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 78d99f6d-95a6-35a3-9daf-6d9665d28cc0 | -6.25583 | -42.49197 | 2025-09-26 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3f015fb6-9abe-3fcf-9ff2-39c9f5b26e39 | -5.21209 | -39.85769 | 2025-09-26 03:21:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cbee3843-9b24-380a-a782-06b01ca42ee0 | -6.95907 | -43.24852 | 2025-09-26 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 6934ad23-8a01-3a0c-a750-feb2bd6bc1d5 | -4.82158 | -42.7492 | 2025-09-26 03:21:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 023fdc21-2e86-3ea4-9d2a-88a678878fac | -6.31985 | -41.88725 | 2025-09-26 03:21:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f0cc4bd3-ad2b-320b-912f-2c976334bfb8 | -6.37682 | -35.21239 | 2025-09-26 03:21:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 50.1 |
| fceaeef2-33c3-37f4-8d2f-08609e4cf964 | -9.44611 | -40.38343 | 2025-09-26 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9212e80f-22ae-399d-803a-aa5cce14bf6b | -6.42101 | -43.08245 | 2025-09-26 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51ff35b7-eaf7-36f4-bdaa-d72bcdb62622 | -6.36885 | -35.21107 | 2025-09-26 03:21:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 08c2dbfb-19a4-39f3-b693-667585ac1e60 | -5.36967 | -42.29237 | 2025-09-26 03:21:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a4b5c1bd-dd96-361c-b228-6454a24593b1 | -5.36868 | -42.29785 | 2025-09-26 03:21:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4278a188-2a94-3acd-9437-1bf986f5d0a9 | -6.37342 | -35.20828 | 2025-09-26 03:21:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 50.1 |
| f29c19ad-7c8c-3c6d-9fe9-6d3a63c9cb1e | -5.46273 | -43.06765 | 2025-09-26 03:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 73bc4af1-98a8-361d-b162-b17230903248 | -6.11529 | -44.22876 | 2025-09-26 03:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0177e60d-51d8-313e-8113-d36cc658a870 | -5.92386 | -42.91906 | 2025-09-26 03:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| bf885ab6-03da-359a-8f9e-760f58d8b74b | -6.25784 | -42.48082 | 2025-09-26 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 60478fa9-4f45-3d2d-970b-8313d8cce6f2 | -7.05295 | -41.43426 | 2025-09-26 03:21:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ecb90e43-dba2-3783-8be3-80c89b1f809f | -6.36086 | -35.20985 | 2025-09-26 03:21:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1f37b6e0-138e-32c9-8c47-da976f49fbc0 | -6.37624 | -35.21581 | 2025-09-26 03:21:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 54.1 |
| ceb2bd9d-8162-38d0-997e-1f79f2421098 | -5.46947 | -43.06888 | 2025-09-26 03:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 0ac4fd66-98e6-305f-9b2b-4014bab2c542 | -6.87347 | -44.5124 | 2025-09-26 03:21:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f4bff54c-543e-34b7-abd7-13b5201547a6 | -6.59621 | -41.92509 | 2025-09-26 03:21:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e8136b5b-8720-345d-9689-fdbfd5352c90 | -4.7531 | -43.61493 | 2025-09-26 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 600a1232-9671-30c1-9194-4779795b608a | -6.9606 | -42.30698 | 2025-09-26 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db8d865d-a2d1-30f0-a911-5970f7d3341a | -6.37167 | -35.21856 | 2025-09-26 03:21:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 54.1 |
| 31964c26-eeed-3322-911a-17d3aaeef892 | -11.65113 | -45.35794 | 2025-09-26 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad7ebe1b-bd0e-3b11-a400-4c59cbe78e08 | -11.21946 | -45.62024 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56bf7905-7d5d-3836-95d8-06bd758ad908 | -11.21633 | -45.63537 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38a43f97-1b32-32bf-a3a1-d8ffa7b7e59c | -11.22138 | -45.61091 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08c515c5-c514-39c7-9515-949538447c06 | -11.22029 | -45.58035 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7c7e6df1-7acb-33d6-a6cf-65e171a2f49d | -10.56602 | -44.08537 | 2025-09-26 03:23:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33358282-7a30-3a56-8713-fe5dfe457e9d | -11.22509 | -45.64339 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de4e80ec-fe9b-3a42-a255-3df2083da9d3 | -11.22475 | -45.61011 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bec0a5b4-5818-3e09-9296-158a5aa685a8 | -10.92827 | -42.78888 | 2025-09-26 03:23:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 962e474e-005a-3923-ba5c-edf8f0a5e65c | -11.67855 | -44.45898 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbc9fc99-cfc4-306f-9c21-2db244b0ebb7 | -11.24101 | -45.56845 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 619222df-91ee-3017-9755-a0397f846281 | -11.66974 | -44.45443 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc3aad4a-0249-3494-9ed9-902edf856dea | -11.38609 | -44.94906 | 2025-09-26 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5ad5a317-15c0-33a4-bfcf-8363e33d1807 | -11.65822 | -45.35875 | 2025-09-26 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f66586d1-8257-3c60-801d-2101b650c17c | -10.00278 | -44.18864 | 2025-09-26 03:23:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9815db3d-bbf9-32e6-b7d7-b3b70938c94b | -11.437 | -44.94379 | 2025-09-26 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33008da0-6fe9-3e76-a933-c289aaf4152c | -11.66299 | -44.46775 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17575a6b-6c91-3805-ae13-6e8e721d32d3 | -10.09813 | -45.31707 | 2025-09-26 03:23:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cad95f4-2c45-35dd-83c1-0fa77abc8161 | -11.47818 | -39.00349 | 2025-09-26 03:23:00 | NOAA-20 | TEOFILÂNDIA | BAHIA | Brasil | 2931509 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 789aba74-a5d0-3125-b2b6-7f1602b42b30 | -11.23571 | -45.6132 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 360ae676-cd4d-351c-900a-16571f74dcc4 | -11.22105 | -45.62748 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ce87324-9adc-3583-a908-9011d7891101 | -10.5726 | -44.08672 | 2025-09-26 03:23:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce72763e-4024-398c-88f7-a3197795dadd | -13.84252 | -45.62483 | 2025-09-26 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65a9a1fc-5d6f-30f4-8b47-dcd04a87a060 | -10.004 | -44.18245 | 2025-09-26 03:23:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dfce92d-73e4-3307-af76-4274089a3396 | -12.73347 | -43.46208 | 2025-09-26 03:23:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfc123c9-fc0b-3423-9b7b-04639e8575d2 | -11.61925 | -44.44582 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7def7694-c736-392a-8362-9908b79e73fb | -11.22678 | -45.62066 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72b96f87-e463-301b-ab2f-2617eb85f34b | -10.92882 | -42.78844 | 2025-09-26 03:23:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c00d7c6d-ba80-3ed2-8e66-349252c99286 | -11.23569 | -45.62839 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 68aa5acc-a51a-3dfb-95f7-6343edf16d50 | -11.23191 | -45.61126 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5743828f-3d7f-3e7e-a91b-be296cfae1de | -14.34013 | -44.50185 | 2025-09-26 03:23:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6d6496f-abbf-3069-9dec-562f78c14d9b | -11.66538 | -44.45601 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2277b774-5bde-3748-889e-d56f4bb949c3 | -11.21454 | -45.57243 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d24dc2b-170d-3b6e-b20f-fa5cea9af183 | -11.23724 | -45.60577 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0fc0c684-de04-32bf-90c1-f959d4273cca | -11.21801 | -45.64176 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d0b258c-38d6-3268-9ce5-750806fadd45 | -11.24617 | -45.6139 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README6.md)
