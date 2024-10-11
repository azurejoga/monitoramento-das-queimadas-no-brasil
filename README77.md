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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b0dadfc-c26e-32ad-a401-7f721dff2fc9 | -2.38984 | -50.41342 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ada679a0-2153-3305-bd85-e7042641f2da | -2.38974 | -50.4103 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d100d2f0-3de0-31be-9ae2-ca0f9537a311 | -2.3796 | -50.31983 | 2024-10-11 05:16:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b83eb4e6-14d9-300e-b503-e7798a1ed02e | -2.37878 | -50.32518 | 2024-10-11 05:16:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db00b13b-a932-3e01-8aec-5ab97dd96e86 | -2.37394 | -50.32441 | 2024-10-11 05:16:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ba0a4d5e-558b-356c-9e31-e0cc957ae120 | -3.26998 | -49.09695 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba3de0b9-fb82-3bc9-bb59-a29156aa38cc | -3.26949 | -49.10032 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ea3710f-e195-3fee-a200-63a861c38fee | -3.26899 | -49.10369 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b633c73-bfdd-3779-898e-6b817e189480 | -3.26416 | -49.09941 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55741fc6-521d-3e65-ad32-18316f2bf3f0 | -3.26367 | -49.10278 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb568003-264e-350c-9c07-581bed202239 | -3.26317 | -49.10616 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1c45eff-b800-329f-8955-8eb95e504b00 | -2.95938 | -49.20169 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a85adb74-3da5-3363-be6a-a8da7ff58d1f | -2.95889 | -49.20495 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b7c0d74-7f89-3329-8ff7-9ca0e4e3ce97 | -2.78501 | -49.25302 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c06ef93b-2a01-3deb-896c-bda4120d02c4 | -2.7807 | -49.24581 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9654625c-5f54-3b91-b7fd-3502bfb55b15 | -2.78059 | -49.24623 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 298f8ffe-422a-3c82-a967-0d8af575fcce | -2.78023 | -49.24898 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d04d5c7c-b4cc-3add-a43e-63db405411c4 | -2.78011 | -49.24939 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0349a013-0ff6-335b-9b9d-a8a7246d1adf | -2.77977 | -49.25218 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f254d27f-5971-3d30-8677-d5d60efed757 | -2.77962 | -49.25255 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5812fd48-824a-30a8-aa07-f38a53fa7a27 | -2.7793 | -49.25536 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 080ca222-ca4a-3520-bd2b-450efd025e02 | -2.59968 | -48.95285 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 334c24de-89af-339f-95c7-43041b32f928 | -2.59916 | -48.95619 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c518f6b-a784-3d8b-9d91-1c775fdc5e5e | -2.57512 | -49.07776 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26701901-687e-3e8e-bf33-ed49b93d702a | -2.5746 | -49.07533 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 332d3d1f-11fa-3192-aa89-2a5f2c3a8094 | -2.49962 | -49.14914 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1382565-a1ac-39cc-87b8-0533ca06235f | -2.49915 | -49.15235 | 2024-10-11 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ca968f0-14d6-37c9-a389-fc6583834b52 | -4.43686 | -50.54166 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85685869-4e9a-34e6-ba9f-49cfb80d2e70 | -4.43607 | -50.54716 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67912cf3-88fc-3ff3-a68c-299e061e56c7 | -4.38769 | -49.82569 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| be08d2fc-2542-3d73-940d-5d1541b607ec | -4.38724 | -49.82879 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d52a0769-bb0c-3bde-8d20-3c9f05d3ee4c | -4.34885 | -50.50941 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df17dc53-3a77-3fc4-ae7d-c562f932469d | -4.34392 | -50.50869 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 165d9ece-c14d-3ba5-b4d1-9e6a3e889fee | -4.14238 | -50.41402 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41166486-f17c-33c9-bcc4-2fd1724c7558 | -3.91392 | -49.69187 | 2024-10-11 05:16:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1ec30db7-4c73-3e42-ae9c-86f9a817a8b8 | -3.91343 | -49.69527 | 2024-10-11 05:16:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 622ff5f8-373e-3dc8-a5d6-6add878edbb5 | -3.90876 | -49.69093 | 2024-10-11 05:16:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6f9f15de-9f6d-3a6f-8a6a-a7735e47f3d8 | -3.90827 | -49.69434 | 2024-10-11 05:16:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 919f7174-841d-3d05-9671-9b62c87baaaf | -3.69257 | -50.12472 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29f496c3-fc14-399a-ae71-ec39af092300 | -3.68887 | -50.11516 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 89c680bd-5b7b-337b-aac0-e86cb933fa27 | -3.68843 | -50.11812 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 35294193-b743-37df-990a-88983ddfcef0 | -3.688 | -50.12105 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 51b0dadd-68ca-3914-a491-c7d0afbcb160 | -3.68757 | -50.12393 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ff9974d-74f6-3ef5-aca9-22c6c71aaa1e | -3.68344 | -50.11721 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18f2ff34-f57c-35ed-a609-fb7ecc3ecee7 | -3.68301 | -50.12012 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 223845aa-ed65-3155-a9ca-18fdaecf40fd | -3.67869 | -50.04518 | 2024-10-11 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48bf4f74-fbbd-3f5b-b90e-f9c18c553576 | -3.65897 | -49.62781 | 2024-10-11 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50def517-2ca5-30c1-bd4b-f15cab242b6d | -3.65851 | -49.63089 | 2024-10-11 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b10de912-253b-343a-b5d7-0c28abedbdda | -4.99506 | -50.43378 | 2024-10-11 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8aec5e8b-b995-3f6b-bb49-c12f7c04ba31 | -4.99465 | -50.43668 | 2024-10-11 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e353199a-6be7-33ac-aeee-0f804bcd2221 | -4.94998 | -49.76403 | 2024-10-11 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a755f86-078d-33d1-bad8-e6db29493ada | -4.94951 | -49.76722 | 2024-10-11 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8961b88-19b7-3d59-b323-8a9c04131b99 | -4.8854 | -49.91568 | 2024-10-11 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ece490f-9800-35f2-a4ce-8d750c5bc57a | -4.88025 | -49.91475 | 2024-10-11 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 521911ef-f272-31a4-ac5f-ed4e264a156e | -4.85312 | -50.67584 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9dbc8341-3f3f-3d6f-8d26-b9d39c2beef9 | -4.85233 | -50.68132 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68f5ed4b-3255-31f6-910b-a14d1b708545 | -4.84707 | -49.88784 | 2024-10-11 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89eda358-4260-354c-8424-335190a37aff | -4.84189 | -49.88705 | 2024-10-11 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ed92c6b-142c-31df-b145-40c48e649dc9 | -4.84146 | -49.89012 | 2024-10-11 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31d21447-061d-3fa0-9bf9-6b1c79a3e9cb | -4.83592 | -50.79602 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a5437761-a18b-3776-bc6a-612145723854 | -4.83182 | -50.78989 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b3e691a7-6d4a-335f-8337-f7f8c832e872 | -4.83104 | -50.79542 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 76b92565-1d2e-3d14-af3e-001d03a0a016 | -4.83027 | -50.80074 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f90649f2-f7a3-37a7-a2d6-55aa6546b2bd | -4.82945 | -50.64923 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f5d0fc4-95f4-391e-891d-7ff63187232c | -4.82618 | -50.79462 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d5222cc0-1bf1-37e5-8a46-325acda36c35 | -5.99816 | -49.67631 | 2024-10-11 05:16:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61a18024-3a6f-3b75-a83e-37d8a7a31f09 | -5.55543 | -49.58076 | 2024-10-11 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b428a6af-17af-3642-b8fc-2ee87bf95837 | -5.55495 | -49.58417 | 2024-10-11 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3729a60b-29a1-301d-a817-832ed2746b2b | -5.55471 | -50.4227 | 2024-10-11 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3237896-0ad7-3de2-afd3-f6bbc5b23e5c | -5.5543 | -50.42559 | 2024-10-11 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cff26467-bce6-36ef-beaa-fc049d4d6f1b | -5.54966 | -50.42195 | 2024-10-11 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60fa856d-52bc-30ca-81a2-5bedd5599a4b | -5.54961 | -49.58337 | 2024-10-11 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ec05abe-1f7d-33fa-828e-e4f14cd2aed3 | -5.54925 | -50.42486 | 2024-10-11 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7def06d1-de7f-38a7-9de8-cf2dedb7b551 | -5.53812 | -50.99049 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 368ac16e-2992-3956-9851-ecd06d59a18f | -5.53653 | -50.99111 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4416192-0e0a-35e9-9fbe-f0364405d7e0 | -5.53328 | -50.98973 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97f9bd22-8d9e-3a2c-87d2-6da192861a14 | -5.46668 | -49.60479 | 2024-10-11 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d01ccbc7-2be4-3ea0-a650-18af08af513d | -5.46621 | -49.60809 | 2024-10-11 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbd8af2e-7be4-39fe-8bd0-001e82ee9f1a | -5.34526 | -50.83751 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd8526c9-0c08-3b90-a02d-2bd98d7e62b6 | -5.34275 | -50.83907 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fa8bb91-0399-380b-a9a1-bc55fce9a7d3 | -5.34061 | -50.96026 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dc4d831-921b-3643-8a85-7bb9c0438c60 | -5.34016 | -50.99836 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9dd58836-4f12-3fbc-945d-0fb54378826f | -5.33533 | -50.9976 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd5934c8-d143-3cac-bb60-a4014b09c24f | -5.31079 | -50.96994 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5036997-f2c7-31e7-a793-af309f171b4b | -5.30931 | -50.9718 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fae4906-89c4-3845-921e-3a9806ecd33d | -5.28834 | -50.9882 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c943e28a-acf6-38c4-8f52-8aa1bdb80022 | -5.28816 | -50.9555 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 610b8061-53bc-38fd-a666-5cd7a1cac52b | -5.2835 | -50.9875 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f81fa29-10d9-3652-a677-d32fed30de56 | -5.2833 | -50.95488 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd89e211-fe15-3ae1-b53a-a918bdddb80a | -5.28274 | -50.99273 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e033e128-0fac-35cb-834e-036217b16565 | -5.28252 | -50.96022 | 2024-10-11 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7c87307-dace-34f8-a1d9-641e784e7338 | -5.17428 | -49.92704 | 2024-10-11 05:16:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fbda5de-f4a6-3255-9da3-c6c470daff42 | -5.06191 | -50.75524 | 2024-10-11 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a584e6d-60e3-348a-b875-833178f12684 | 0.02716 | -51.35559 | 2024-10-11 05:16:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c81f48f-dc69-32bd-a1ff-741093401483 | -2.14503 | -50.89469 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f42dc186-4df5-300b-bf5a-c3d373514492 | -1.97798 | -51.09961 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9efa97ec-e08b-38c4-9ddb-f1037990edb3 | -1.97342 | -51.09891 | 2024-10-11 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81568f6e-ca90-32d7-bd1f-b7e92a0b4b39 | -3.55647 | -51.59587 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6874e7c9-350e-3a63-98aa-4e0663caa6c3 | -3.5558 | -51.6004 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63b9502f-eba1-3c6d-8f8c-681161f3dcdd | -3.51062 | -51.36856 | 2024-10-11 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README78.md)
