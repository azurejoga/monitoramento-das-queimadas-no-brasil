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
| 3fb6bfe4-655c-34ba-8def-2ae835480644 | -8.9041 | -60.5577 | 2025-08-07 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 5c33f9ca-4ab0-3f65-a285-76db89de638e | -7.4074 | -60.0108 | 2025-08-07 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 82c755d3-88ad-31cf-82ca-1d7564825ebb | -8.9399 | -60.7481 | 2025-08-07 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| c419624b-0df0-37a7-a609-c58bc0133d89 | -4.1899 | -38.37355 | 2025-08-07 03:36:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| abf0bf6b-4416-3f39-879f-7bc7c796b759 | -3.82419 | -41.55916 | 2025-08-07 03:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 876b73a8-54e5-37fa-9f65-54d9cc6447a1 | -3.8247 | -41.55607 | 2025-08-07 03:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ab4357d7-b546-352b-bbcd-e7c8fbc5aae2 | -3.82368 | -41.56224 | 2025-08-07 03:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 17f24128-452e-3f67-ad22-bca83da8ec49 | -3.42792 | -43.1517 | 2025-08-07 03:36:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f2eea21-f899-3d71-94fe-14e10d30b7e9 | -3.8216 | -41.57474 | 2025-08-07 03:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5b883338-43e6-37c8-bf13-ade1442a42ec | -3.82212 | -41.5716 | 2025-08-07 03:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1b408e3c-f784-3b40-9f3d-35b33438d726 | -3.42725 | -43.15568 | 2025-08-07 03:36:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4498d673-a7bc-3fdb-a546-9e9ed0b5304e | -10.42814 | -44.40133 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0489472e-6f5a-3f7f-b28d-0db7c5101074 | -10.42256 | -44.40023 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcee5900-1c9c-3785-8699-271989dff6b0 | -10.63945 | -44.74296 | 2025-08-07 03:38:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7dc801b-5cff-3fa4-bf11-55f5f6386b59 | -10.42042 | -44.40081 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 507824ba-a7f0-3a75-9d4f-fdaeb75799eb | -10.43533 | -44.38367 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 44823eff-536a-35c3-8db3-58de7455140e | -10.43721 | -44.40382 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6c2c0896-9101-36e1-8dda-33c763d2cf0e | -10.43032 | -44.38966 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6329f48b-8356-3214-a421-70a245514f5a | -6.44714 | -46.11269 | 2025-08-07 03:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb14a87e-b4bf-3177-9902-8d6cb097ffba | -7.27738 | -44.31974 | 2025-08-07 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 66fe61be-2af3-3fbe-abf9-0821d605a8cf | -10.62653 | -44.74876 | 2025-08-07 03:38:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fe68ad0a-96b6-3b8d-b699-d99f77f26bf4 | -10.4313 | -44.37465 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c08f77a0-6ec2-388f-b34e-08a4a282d44d | -9.08633 | -45.0683 | 2025-08-07 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a06ad1-cbf2-32a1-af28-350294491fdd | -9.64874 | -43.84528 | 2025-08-07 03:38:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4587d350-b064-363b-8461-9918942f77ef | -10.4296 | -44.39352 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e8f8ece-b475-3603-89f1-ebd579515851 | -4.77762 | -45.32824 | 2025-08-07 03:38:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf653f28-42a8-3c3d-96c4-baf8ad95370e | -10.43446 | -44.39845 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0b45d26-4d37-3b37-999c-ab0b0cd84547 | -7.27566 | -44.32912 | 2025-08-07 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 87f2cd1f-d79d-3de7-abe3-0ff6f9700f63 | -7.23787 | -44.63654 | 2025-08-07 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b604003d-efa4-3b44-a398-e5615e9232a0 | -6.4452 | -46.10715 | 2025-08-07 03:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c218213b-3ea1-3ba4-ad05-aeeb297b177d | -9.64804 | -43.84903 | 2025-08-07 03:38:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 50ffa5ef-860f-3a18-b44a-3ea09dc09e47 | -10.4361 | -44.37971 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3e27368e-c205-3f20-aba8-32a4e1e54a0a | -6.44166 | -46.10524 | 2025-08-07 03:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2012c645-d809-37f3-9333-f796cb8fec87 | -7.90789 | -45.53737 | 2025-08-07 03:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 806793ac-90e4-3ab6-9f07-4f2aca503b67 | -4.77213 | -45.32736 | 2025-08-07 03:38:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48abbe95-063b-3cda-a64c-35fc03fc45be | -9.30173 | -40.23952 | 2025-08-07 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| cd66780f-fee3-3b5f-b3e5-546bc6568dfe | -8.97517 | -40.6182 | 2025-08-07 03:38:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6d7a8cb1-360b-3be2-a0dd-609bb7083cf5 | -10.43734 | -44.38302 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45508924-0efb-3970-8cf8-2ed7f4a8214f | -11.28056 | -40.97429 | 2025-08-07 03:38:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d2cfead-4ef2-3f35-a723-8366ff3b30af | -7.18858 | -45.48619 | 2025-08-07 03:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1d29cfb2-c1ff-3943-90f5-4779d53bff7f | -10.42329 | -44.39635 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6c89a61-924b-337a-83b6-4c5aacb1aae3 | -6.44051 | -46.1115 | 2025-08-07 03:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92887ce9-8358-3985-b29b-1ca77ef11f3b | -10.43176 | -44.38198 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f69db7b-5092-3c7a-94bb-338ba1c1ecca | -7.39508 | -39.68325 | 2025-08-07 03:38:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| acbb58d7-9042-3d8d-9b8a-6826c9162a40 | -10.42192 | -44.39312 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e6a2e9a-2af5-332d-8c8c-8511721b5676 | -10.62807 | -44.74077 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7e61db77-204f-3775-8268-7a4ce4baf1ae | -11.28055 | -40.97594 | 2025-08-07 03:38:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 190ac936-fc88-3aa8-8a39-4bb11265bb77 | -9.61401 | -39.01488 | 2025-08-07 03:38:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 370e874d-ee53-3bb9-8c83-8b191ad8ef70 | -10.43589 | -44.39081 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36e3326d-ba0b-39f9-9008-6d1648af034c | -8.51942 | -43.30979 | 2025-08-07 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 15835827-ca3b-3a45-8744-2ba478c98fb2 | -10.43866 | -44.40696 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4499cbdb-a98e-3b28-9f72-ba4a4606f2fb | -4.77867 | -45.32825 | 2025-08-07 03:38:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bda0774a-27c0-3e76-ab99-c1fb66931905 | -10.43383 | -44.39139 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e496e7ea-3b7f-34f8-aeb4-40c208c4c725 | -9.55707 | -40.34756 | 2025-08-07 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 5cfb9659-4454-3487-82ff-b55682d2884e | -11.40279 | -41.71548 | 2025-08-07 03:38:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 04732159-973f-3269-9016-23720862128e | -10.4381 | -44.37895 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3de6b07b-a6c1-36ac-89fe-de220e7fcb5d | -7.91415 | -45.53853 | 2025-08-07 03:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da92de52-cbad-31a6-8472-a4f69506ed04 | -8.52005 | -43.30639 | 2025-08-07 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a58ffa46-a32a-34de-ad42-829982c46bbe | -8.52067 | -43.303 | 2025-08-07 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 59cdcbea-a7c7-3153-bfb5-79682dae9cfa | -9.55636 | -40.35174 | 2025-08-07 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 66fda771-def7-3315-b02e-035cd3412b5e | -8.32901 | -38.09015 | 2025-08-07 03:38:00 | NPP-375D | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 30f3e826-7fef-3067-ae50-a21493f9c641 | -9.0828 | -45.0543 | 2025-08-07 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a17a4d65-0ff6-3444-b2d4-6eb5bfa596cf | -9.55818 | -40.34595 | 2025-08-07 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 26.7 |
| a3f28918-7e9a-3b53-9ffb-2878e571d0e6 | -5.3828 | -36.90452 | 2025-08-07 03:38:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b927452a-6d82-3529-8772-306318f6ecc5 | -10.27766 | -40.81285 | 2025-08-07 03:38:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 35fbecb0-8532-3ac0-aa51-ca4073e56352 | -11.40368 | -41.71067 | 2025-08-07 03:38:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 87536a2d-ec0d-3097-a071-69460f66c016 | -11.28496 | -40.97501 | 2025-08-07 03:38:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36710013-9e44-3f6c-abb4-00b9bb21c531 | -8.5153 | -43.30199 | 2025-08-07 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ec5eaeee-81d2-3363-b9b7-add9a6a96135 | -10.63376 | -44.74186 | 2025-08-07 03:38:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 145ff2b6-91e1-3a48-a4b4-1583b7130171 | -10.43158 | -44.40295 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3d9bfa6e-522d-39c2-bb73-a41d6ed6d8d7 | -6.83819 | -46.39132 | 2025-08-07 03:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83f3309e-7fff-3137-b4ca-1087b6cdcfa9 | -10.43374 | -44.40231 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7900f83-4c55-3265-a3e7-e760753d39b6 | -10.62841 | -44.76968 | 2025-08-07 03:38:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a84e17ce-0877-30d3-8d9b-bec52815992a | -7.91506 | -45.53368 | 2025-08-07 03:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90138c3c-ec79-3f0d-b16b-d2aa647e4044 | -10.43794 | -44.40004 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7aef4599-a864-3d24-92fb-a6ba245aa7c6 | -9.56212 | -40.34417 | 2025-08-07 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 93c3278b-6dd8-3e78-b25b-3ff9ba3df981 | -10.42887 | -44.39742 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9e3c08e-2cd8-3124-81ea-8fb6797de437 | -10.64359 | -44.75209 | 2025-08-07 03:38:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3b4d9bb-52c6-3bbf-b206-c945819fa829 | -10.42266 | -44.3893 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7ce5e814-310e-3118-9135-035e58d312b9 | -10.41916 | -44.38754 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65e7b1cb-5439-3bee-b614-da0aba16e407 | -7.18323 | -45.47979 | 2025-08-07 03:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04a1705a-7819-3569-bc27-322f248ff23d | -10.43518 | -44.39462 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 486288db-275f-3360-91a5-9ae9ff97c6fb | -8.5213 | -43.29961 | 2025-08-07 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f6340eb8-1116-32f5-8d8f-78558dec7661 | -5.1559 | -39.51033 | 2025-08-07 03:38:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1c685192-d5a2-3d5d-ab11-bae5980716e2 | -9.55779 | -40.34339 | 2025-08-07 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| cabb4571-b1a5-342d-88a5-24d02763683a | -10.44578 | -44.38944 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27ffd33a-d9bc-36e8-9c8b-cc8c3cb20454 | -10.41845 | -44.39131 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2663a95-2597-33f1-8dcc-d30456628f78 | -8.51593 | -43.29859 | 2025-08-07 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 11c5c99d-8fb5-36e8-831f-12d058ce9ce3 | -10.4275 | -44.39415 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 565c0b90-0afc-3202-84fd-287545118937 | -10.62919 | -44.76564 | 2025-08-07 03:38:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8665006f-bacc-3e31-afc1-113d022da638 | -8.51655 | -43.2952 | 2025-08-07 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8cbf7dcc-0e73-3ac8-af6e-e42ac467dacc | -7.18227 | -45.48503 | 2025-08-07 03:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0561db16-8a8f-365d-8456-0a35a4a8ed64 | -10.43326 | -44.37392 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a9835a46-1f85-3a88-abae-bb85abe68902 | -10.43934 | -44.40328 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 690897de-aa72-3552-a285-fc6cd43b2022 | -5.15518 | -39.50929 | 2025-08-07 03:38:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 313e717c-3af0-30c1-b121-8ed1b4979db1 | -7.91322 | -45.54348 | 2025-08-07 03:38:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b81ab177-65bf-39b5-b8cd-eac7f00e90a4 | -9.06928 | -45.06053 | 2025-08-07 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b7fd989-e6a4-3477-a686-a484b27f97e1 | -10.42473 | -44.38863 | 2025-08-07 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c9795b8-dee5-3213-8461-cf51cea1a9be | -9.65342 | -43.85051 | 2025-08-07 03:38:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| beaef25b-a3a4-3f73-9391-ba6dd97cb21e | -8.97735 | -40.62113 | 2025-08-07 03:38:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |


[Clique aqui para ver as próximas entradas](README6.md)
