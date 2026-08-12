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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dabd8b2-d130-3f31-86fe-f96cac8a7bca | -7.60061 | -42.75913 | 2026-08-12 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a987c373-49f9-3ca5-bd4b-93f42f91260e | -9.13235 | -46.39939 | 2026-08-12 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 287309be-a273-3ed1-8b5e-dbcf5572e798 | -7.92348 | -45.1109 | 2026-08-12 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 423a0b7e-f7b6-3446-91a5-b29cf54bc0f0 | -3.84945 | -49.09173 | 2026-08-12 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6cd1685-16a5-37ea-9d48-c7096a946c48 | -7.91076 | -45.11432 | 2026-08-12 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2dd0655-1cdd-3dc2-b7c0-143f523d7b10 | -4.31464 | -46.41619 | 2026-08-12 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2158fc26-1144-386b-a8d4-4befeab451b7 | -4.10779 | -50.44783 | 2026-08-12 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93370c7f-e38c-3c43-9885-f26a4907a794 | -9.13676 | -46.39546 | 2026-08-12 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e2da0fa1-cae8-34ae-adaf-9332c0bc319c | -3.48623 | -50.05381 | 2026-08-12 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efed77f9-d12e-3fd6-9236-07c86273000b | -3.14863 | -54.6083 | 2026-08-12 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7eabc43-b363-3056-bfe9-4789ff28db8f | -7.38161 | -45.1092 | 2026-08-12 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96253673-639d-3615-b0a5-2a1ea486a351 | -6.60741 | -59.00374 | 2026-08-12 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5d60df29-4333-3bb5-8caf-1aa18d9f03e5 | -8.48135 | -45.42161 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31ecbca5-6623-37b6-8e70-e58e71c72ab0 | -8.07762 | -46.51853 | 2026-08-12 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a155f4a-4d5e-3b93-9212-2c6eaae44eb4 | -7.01299 | -44.62751 | 2026-08-12 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cfa1b04-6365-33d0-b474-47b53d2b3f4e | -7.72462 | -46.22258 | 2026-08-12 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2daba1b-f5ef-3a83-8c69-bca230c59611 | -6.59375 | -59.00867 | 2026-08-12 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| de01d47b-f866-34f9-984a-d63e7c64ce52 | -2.85105 | -49.54058 | 2026-08-12 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65f6b1e6-a536-38d4-972c-caa82d9bfcab | -3.01543 | -48.84339 | 2026-08-12 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4f35f95-6ca8-37ff-aeb4-2214a00ab55f | -6.33798 | -44.05891 | 2026-08-12 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8280b3d-f469-365c-8964-bb1a692ae241 | -8.10934 | -47.18703 | 2026-08-12 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d668998-9ab9-32d6-9914-0e2ef34d1670 | -7.19219 | -44.36477 | 2026-08-12 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c534543b-0736-3706-ba06-936563e1f54b | -7.45468 | -46.15258 | 2026-08-12 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8e68c38-86ed-3c6d-887d-22b458000925 | -6.85652 | -46.00206 | 2026-08-12 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ac01a58-a3e3-367b-be34-276be3e5b979 | -9.13368 | -46.39029 | 2026-08-12 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ffa0344f-66a6-3c2d-8e87-456f916f23d4 | -6.34215 | -44.05958 | 2026-08-12 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70cc674a-a395-38c5-9725-95d14a7faf23 | -6.34159 | -44.06347 | 2026-08-12 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 24682c7a-b79e-3bc9-af99-d5e06775fed8 | -7.026 | -42.13279 | 2026-08-12 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| cd35d712-9505-3654-82c7-4bc1c99f3355 | -9.13435 | -46.3857 | 2026-08-12 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8580aa57-5901-3c81-ac03-e07a1ec0dca1 | -6.03909 | -43.86768 | 2026-08-12 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99b12a7a-716a-307f-9ab0-55f2e5e8051d | -5.8051 | -47.12774 | 2026-08-12 04:49:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 789ba1eb-bfe9-3603-9a78-abaae24586b4 | -6.54573 | -43.12215 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c4327756-082b-345d-b55c-992733132f2a | -8.60203 | -45.4067 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c209475b-bfe5-34c0-be8a-1ae3738f964d | -8.1129 | -47.18758 | 2026-08-12 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e8584ec-adfb-37f9-b5dd-338e2c90c540 | -9.02806 | -47.46951 | 2026-08-12 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8954b077-dea0-3b72-a309-1cc02a9c144b | -3.43185 | -49.48243 | 2026-08-12 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 908dbf0b-7806-3f64-9f39-6a3b324c7de7 | -6.33741 | -44.06282 | 2026-08-12 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de581391-d886-3968-8686-bdbc55844342 | -6.99523 | -42.62876 | 2026-08-12 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a5249dae-6cf1-3a7e-b4b6-e2f75ad87aca | -2.68598 | -48.20812 | 2026-08-12 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8561cda0-7fb6-3ba3-8098-59aae630796f | -8.54358 | -45.34383 | 2026-08-12 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26887f53-9873-3c24-a91b-850736ea0ccd | -7.74944 | -45.02362 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67aa71c8-ebfd-3520-9db7-2e470a4ee613 | -1.82745 | -54.50414 | 2026-08-12 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f631d52f-875c-3772-9d8d-2eb7cc047a63 | -7.61194 | -42.74605 | 2026-08-12 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1eff1aea-0996-3e60-bd05-e35f051b4618 | -2.80481 | -48.59466 | 2026-08-12 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 029c2c2c-9f07-378b-af24-ed55481d2342 | -7.00037 | -44.82688 | 2026-08-12 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8630743-ba43-3846-ad62-0007c6c566f2 | -4.76658 | -41.79961 | 2026-08-12 04:49:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cbd39c60-a4fe-3181-9b96-40eff7332417 | -4.11117 | -50.44837 | 2026-08-12 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62a06593-e1aa-3dad-810d-24118d5230d7 | -5.67945 | -49.82483 | 2026-08-12 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eaabe8a8-e79e-3602-a5e7-1c55e3c0686d | -9.1381 | -46.38632 | 2026-08-12 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce266ddf-f8fd-3983-981d-08d00d8b3542 | -6.99855 | -42.63885 | 2026-08-12 04:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9b3c622e-37f8-3b60-be48-faa1520dbb46 | -5.72864 | -49.13396 | 2026-08-12 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f32865da-26b7-3239-9136-a77865d85814 | -3.84493 | -49.03447 | 2026-08-12 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ca7d77e-d06a-3c4a-8a02-5852686845f5 | -8.48833 | -45.41891 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da801b12-5d7f-310f-9e26-9f8f28e16c5d | -4.46992 | -45.89936 | 2026-08-12 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10e0ad72-8b42-3af4-8247-57c89aebe5a6 | -8.35518 | -45.97727 | 2026-08-12 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0499a92b-f9de-3a8c-b04b-961c813d5e36 | -8.07831 | -44.84465 | 2026-08-12 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f9e3054-a091-310d-9d1e-17485e6258cb | -5.73975 | -44.50119 | 2026-08-12 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66933609-530d-3964-a1d8-139c83f72cce | -7.71867 | -46.21931 | 2026-08-12 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e41cd936-de69-306c-84d9-d5819c96967d | -8.60267 | -45.40946 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 11994f60-b716-3e6c-9fb9-a8cf199a68b8 | -8.78191 | -45.79193 | 2026-08-12 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87ead4f0-0de1-3c14-bb84-d1414436ada1 | -2.41918 | -48.63317 | 2026-08-12 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9fed2ac-5098-3480-a3e8-3a0410deffbe | -7.02681 | -42.13743 | 2026-08-12 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| f1a9c911-b4a5-388e-8985-46698b4aae5a | -3.05887 | -48.74079 | 2026-08-12 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3da5392-33d8-3ad2-a01e-f3416d1efbf8 | -8.36577 | -47.75073 | 2026-08-12 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| a7a9dcee-6131-374e-962a-59bdb2aea189 | -2.41946 | -51.83479 | 2026-08-12 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f187eb88-6e27-3b76-9a41-485c6969b119 | -6.5515 | -43.11397 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be36fffc-1da2-3654-8ca0-c8486bf2076b | -8.49301 | -45.41436 | 2026-08-12 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0c02d0a-72a3-3e81-ae4b-bab33ca9a9e9 | -7.39484 | -42.86679 | 2026-08-12 04:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b798a237-b235-3568-9bc2-89e255c2212a | -8.10996 | -47.18304 | 2026-08-12 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69a6ee55-e7a9-33b4-9933-0bb1e59601be | -6.99788 | -42.64351 | 2026-08-12 04:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb7995e2-9963-3d9e-9702-6123440c7a20 | -6.55084 | -43.11841 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d39823d-df93-3e08-9c15-1e0bd3efc0c1 | -7.39091 | -42.86132 | 2026-08-12 04:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43d43fa5-8e63-30da-a55b-3bb14e26ccc6 | -6.00944 | -47.41142 | 2026-08-12 04:49:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd174994-152f-374c-a8f1-ca5c3d8d7088 | -3.14926 | -54.60435 | 2026-08-12 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5084039-6f33-3397-bd3c-b46a01d470b0 | -6.54637 | -43.11776 | 2026-08-12 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ed30468-0b26-3072-ba92-446a0708187b | -6.59532 | -59.00879 | 2026-08-12 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f865f4a1-c03f-3a8c-b4e6-1c8ae63a280b | -3.02774 | -54.52537 | 2026-08-12 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2610beb6-c7e8-3f8c-8296-573d88c52822 | -7.03082 | -42.13351 | 2026-08-12 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| b8e29cb3-64be-3946-a550-29dbe23b911e | -7.38236 | -42.85521 | 2026-08-12 04:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6e8be22a-e4ec-3bb1-9f38-19113906561d | -7.72239 | -46.21986 | 2026-08-12 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de91dc58-6c1c-3fb5-b447-1647db32045c | -7.91949 | -45.11034 | 2026-08-12 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77fdccc2-1a38-3159-8937-513a3bc24bdb | -16.1015 | -49.8794 | 2026-08-12 04:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| f1c3db3a-acb8-30e3-ae68-8f94aeb62aa9 | -11.9535 | -46.3444 | 2026-08-12 04:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 029cc8c6-c36e-307b-acd7-c658832faac0 | -11.9527 | -46.3899 | 2026-08-12 04:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 22af75d9-0b92-3b25-b332-197cb9f01259 | -11.9539 | -46.3217 | 2026-08-12 04:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 56276ea5-67c9-3a40-a7b3-c5bf72619f1e | -13.29015 | -49.69574 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db48cd15-ddcd-3cc1-a815-e699473683ca | -11.78554 | -51.86425 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 07dd9ca3-2539-3d0b-ab2b-25605e0c91f3 | -11.48599 | -44.56865 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cbbca056-391a-3094-9741-bc97916c025a | -13.53009 | -46.28853 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 166d6949-d775-38c6-abb0-4445f1c6a1e1 | -10.89437 | -50.17231 | 2026-08-12 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b878df9-a48f-3ac6-984b-0f4dae5aeeb1 | -13.05519 | -52.71652 | 2026-08-12 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a6972b1f-9142-3b00-b317-377203a5b4f6 | -8.9526 | -60.5535 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a78302b1-9347-38d4-bff4-9e7141a3317a | -9.33654 | -47.52167 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c876cb72-cc78-390a-866f-bfa24a74c508 | -10.10146 | -46.20902 | 2026-08-12 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4262ab9a-64d3-35ef-b4e5-23ec7dd2bbd8 | -9.34438 | -47.49404 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a92d90c9-b270-39db-b474-e88934c5a44d | -11.9548 | -46.35204 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 815cd400-b2b6-347e-acfa-2cafcbde84be | -11.97562 | -49.55934 | 2026-08-12 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de9f51b4-8166-3611-874d-b370e8e2b608 | -13.83933 | -53.7853 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce2c000c-1f76-31ea-9279-e3ff2f310db0 | -9.37016 | -47.44427 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4c34a64-afbb-37db-8217-a7008a04b58e | -14.49749 | -49.30025 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README18.md)
