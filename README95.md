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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c804a0a1-9409-3d2e-ab0f-340211b57235 | -17.77765 | -53.05557 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3e56518-944f-35b3-bf71-28f36739991f | -17.76512 | -53.11835 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abe08c08-f010-3257-a841-6e3642c337c6 | -17.71165 | -53.04129 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c84c176-5a1e-3d47-b16b-0174931e631b | -17.70989 | -53.0388 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5211b596-fb7a-31b1-aa3a-a09366426299 | -17.70925 | -53.04334 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3935242c-e6f7-3088-822a-7db50b13b297 | -17.70795 | -53.04071 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 185fb366-aaf6-3ff9-997b-1daa7ea37c80 | -17.70555 | -53.04277 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fb95e17-7957-3572-a3c4-d8a2f0f62035 | -17.70425 | -53.04012 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81c599db-1fc9-323a-943c-e9dd8d583550 | -17.70186 | -53.04217 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40260c17-cfd7-3eb7-8f80-d9f003dce25d | -17.70056 | -53.03952 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1d02e5e-d047-3e72-bd48-9a052cc33c05 | -17.69447 | -53.04097 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbcd7856-9cc8-39a7-8d55-fb44bede0b4d | -17.69078 | -53.04038 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 668d502a-f8e6-3a3e-8227-08a2a454d519 | -17.68544 | -52.63649 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8311bb6e-95b3-337f-ae92-fd3d34a2bbce | -17.67599 | -53.03813 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa1e4334-7644-36d2-b72f-517b8ac334d8 | -17.67051 | -53.0233 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94076911-0a7e-3da2-a0da-2fd4d718fed4 | -17.66681 | -53.02273 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a71e1b27-3af1-3a7a-8cc5-4f9c21862811 | -17.66618 | -53.02728 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 20d6cec7-b30b-3913-8c81-c2718e0fc2d3 | -17.66311 | -53.02216 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 588732b2-289f-309d-8625-ca87aa8810c9 | -17.66248 | -53.02674 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b17c3983-50af-3216-9a37-33826a36c178 | -17.65814 | -53.03078 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3da458af-f35e-3773-97e9-cf40b2c29150 | -17.6575 | -53.03534 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 33613e1b-c880-39fd-84c6-ca660e686bbd | -17.6538 | -53.03484 | 2024-10-08 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 61052035-fb11-3076-83fd-fb06ab6d56df | -18.49768 | -53.4522 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c65974f8-4361-3b9b-a574-c85503278969 | -18.49643 | -53.4611 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bb79eb91-298a-3a47-b0c8-7c10fa84d3ac | -18.49527 | -53.44282 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dae67c07-856f-3fab-b577-0fef5fc1d8d7 | -18.49465 | -53.44727 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9d4baf6e-25ec-30b8-8bdc-35583a0b03ba | -18.49402 | -53.45172 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 76bec705-be5d-3a11-ad42-2db2c950f421 | -18.49224 | -53.43779 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e73cfcc4-5b15-3a56-a1a8-2706bca3a991 | -18.49161 | -53.44226 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fad2348b-ec4c-3cb1-a4ea-e880c16d88ff | -18.49099 | -53.44674 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3da33ea6-7694-3e69-9c97-abec08f11007 | -18.49035 | -53.45125 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3279cf25-939c-3f43-a0e5-e8dea11363b0 | -18.48972 | -53.45572 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 34b649db-3a4b-3675-a49e-4fd19194929a | -18.48843 | -53.49136 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 967a9413-fea4-3118-8567-7155a2b3b202 | -18.48796 | -53.4417 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3f730ae0-3620-3b34-a8ca-48e2ea3acb8e | -18.48733 | -53.44619 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0c0ac66d-a1b9-3e0d-b717-c749d22bc8d1 | -18.48669 | -53.4507 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2d14e3ae-2bf2-3e02-a2dc-7060f5d117c3 | -18.48606 | -53.4552 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dede1057-609b-3dce-9385-d371525001cf | -18.48545 | -53.45958 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6a9d07ff-0f4c-3e5c-ae11-efeac4ea9a8b | -18.48478 | -53.49081 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65f4af95-6ac0-3d23-9a31-3ea1b2b248ba | -18.48369 | -53.44552 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0bf2c17b-c9e0-3ddd-9e0a-85fd1fac10c8 | -18.48306 | -53.45003 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c728701-f305-3887-aa65-5632b49a3170 | -18.48242 | -53.45452 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23d7e7fd-3993-365d-8377-a106ab5c8c17 | -18.48113 | -53.49027 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a24986c2-ddf7-305f-ab0c-cec52770381b | -18.47987 | -53.49921 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aaa94938-1c22-3b4e-bb8e-3b4842044a9c | -18.47622 | -53.49864 | 2024-10-08 04:59:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12a9a602-2a15-3e05-a98a-55ad705a43ef | -18.55354 | -52.62941 | 2024-10-08 04:59:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9a94812-6275-36f2-9f2f-bceaeb026cd0 | -18.55289 | -52.63432 | 2024-10-08 04:59:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16c31c10-4dfa-37cc-9a8b-1f8243b794b0 | -18.55223 | -52.63922 | 2024-10-08 04:59:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c6048e4-bf9d-3dda-913a-3bfc37a20232 | -18.55158 | -52.64411 | 2024-10-08 04:59:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0926eb7-2b41-333f-90a4-ad9f881b2a30 | -18.55093 | -52.649 | 2024-10-08 04:59:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b405fcf-069e-3008-8c8b-4b1e4c40c2cd | -18.55083 | -52.6788 | 2024-10-08 04:59:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c214713-11b7-30d6-8da7-f26623e514ab | -18.55027 | -52.65389 | 2024-10-08 04:59:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9800e0e6-1962-34de-8033-334f9641b4c6 | -18.54907 | -52.63372 | 2024-10-08 04:59:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c6eb0d08-f482-3c36-9a37-d09213e08f57 | -18.54776 | -52.64352 | 2024-10-08 04:59:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d862b466-80a5-3f5c-8955-63097ddda778 | -18.54525 | -52.63316 | 2024-10-08 04:59:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 500c120c-5de0-3520-aecb-db1bb163b562 | -18.5446 | -52.63806 | 2024-10-08 04:59:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12e877f4-bd5a-35de-a0fe-8b974bbf3fae | -20.47754 | -53.6745 | 2024-10-08 04:59:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c68e392-76a7-3bdb-9377-360d406102d0 | -18.08423 | -54.30703 | 2024-10-08 04:59:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37741d51-39a3-307d-8618-48ee70edd8b7 | -14.83423 | -53.88667 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1583a66c-a2ba-3b81-85b5-506e24e0a5c8 | -14.83077 | -53.88611 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03677a8f-5a25-3a80-8f82-f531f52653f6 | -14.82731 | -53.88557 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2ffd346-8bc6-3b4d-8ac7-0a147e338ea1 | -14.82559 | -53.89722 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b18b8c67-9695-3b79-a357-0412306018e8 | -14.82502 | -53.90109 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea7be781-a2fd-3981-b7c7-769e0d91fac5 | -14.82385 | -53.88502 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 896667d1-991c-35f4-affa-65a71656f365 | -14.81066 | -53.92651 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e441b085-f40f-39a7-a366-ef3ca755cbc6 | -14.80778 | -53.92205 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a99540a-23f6-3ac8-9bd7-70e95d4e8a53 | -14.80721 | -53.92593 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e06563c-4d96-3b37-b9f0-338bf5291cd1 | -14.80664 | -53.92979 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0a21adc-798a-3037-9eb1-3ff1aba63b79 | -14.80376 | -53.92534 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3160fdb6-fb99-3900-9dbd-7a8996e18bfd | -14.80319 | -53.92922 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c1c2ed8-2be7-3a10-86ca-866c0947b8e9 | -14.80262 | -53.93307 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bcb1c2c-07b9-305d-a39d-022ad9c3e43f | -14.79974 | -53.92864 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6d0272c-e03e-34b2-8422-9a6b93a6649d | -14.79918 | -53.9325 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3184222-de6f-3a2e-bf3d-ed22c3409f99 | -14.79573 | -53.93193 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 813122e5-e025-30bd-8402-e8f19e986696 | -14.79171 | -53.93524 | 2024-10-08 04:59:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bb491e5-9aee-3052-864d-6d15a9580460 | -16.49885 | -53.96504 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 042a58a7-024e-3a4c-bee9-6a998e9b5a19 | -16.49865 | -53.96213 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56ba0d1c-e378-387f-bd21-a9cdbfc5651d | -16.4965 | -53.95648 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26ec0ccd-feb2-308f-b935-876fa516dfdf | -16.49574 | -53.95759 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 882e6a2a-d4dd-30f1-8e9f-ecf17af483a0 | -16.49046 | -53.9691 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9e4cad4-57c6-3e2f-a86d-51e39d42e612 | -16.48286 | -53.97209 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68f195bb-3c55-359d-a412-a41442594a15 | -16.4811 | -53.91084 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e49eae3b-1e14-329e-8de6-27c574b35567 | -16.47994 | -53.9676 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e968a63-a018-3c2a-813f-4fa7081f4a64 | -16.47645 | -53.96701 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11f390df-0571-3aa4-b1b7-b65de530f4dd | -16.47587 | -53.97099 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3540a0d4-63ef-36af-ac27-789b980da67e | -16.46999 | -53.91328 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3ea7047-24b3-3f99-929d-03bb63e195ea | -16.46829 | -53.9249 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf3c837e-88c3-3193-b330-96f442c5f9e1 | -16.4671 | -53.90849 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5137b42-629d-31ab-a312-f72bbff96a71 | -16.46651 | -53.91256 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c90b875-5cc2-3fcc-a055-4df84ae8b327 | -16.46594 | -53.91646 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c002db7e-5b67-3b69-a364-0b998be6c79b | -16.46246 | -53.91579 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfc0cb1c-8342-39a4-b85a-0f733c9b6f06 | -16.45838 | -53.91917 | 2024-10-08 04:59:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 796457e8-89e0-3550-ab69-559866c0639f | -15.36126 | -53.72714 | 2024-10-08 04:59:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db1d4153-6576-3c55-b32b-4062ca21dfb0 | -15.36068 | -53.73112 | 2024-10-08 04:59:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9b6730d-9cb1-3534-8c7e-c9d1f8cbf18f | -15.35719 | -53.73057 | 2024-10-08 04:59:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6268040c-de19-3f98-99d1-76f1c035661d | -15.35369 | -53.73001 | 2024-10-08 04:59:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b88c734-5506-3d59-acd5-f48afb3358cf | -15.3502 | -53.72945 | 2024-10-08 04:59:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e2fa00e-e194-362c-8a67-d3b784490c92 | -15.34962 | -53.73344 | 2024-10-08 04:59:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b2b2cbe-6b8c-3224-9ac4-9d58f96fdca2 | -18.08774 | -54.30751 | 2024-10-08 04:59:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73ee71b6-ba8c-3734-bf70-184a27a8e030 | -18.08717 | -54.31149 | 2024-10-08 04:59:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README96.md)
