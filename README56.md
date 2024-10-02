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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf1673d8-49bc-3b34-ac40-df61352df66c | -23.35363 | -47.01243 | 2024-10-02 03:34:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 870e9d50-1a53-306e-8216-e75adafc3df4 | -23.35278 | -47.0213 | 2024-10-02 03:34:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 148db69e-1008-35d4-ba5c-a5ed831bbaa7 | -23.35266 | -47.0167 | 2024-10-02 03:34:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 95caada2-8382-3b58-a1fa-707bf5ed5ae6 | -23.35163 | -47.02121 | 2024-10-02 03:34:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 03920778-ac9c-3a7b-9fc2-aab3cdb0e13e | -23.35157 | -47.02643 | 2024-10-02 03:34:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 341624cb-1b1c-3558-b1c6-d2820eced438 | -23.28379 | -46.66172 | 2024-10-02 03:34:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a34ea7f7-3e48-3323-82d4-5a34e7bee70f | -23.28288 | -46.66574 | 2024-10-02 03:34:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e978ff03-9573-38c1-9cda-3048c45998c8 | -23.27928 | -46.65586 | 2024-10-02 03:34:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ede98c29-b46f-3bea-995e-f7730d8084e8 | -23.27838 | -46.65982 | 2024-10-02 03:34:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 6805e995-6d7e-3639-8a06-0dfb419adad6 | -23.27742 | -46.66399 | 2024-10-02 03:34:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| f00415ac-6cee-35b7-88bc-3a5a017847c2 | -23.2746 | -46.65076 | 2024-10-02 03:34:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| da9209d5-c916-33d7-a372-f57ae98ff03e | -23.17144 | -49.59887 | 2024-10-02 03:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| a025fdfa-2f67-3475-b638-734c95e5da19 | -23.16759 | -49.59606 | 2024-10-02 03:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 8174a42c-9b0d-3f86-9d18-c1bfe3b96a00 | -23.16497 | -49.59691 | 2024-10-02 03:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 38f69f07-efc9-37d6-a89a-629fc9b4ba63 | -23.16427 | -49.60954 | 2024-10-02 03:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 347b6fa5-8288-39ce-a5c8-23071a57e337 | -23.16338 | -49.6032 | 2024-10-02 03:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 8005b8ab-bcd3-306b-9cd9-10dedd9a68c0 | -23.16164 | -49.61002 | 2024-10-02 03:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 40129c83-a306-3819-bc4b-56872b8beb97 | -23.15951 | -49.60061 | 2024-10-02 03:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 762a2616-ef2e-3e14-b1ec-02cd5a9839f0 | -23.1579 | -49.60715 | 2024-10-02 03:34:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d8d5b772-02a0-362a-8c49-8f2d1e978c58 | -23.11526 | -46.2662 | 2024-10-02 03:34:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b661e403-4393-3b92-90a5-0dd2fd419120 | -23.03781 | -46.88773 | 2024-10-02 03:34:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0f9542d1-da31-37f4-8e27-3a8658323807 | -23.0323 | -46.88574 | 2024-10-02 03:34:00 | NPP-375D | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 3365490c-983d-3bac-8414-7c2186126a98 | -22.93891 | -43.23898 | 2024-10-02 03:34:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e6977be4-be9b-3600-a6f1-12cf9f29e059 | -22.93175 | -43.73006 | 2024-10-02 03:34:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 322a2da0-9a8b-375b-8eb2-e217810c0e68 | -22.93064 | -43.73536 | 2024-10-02 03:34:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 0c2c673b-38d2-3b07-b7c4-4660264fa88b | -22.92709 | -43.72891 | 2024-10-02 03:34:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| ef52095e-d9d0-3c08-b738-28c24c0283ec | -22.92354 | -43.72245 | 2024-10-02 03:34:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 7951d1f5-df83-3c98-af0c-821cc9e39497 | -22.82918 | -42.70614 | 2024-10-02 03:34:00 | NPP-375D | TANGUÁ | RIO DE JANEIRO | Brasil | 3305752 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ba0e1c21-761e-33b8-9fa6-675aea5d755e | -22.82519 | -42.11077 | 2024-10-02 03:34:00 | NPP-375D | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 727c3523-c36d-320c-add0-437d6e6e4cf6 | -22.78669 | -44.25098 | 2024-10-02 03:34:00 | NPP-375D | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0cf15f52-4dde-368d-bbd5-39b54d35665c | -22.78194 | -44.24945 | 2024-10-02 03:34:00 | NPP-375D | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 345e871d-6415-3ab6-8686-5334ed1d2a38 | -22.77449 | -44.23685 | 2024-10-02 03:34:00 | NPP-375D | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| ac23db5c-f8e8-3fa1-aa05-b474f796bf1e | -22.77348 | -44.24154 | 2024-10-02 03:34:00 | NPP-375D | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 79040731-9968-3205-b18f-8159e1282773 | -22.77302 | -43.80462 | 2024-10-02 03:34:00 | NPP-375D | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 9be5a166-9714-3ca2-979c-53ba509f84a5 | -22.77269 | -44.23563 | 2024-10-02 03:34:00 | NPP-375D | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| a04f6fdf-55a6-30a6-9e75-36f97b36e65f | -22.77172 | -44.24029 | 2024-10-02 03:34:00 | NPP-375D | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 866b2e70-cb3d-3bf9-883f-fbcc1f81a4a3 | -22.76977 | -44.23522 | 2024-10-02 03:34:00 | NPP-375D | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| f961088c-a81e-3262-9400-eefa4f88af7e | -22.76941 | -43.79837 | 2024-10-02 03:34:00 | NPP-375D | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| bfdc2af1-84ae-326e-a0bd-701f45b05b22 | -22.76842 | -43.80301 | 2024-10-02 03:34:00 | NPP-375D | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 99903112-74fe-3f03-a876-f9b086435d6c | -22.76793 | -44.23416 | 2024-10-02 03:34:00 | NPP-375D | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 118cdcba-08bd-382a-9887-a0a754885297 | -22.76671 | -43.76453 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f2e2bc5f-8826-314b-9adb-4873c430d065 | -22.76571 | -43.76923 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 99c3b778-181e-3f9f-aac0-d8fb4ca44969 | -22.76542 | -43.76765 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 45b1ba13-1cf4-3b18-8d6b-6893c1d59c4a | -22.762 | -43.7635 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 344a4942-8da7-3e70-ac66-e9eaa561df54 | -22.67363 | -43.71 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2970e80a-140e-3ef5-ad54-e4c11c3e83de | -22.67348 | -43.71288 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7a1eeef3-89d7-39ca-afd3-084cd39fa78e | -22.67241 | -43.71599 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c4357898-abe8-38cd-bf67-f846a65245c5 | -22.67019 | -43.70278 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 641bc420-42da-3a9f-a344-435f2cb077bf | -22.67006 | -43.70578 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c6d76c08-e07d-3317-9f0d-ec5adda54eb2 | -22.66894 | -43.70892 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 53320fb6-6ab4-3188-b843-529d9ff3cca1 | -22.66874 | -43.71202 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fa0f8dc7-b20c-30b5-a2e1-5acde37db72b | -22.6677 | -43.71502 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 86616f1d-ba9b-38e2-afd2-32724ad9a6a3 | -22.66538 | -43.70227 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 95208aec-05f2-35f1-8c89-46222ddddd50 | -22.66525 | -43.70526 | 2024-10-02 03:34:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| a4e79e73-4115-371e-87d2-d036a9532c20 | -22.65322 | -47.26839 | 2024-10-02 03:34:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55c01c79-a120-3108-ae35-b45bc2dd55aa | -22.64954 | -47.26455 | 2024-10-02 03:34:00 | NPP-375D | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bcb9f26-2041-3f95-86ad-5addc063c32f | -22.64853 | -47.26898 | 2024-10-02 03:34:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3ad136f-cd2e-388d-9eb4-4b1f8e0e04f4 | -22.61613 | -43.96635 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0f891316-e203-3b16-9757-429216ddffbb | -22.61546 | -43.96272 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 16b0b90e-8be2-327e-9fc5-318464319504 | -22.61252 | -43.95963 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 98bbf06d-6543-3ae3-8426-2ee6bb6c9ac2 | -22.6114 | -43.96505 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fd0732fb-9ae0-3fbb-bc93-f0cd7dc41274 | -22.61074 | -43.96142 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 44f2e7cc-10c5-3ad9-81c1-920d2c411218 | -22.60958 | -43.96683 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9560d05d-40ec-3f06-b1e4-6eee37e09047 | -22.60665 | -43.9638 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 38d9e37d-f50a-3247-bb6b-f447f29222f3 | -22.606 | -43.96017 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 058fa9eb-b785-34a9-bea0-7d5337bd46dd | -22.60484 | -43.96559 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| baceb8f3-ac73-3573-8239-a1e9bf4e7a4a | -22.60456 | -48.76908 | 2024-10-02 03:34:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 920914b5-986f-35a3-bb21-2b5b859ad45b | -22.60322 | -48.77448 | 2024-10-02 03:34:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dca0e44-5e84-33df-a3a2-74fe5df1087b | -22.60301 | -48.77004 | 2024-10-02 03:34:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea8d6da1-7011-31af-964e-8b09b370c5ca | -22.60171 | -48.77544 | 2024-10-02 03:34:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c745bf7-659f-3edf-b698-43dad2ec95c7 | -22.56018 | -42.41747 | 2024-10-02 03:34:00 | NPP-375D | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1c456a67-a4e9-3451-945c-c4236e7f3444 | -22.55696 | -43.82009 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 46bc44c4-a92c-34a4-a938-e9c80afe73ef | -22.52442 | -43.54859 | 2024-10-02 03:34:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| a00f733f-f246-342c-a8e5-a42a5d548e63 | -22.5141 | -43.83608 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 0943c40a-04a9-38bd-98e8-a1fdc344d082 | -22.51352 | -43.83745 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 9c271f75-725f-3f18-8dbd-e0a9d664b482 | -22.51303 | -43.84127 | 2024-10-02 03:34:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 61274c28-6e81-3d5b-8d97-72997de47021 | -22.5094 | -43.83478 | 2024-10-02 03:34:00 | NPP-375D | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f1aad9e4-79d6-3efb-8fa4-a12e96a74fad | -22.50051 | -43.5462 | 2024-10-02 03:34:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8fe3d2c1-2568-3994-8044-4be3d785f20a | -22.49952 | -43.55092 | 2024-10-02 03:34:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 54be2a21-fc06-3c41-9d35-71bd5c42a7bc | -22.49494 | -43.54949 | 2024-10-02 03:34:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2fdd1e57-d06a-35fa-85e4-1c8185ea92fe | -22.49221 | -44.14923 | 2024-10-02 03:34:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 96d6440f-08cd-3b25-a1dc-1ebf2b9a4772 | -22.4874 | -44.148 | 2024-10-02 03:34:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0683c02d-1ab0-3570-99ae-a5ea0ed71e2e | -22.48622 | -44.15351 | 2024-10-02 03:34:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2adb68d2-4795-3ef7-91f2-1bad3c57fa56 | -22.48009 | -44.13467 | 2024-10-02 03:34:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f796975-5bbe-3c7d-8eb2-bc3d92c35b41 | -22.45612 | -44.1282 | 2024-10-02 03:34:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c3876d4d-ab6a-33c2-b094-d96afec99b2f | -22.45273 | -44.13206 | 2024-10-02 03:34:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9903f54c-64e9-36f3-b479-fdbd2dd855b1 | -22.45128 | -44.12712 | 2024-10-02 03:34:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 00810323-ec92-3ea0-b3cf-409c05c6e165 | -22.45005 | -44.1328 | 2024-10-02 03:34:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| baeefa9c-cec0-34f6-b828-fa464e7982f6 | -22.40044 | -49.31881 | 2024-10-02 03:34:00 | NPP-375D | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3170cdbb-02a2-37c0-b411-0a97c1701f8a | -22.39894 | -49.32483 | 2024-10-02 03:34:00 | NPP-375D | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ec91b915-9916-3a4a-a156-200f86f11e0d | -22.39323 | -49.30075 | 2024-10-02 03:34:00 | NPP-375D | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| df79c914-4586-3fa3-bba4-47cedfbc241a | -22.39181 | -49.30662 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| a2700480-e94e-33c8-a458-2e3085bbf056 | -22.39181 | -49.29763 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| afec7b73-126e-399e-8950-b49b1483fafa | -22.39035 | -49.30349 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| 4880a836-dc0c-3778-ac63-002ef1c6bf88 | -22.3896 | -49.28714 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 7db8f7fc-adb7-3ad3-933f-2e13c40d8801 | -22.38893 | -49.30918 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| 6d1332ed-3a46-38c8-a046-8a08f303711f | -22.38828 | -49.28397 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 70937a54-ad1b-3674-a3f3-cde176d85b8e | -22.38812 | -49.29325 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 63d22f0b-385e-339c-b4e7-78881c39020a | -22.38752 | -49.31484 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 017b192e-44e9-350e-990f-6a6df1ab0877 | -22.38673 | -49.29016 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |


[Clique aqui para ver as próximas entradas](README57.md)
