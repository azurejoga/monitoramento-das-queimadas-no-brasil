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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0b7c318-adfc-316e-a61b-ad2da420d443 | -3.2828 | -51.418098 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8248319b-3d88-3e2e-a7c5-5b55414e18f0 | -12.7412 | -45.414001 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f758b08-b3fc-31d2-9569-f6896ce05800 | -4.8689 | -49.000198 | 2025-11-18 00:11:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 904e1827-b024-3469-a60a-568ffce699f6 | -12.2363 | -49.369499 | 2025-11-18 00:11:00 | METOP-B | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22750861-c722-3549-a905-2f86cc7160c8 | -2.6906 | -49.164101 | 2025-11-18 00:11:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d76072e-3bb0-3e3b-9335-464d34f2b7d7 | -4.5516 | -48.465099 | 2025-11-18 00:11:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35e86f15-3c83-342b-9745-5ec9ddb00015 | -3.4631 | -46.056499 | 2025-11-18 00:11:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5b3ad949-e90f-3eb4-8dab-73d860330bde | -5.7495 | -49.249298 | 2025-11-18 00:11:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40508ffb-642a-3a7b-aa13-6e78a8eaf0ba | -7.6093 | -42.575699 | 2025-11-18 00:11:00 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9a0ce859-8977-38bf-afa0-3e7df8aa9368 | -7.1784 | -45.498901 | 2025-11-18 00:11:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 188e71fe-5d47-3ab8-abd2-d1dea48acbbb | -9.9711 | -44.7789 | 2025-11-18 00:11:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 21dd24f9-3953-3c48-8374-21d07eff5e22 | -7.425 | -45.185902 | 2025-11-18 00:11:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d33af5ed-91e7-3a2b-9561-c6d8e0216545 | -3.0761 | -50.2281 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c847807b-90d5-3e75-bfc6-afbd970afc5b | -3.1227 | -45.742001 | 2025-11-18 00:11:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de847af1-8c66-32e5-9a5d-b539169145da | -6.1534 | -46.102299 | 2025-11-18 00:11:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81bbcff1-9b6f-3150-9ad4-2be7f1e85ca0 | -1.7738 | -54.173901 | 2025-11-18 00:11:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff15b94-76fa-3762-b27a-8def17d8b30c | -10.8481 | -44.864799 | 2025-11-18 00:11:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5033919f-0e39-352c-be06-d0fb52177eae | -2.471 | -50.239799 | 2025-11-18 00:11:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5af60f24-0fcd-3475-b0b5-7186ec6c1174 | 0.2385 | -51.103001 | 2025-11-18 00:11:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 662b5ba3-5782-3849-a07d-171ea0a91f52 | -7.619 | -42.573299 | 2025-11-18 00:11:00 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fa8c510d-ef17-3639-a982-bf0606d7e5bb | -3.4894 | -52.339199 | 2025-11-18 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eddc25b6-655b-3fb4-a6c1-f99faadf1820 | -10.3578 | -48.911499 | 2025-11-18 00:11:00 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8eb16e5-a2e8-3b27-91c2-14da5ed231a1 | -4.092 | -45.6133 | 2025-11-18 00:11:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b7657fc6-0860-3aa8-824b-831354867871 | -10.8487 | -44.253502 | 2025-11-18 00:11:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01ee4c55-3adc-39ea-a0d4-2cf269214cd4 | -2.2886 | -47.220798 | 2025-11-18 00:11:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae6ec5bc-f705-396c-a68b-f82233255f12 | -2.4931 | -49.337601 | 2025-11-18 00:11:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ce5a1ac-61fd-3579-adeb-e8220c70e6df | -7.3522 | -46.202301 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01a2be17-0846-3b46-9d1d-48dd45da6cfe | -5.2135 | -50.161999 | 2025-11-18 00:11:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca3a7bee-470f-3870-a8b1-37a9477973b1 | -12.7429 | -45.421501 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46be521a-2423-3976-b789-325c8f48663c | -2.2903 | -47.2285 | 2025-11-18 00:11:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 669ab383-2e90-3f93-bec5-24641e1aee53 | -3.6503 | -50.216499 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79d00c84-f204-35e7-983e-589f894cfe75 | -2.9885 | -45.4291 | 2025-11-18 00:11:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 96f574c8-30e2-36fd-b293-f996c9965b3e | -11.2888 | -48.516399 | 2025-11-18 00:11:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56b719b6-c335-31dc-a0e5-4efb55b46035 | -4.7065 | -46.308998 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d2ce7ff-4295-3ce9-86fd-7a5805f5ff04 | -2.5171 | -47.814701 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3970c26-5713-3b9d-a9f4-3632a6043dc5 | -7.8548 | -46.861198 | 2025-11-18 00:11:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c9e28a4-ec4b-31ff-819d-aa8a35833d00 | -10.7249 | -44.428799 | 2025-11-18 00:11:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b1b8b95-3d74-3ee2-ac40-237e0127aac2 | -6.6631 | -43.747101 | 2025-11-18 00:11:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8fa0281c-dbfb-3664-918a-920fc73fc834 | -4.3656 | -46.5289 | 2025-11-18 00:11:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c11235fa-2f8d-33e9-b07d-2b489f9e8a89 | -8.1072 | -43.533501 | 2025-11-18 00:11:00 | METOP-B | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3ada46bd-4851-3291-acf6-7dcae21f4aaa | -4.6349 | -45.644299 | 2025-11-18 00:11:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63548c49-4c27-3fc3-b700-9d7cb44c8714 | -3.6778 | -50.246799 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b18808e-8003-3de4-a869-7894379825e4 | -4.5547 | -48.478901 | 2025-11-18 00:11:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20b05ecf-1294-35ad-b325-91058392334a | -4.1618 | -44.2342 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9480b6b4-efa2-3b3b-8e10-3812733eddd6 | -4.5217 | -46.4016 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d4c5d42-0d1e-3f4f-88cd-da3595a4d3d0 | -3.1619 | -51.4758 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5284615-0c1f-36f1-b726-76dba5d677d0 | -3.0897 | -51.246101 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffa8e0ed-554e-3426-a162-8a429d2e4a66 | -8.2092 | -45.010399 | 2025-11-18 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8144480b-1754-3ad8-b40b-92685e5b6613 | -4.3922 | -49.761501 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c738b89-53f8-3c7d-ac0e-e36acb96abc6 | -6.9215 | -39.600399 | 2025-11-18 00:11:00 | METOP-B | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2562afa0-e94e-364b-9da8-0de27c011c6a | -4.226 | -46.325901 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0f563e3b-e4f0-359e-b252-4522cd14a827 | -4.5235 | -46.4095 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5355890b-c5ea-3776-aa64-915aebc8d070 | -3.8342 | -49.7994 | 2025-11-18 00:11:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d94a301a-c0c5-371e-8057-bf7fc3ebc83a | -12.7007 | -46.7715 | 2025-11-18 00:11:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cb1ebf3-ca8e-3519-98b4-5b5f9d28001c | -4.1379 | -46.345901 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9348b7c9-246b-304f-a717-0245008b58f6 | -6.7168 | -46.3088 | 2025-11-18 00:11:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83fea401-39c9-3ff1-8264-013403f37196 | -3.4754 | -55.411999 | 2025-11-18 00:11:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b0c8230-2dab-3e0e-a7eb-36a53a0d380e | -7.0671 | -46.0401 | 2025-11-18 00:11:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36f5b0b4-2127-31db-be1b-19bb6a9fcb37 | -11.6865 | -44.697701 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8e4e608-9e84-3973-aa1f-7e16719b8ebd | -9.7251 | -49.1203 | 2025-11-18 00:11:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64dc6bd6-9e16-32ae-8276-4f44d9cc5a36 | -7.5682 | -46.288799 | 2025-11-18 00:11:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bde8c6c-2ba6-31f7-9056-1dd5486e6be6 | -4.6686 | -45.789501 | 2025-11-18 00:11:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0cffd53-bbcb-395d-b907-f1c45ee8c4f9 | -6.4067 | -47.2006 | 2025-11-18 00:11:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f006378-54ab-362b-8342-6724e5299596 | -10.6491 | -49.721699 | 2025-11-18 00:11:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec147776-119e-3f11-b8f6-18614cf5e22c | -3.465 | -46.064899 | 2025-11-18 00:11:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8122654a-d3a9-3848-9cbf-54f091ae078b | -7.4139 | -42.748699 | 2025-11-18 00:11:00 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e5dbde44-c0e8-3274-bfaa-98947d8a4296 | -7.268 | -47.902401 | 2025-11-18 00:11:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b7841a6b-28d0-34e3-b3a7-9b3c3476c1c2 | -4.5939 | -45.423599 | 2025-11-18 00:11:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d57e2649-fb92-3be1-b2c9-b06fbeede84d | -4.7028 | -46.292999 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2428cb8b-6689-393f-9291-f1494366b3ff | -11.6097 | -43.8923 | 2025-11-18 00:11:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be6ee5fe-f36b-37fb-88e0-11c75dc897fa | -3.0219 | -44.464001 | 2025-11-18 00:11:00 | METOP-B | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5570acfd-43d5-3dc0-a09d-481fcb25bca2 | -4.596 | -45.4324 | 2025-11-18 00:11:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4122cd7-5190-3732-8ed0-e909d9fa7937 | -2.817 | -45.3997 | 2025-11-18 00:11:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf36515-011b-3d7b-ac11-c193bc8e168e | -4.1361 | -52.104698 | 2025-11-18 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80c4443e-a9ba-3c9b-a4db-69fb3c775387 | -4.6357 | -49.563 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3c092f9-42c0-3edc-b489-bc39caf2c20e | -12.6893 | -46.7668 | 2025-11-18 00:11:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca769cc1-c5e6-3f07-a294-3ee9628855bb | -13.7913 | -43.7243 | 2025-11-18 00:11:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c52acf3f-24a7-3f78-bc7f-0546b707b54d | -8.3319 | -45.358501 | 2025-11-18 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e67c10d1-ad18-3ec5-a0af-aafdedae71eb | -3.4768 | -46.071201 | 2025-11-18 00:11:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d55783ff-5acf-36e4-958a-164c42040214 | -7.6848 | -46.839199 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23c570d1-c910-32b2-9d07-bf81398ba3fb | -3.2421 | -43.031799 | 2025-11-18 00:11:00 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47616fbd-2107-3563-b758-af45ebbc7c82 | -4.1759 | -50.172501 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87932fdf-ee66-38de-91f4-bc33dfc04fd0 | -5.3968 | -44.056599 | 2025-11-18 00:11:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3502999-64f7-3226-908a-1a9d755ec208 | -6.9337 | -49.6618 | 2025-11-18 00:11:00 | METOP-B | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a2595c5-be73-3198-88bb-fde4bdd1f529 | -4.09 | -45.6045 | 2025-11-18 00:11:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d351d06b-b7a0-3103-9708-484384aca638 | -3.1207 | -45.7332 | 2025-11-18 00:11:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8248c9b1-1544-348e-a0c6-aaf50a2355d5 | -5.4102 | -43.0261 | 2025-11-18 00:11:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 227b27be-2e4e-3ba8-ae96-ff9ec98d288b | -3.073 | -50.214298 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bcd906e-53d2-3241-bbd9-d6fe5b66d438 | -10.3764 | -49.883999 | 2025-11-18 00:11:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4568abdd-c57b-3bdd-9c86-350b38a4772a | -4.0526 | -47.4991 | 2025-11-18 00:11:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 212de963-6248-3313-93c3-de1922934908 | -4.5531 | -48.472 | 2025-11-18 00:11:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5461dccd-9612-3703-84ca-de7be4521e55 | -9.7188 | -48.9067 | 2025-11-18 00:11:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f575ac02-f84d-36e6-8b5d-f0994cbd7d58 | -3.9938 | -50.5065 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f87473fb-6ce0-370b-b234-09efddf4de87 | -2.5155 | -47.8074 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29832e81-d61c-3360-a253-4968f6dc1f32 | -11.6175 | -48.5611 | 2025-11-18 00:11:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a1d544e-6a15-3ab0-a2ac-01f6560d0308 | -10.663 | -49.363098 | 2025-11-18 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d425a09-3fd0-3822-98c8-02763f17b5c2 | -6.3092 | -43.7757 | 2025-11-18 00:11:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56fd49ca-bd8f-3271-acc7-04b477e1dbb0 | -12.5056 | -49.8564 | 2025-11-18 00:11:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05f8e1ea-5b00-3621-87de-4d9b60bc08cd | -11.2572 | -44.540798 | 2025-11-18 00:11:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29933abf-dc60-3d90-9cbb-ccba9d099227 | -4.6379 | -47.939499 | 2025-11-18 00:11:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
