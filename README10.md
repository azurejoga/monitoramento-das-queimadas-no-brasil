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
| 9732472f-0992-3af8-a62a-85dd9c6c8591 | -2.7128 | -49.319698 | 2024-11-03 01:09:10 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e67108c8-df36-33d7-a216-261ec90e44a9 | -2.7171 | -49.338001 | 2024-11-03 01:09:10 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c245460-feb9-3e82-a5d9-d45d2e1c617d | -2.7031 | -49.321899 | 2024-11-03 01:09:10 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70ea1166-34b4-3885-851a-2f01c468afc7 | -2.7074 | -49.340302 | 2024-11-03 01:09:10 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3f35a8d-9340-34f1-852d-c59be1227c4d | -2.7117 | -49.358601 | 2024-11-03 01:09:10 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa1100da-0e22-3329-8695-540fba286152 | -3.4118 | -52.393299 | 2024-11-03 01:09:11 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dda29e6-839f-3e03-8564-731816bb74b4 | -3.4144 | -52.4044 | 2024-11-03 01:09:11 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15a79235-6d34-3052-bd6c-bacfa5d1c0bf | -3.102 | -51.108398 | 2024-11-03 01:09:11 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58858120-1673-393a-82a4-0d74c5fdb5ce | -3.6221 | -53.523499 | 2024-11-03 01:09:11 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87b73966-c8d5-3c1c-bc42-c30069120f1e | -3.6124 | -53.5257 | 2024-11-03 01:09:12 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 770c2019-6d9d-34c8-895b-af4e6199d675 | -3.7375 | -54.068401 | 2024-11-03 01:09:12 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34963996-c382-3ca7-8d53-08d33bb45acd | -3.7257 | -54.062 | 2024-11-03 01:09:12 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aed67e2c-c3ac-39b9-9f8b-2ca7d6dbe262 | -3.7277 | -54.070702 | 2024-11-03 01:09:12 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 857fccc2-0645-3b16-8eae-c39476690001 | -4.0638 | -55.5369 | 2024-11-03 01:09:12 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89cdb8b0-d21d-379c-8050-ebf95591a3e8 | -4.0655 | -55.544399 | 2024-11-03 01:09:12 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a044c5cb-62e3-33f3-b402-caa39120d919 | -2.7262 | -49.855202 | 2024-11-03 01:09:12 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 861528a7-4ff7-3906-b4c5-70d78696d901 | -2.7165 | -49.857498 | 2024-11-03 01:09:12 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c161c3f5-fe2a-33bf-88ac-5bbc340cc78d | -2.4015 | -48.866299 | 2024-11-03 01:09:14 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1398be4a-7950-3399-ad49-2e2ca033c63c | -2.2072 | -48.172699 | 2024-11-03 01:09:14 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d96cf37-bfed-3fac-83bf-16ae58b60704 | -2.1976 | -48.174999 | 2024-11-03 01:09:14 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 555351e0-e6ec-3924-be65-76a46cef9722 | -3.2624 | -52.724499 | 2024-11-03 01:09:14 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09933ff4-4af0-3bd7-9c42-cbd7f369365e | -3.2648 | -52.7351 | 2024-11-03 01:09:14 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c342b40-e915-332c-ae2b-703ca5b81e08 | -3.2673 | -52.745701 | 2024-11-03 01:09:14 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 340e4770-e0e6-3b15-92b6-0756b6952daf | -2.2809 | -48.787899 | 2024-11-03 01:09:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3f97844-0bbf-389d-9fdb-baeb6a425aed | -2.2857 | -48.8083 | 2024-11-03 01:09:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d3ac425-7592-3a1b-8e87-3c19e1b0ee7d | -2.2904 | -48.828499 | 2024-11-03 01:09:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed859950-67a1-3d9d-ad26-fda2ffece786 | -2.8705 | -51.304001 | 2024-11-03 01:09:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28fe43c8-1dad-382b-821e-851dcfd3ad39 | -2.8736 | -51.317299 | 2024-11-03 01:09:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07481120-efa1-382a-b7cd-3a9812a6c498 | -2.2712 | -48.790199 | 2024-11-03 01:09:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e4caa2b-f1c8-3b76-8a30-70968b9d83a1 | -2.276 | -48.8106 | 2024-11-03 01:09:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c8defa7-7032-3939-9309-4a8eeb104e52 | -2.2807 | -48.830799 | 2024-11-03 01:09:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10176963-79e9-31bc-be27-aa55d3a4db32 | -2.8976 | -51.464298 | 2024-11-03 01:09:15 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0fd7375-77fe-36c3-9087-ac2ca995556f | -2.9006 | -51.4772 | 2024-11-03 01:09:15 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee87c89b-a2b3-3d9b-bedb-ac6a4e32ac2c | -3.2389 | -53.067902 | 2024-11-03 01:09:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 099eb25f-b598-3d13-87e4-56ea90b88fdf | -3.2412 | -53.077999 | 2024-11-03 01:09:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50b0fdc8-bf19-3274-84ca-515ad239a1c7 | -3.5825 | -54.559502 | 2024-11-03 01:09:16 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a96aa79-4005-3237-a855-d030ae82a348 | -3.5588 | -54.590801 | 2024-11-03 01:09:16 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a857150d-4870-3f33-b5fa-b2a7f7900d0b | -3.796 | -55.628502 | 2024-11-03 01:09:16 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa22681d-6825-376e-b392-7eaaa6f35edf | -3.7977 | -55.635899 | 2024-11-03 01:09:16 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 036afb41-3129-3325-a826-2e07cbc94c3b | -3.7994 | -55.643299 | 2024-11-03 01:09:16 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b24a3b9-58aa-3a82-ae71-7f014239a403 | -3.549 | -54.593102 | 2024-11-03 01:09:17 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 389ea429-7d63-3a56-84b5-550a6849526c | -3.5603 | -54.642502 | 2024-11-03 01:09:17 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47a2301f-7ab4-3347-b09b-4ca4742e443a | -2.8817 | -51.7491 | 2024-11-03 01:09:17 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75c7cecc-b017-3e27-9e66-f1e2ec90389d | -3.2541 | -53.3564 | 2024-11-03 01:09:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92027e83-1f54-386c-b6ea-976ec302719f | -3.8549 | -55.9772 | 2024-11-03 01:09:17 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b5c3ec4-5d61-344e-935b-c7fedd51d30c | -3.2555 | -53.406898 | 2024-11-03 01:09:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31e39654-d814-3fcc-8f1d-f674594942f6 | -3.2577 | -53.416599 | 2024-11-03 01:09:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c5e8576-6327-34dc-8ca8-573f27af064d | -3.2345 | -53.360802 | 2024-11-03 01:09:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8a84b0-4796-33f7-a142-d1bbfcdfc02e | -3.2435 | -53.399502 | 2024-11-03 01:09:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dceb3e0-9cee-3004-a3d6-172676142b58 | -3.2457 | -53.4091 | 2024-11-03 01:09:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba564e2d-0a26-3e40-aa87-8fac26e12936 | -3.2479 | -53.4188 | 2024-11-03 01:09:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4557ef8-8cc7-3e32-a303-9acd126d2e80 | -3.3322 | -53.784599 | 2024-11-03 01:09:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5661bf2c-f339-3b2a-b3cf-d37eb4824451 | -3.3343 | -53.7938 | 2024-11-03 01:09:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 906abd33-a426-3844-aa2f-4790538c9311 | -3.2315 | -53.392101 | 2024-11-03 01:09:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb76cd5-5c2f-39c9-ada5-b8a484731a02 | -3.2337 | -53.401798 | 2024-11-03 01:09:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f3c6c36-cbd6-3a7e-b65d-1206d179576a | -3.2359 | -53.4114 | 2024-11-03 01:09:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5910bd68-4bc3-3992-bf25-5502eca25d00 | -3.3246 | -53.796001 | 2024-11-03 01:09:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86f107a6-1b1d-39c2-8cdc-b0507f2ee1e7 | -3.2217 | -53.394299 | 2024-11-03 01:09:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a7aa0a0-3a83-3969-826f-ccb69cfa4c31 | -3.2239 | -53.403999 | 2024-11-03 01:09:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6324204f-5d26-3343-a32c-81ff3556bd81 | -3.2142 | -53.4062 | 2024-11-03 01:09:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65313942-10df-334f-8cca-50c928444503 | -3.2164 | -53.415798 | 2024-11-03 01:09:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8cb80a7-a515-32d9-aef9-4efccdb065d8 | -2.7851 | -51.598701 | 2024-11-03 01:09:18 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4532a318-6088-30d4-aa4c-b42e52e5646d | -2.788 | -51.6115 | 2024-11-03 01:09:18 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ae88bb8-ccca-3a97-975e-9b6ccf9fbd51 | -3.2021 | -53.3988 | 2024-11-03 01:09:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0dfc263-3091-349d-8379-e2220b83d3cd | -3.2044 | -53.408501 | 2024-11-03 01:09:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d8cb997-66ea-376b-9567-649e0949b76d | -3.2066 | -53.418098 | 2024-11-03 01:09:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d334309-25c1-386e-9ced-e977ec31e254 | -3.699 | -55.564201 | 2024-11-03 01:09:18 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e641d50e-62c0-37ad-9a66-17640d326c4e | -2.7754 | -51.601002 | 2024-11-03 01:09:18 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f0e7b47-1a0f-3f8b-b03a-4a387f2fa19e | -2.7783 | -51.6138 | 2024-11-03 01:09:18 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b95f358-efe7-3bc7-b92e-d7eafd7f8e04 | -3.1946 | -53.410702 | 2024-11-03 01:09:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbb66b5a-4f53-3a66-9d74-e1e7ae6eba2c | -3.1968 | -53.4203 | 2024-11-03 01:09:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11c3f75c-4d5d-314f-9771-0b44e46371cb | -3.2608 | -53.743 | 2024-11-03 01:09:18 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c7f38dc-f5e7-3ad5-ba39-a3a85857dbfe | -3.263 | -53.752201 | 2024-11-03 01:09:18 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8dc9813-4f5e-37ae-9c80-4ecfea17b536 | -3.3284 | -54.170601 | 2024-11-03 01:09:19 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbe0d40f-def6-3198-a631-af394b97f201 | -3.0367 | -53.261398 | 2024-11-03 01:09:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9915a8ac-eda2-37a5-a854-f4ec665414ca | -3.0389 | -53.271301 | 2024-11-03 01:09:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0977236-3566-3738-9a13-defe72371381 | -3.0412 | -53.2812 | 2024-11-03 01:09:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d34f5cee-6c46-3f36-887b-0d19d7b85f6a | -3.0292 | -53.273602 | 2024-11-03 01:09:20 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ced25648-3105-3523-ae87-fb5b48847cb8 | -3.2854 | -54.521702 | 2024-11-03 01:09:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e09b782f-faf0-3d87-9395-ec849efb83f3 | -3.2873 | -54.529999 | 2024-11-03 01:09:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54f4a00f-a2ba-3653-9b51-b2f77abb7419 | -2.8007 | -52.4631 | 2024-11-03 01:09:21 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbea5073-9e7b-317e-bda9-c7002f6a304d | -3.2775 | -54.532299 | 2024-11-03 01:09:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ddeb52f-50a7-32aa-80ad-c38aba169773 | -3.2794 | -54.5406 | 2024-11-03 01:09:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f403e135-88e4-322d-8095-833966282700 | -2.7909 | -52.465401 | 2024-11-03 01:09:21 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37613650-9987-39a8-978b-b82a2b9ae59f | -2.7935 | -52.476601 | 2024-11-03 01:09:21 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05e88df5-2ab9-3245-ab03-e72bf825e19d | -3.2677 | -54.5345 | 2024-11-03 01:09:21 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3ed5bfc-16b5-3570-af6d-6663c4bb3518 | -3.1307 | -54.251999 | 2024-11-03 01:09:22 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ccd64ff-deb3-331a-9b88-5d8eed211d58 | -3.119 | -54.245602 | 2024-11-03 01:09:22 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d17e4cb4-3533-3ff4-a238-0333ff957112 | -3.121 | -54.2542 | 2024-11-03 01:09:22 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5de3f976-7f94-3b9c-a51a-11af8ab6c4af | -3.123 | -54.262901 | 2024-11-03 01:09:22 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff7e2bdc-623f-3145-99b5-18a040fcb834 | -3.1092 | -54.247799 | 2024-11-03 01:09:22 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97e93995-c111-309a-92d1-ecb30d7f6671 | -3.1112 | -54.256401 | 2024-11-03 01:09:22 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1bd6cd5-99a9-3adf-b66e-9cb352bc7fb1 | -3.1132 | -54.265099 | 2024-11-03 01:09:22 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26c1b9ef-bcac-3208-a179-d3233cd97a3e | -3.0753 | -54.145 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf14665f-f0f2-3abe-a5dd-5c58b2c2d622 | -3.0773 | -54.153801 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11b98138-9569-3328-979d-1a13e4a95038 | -3.0793 | -54.162601 | 2024-11-03 01:09:23 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e9b21ab-c31c-3be8-9b1e-23b1d0473d46 | -3.1073 | -54.284599 | 2024-11-03 01:09:23 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66beb0ae-c5b7-351c-a047-b7b7b3fb6a6e | -3.1093 | -54.293301 | 2024-11-03 01:09:23 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e35d9c7-abd7-3f03-80cd-4905b5b5eb25 | -3.1113 | -54.301899 | 2024-11-03 01:09:23 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62404183-de86-3478-86c2-2cae079c99bc | -3.1485 | -54.464199 | 2024-11-03 01:09:23 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
