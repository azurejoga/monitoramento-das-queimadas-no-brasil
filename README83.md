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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1dceafb-b651-30df-b53f-aa2648bfcbd6 | -2.86371 | -52.91254 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 838f5850-d084-3600-9fd0-77ca47c18cb5 | -2.86256 | -52.89819 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d219b134-59e0-3fb9-9a64-4c8ed67f0c7f | -2.86201 | -52.90165 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c144d291-f600-3a26-a587-a01a4a8f6d56 | -2.86147 | -52.9051 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 27414ed5-e705-3b8d-84bc-4cdbfd95b63c | -2.86093 | -52.90856 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 521eab58-576b-34b9-9d21-31379aba2bfb | -2.84782 | -53.31662 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82d99ac2-9bf8-351c-bc13-38c96cfafd26 | -2.84727 | -53.32007 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e813f053-6984-35f2-add0-a758b16e4490 | -2.8445 | -53.31611 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6c90990-9d70-3972-b808-573ada645a6d | -2.84395 | -53.31956 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed47fc28-1a19-3eeb-9c1e-7de76b9bd317 | -2.77613 | -53.21008 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84c36503-c3fe-3b7f-a622-a0f8cc3f09ce | -2.77559 | -53.21353 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d169d48e-a2df-313f-92b4-5f8fff0699ef | -2.77321 | -53.20963 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 640ac11a-0ebc-3857-adc8-a8de77a89842 | -2.77267 | -53.21308 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 023eaa0e-05c1-3f71-8ade-5ebd3ce8d8c8 | -2.76989 | -53.20911 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26af8b78-36c0-3964-b1d8-31fd8dd80acc | -2.76935 | -53.21256 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38a673fe-7b58-3f93-b4fb-1d6257a92bd1 | -2.32229 | -52.17975 | 2024-10-08 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72cccdb2-6c75-36c2-80ae-76fffbb29e55 | -4.04803 | -53.51185 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f24d68a0-65d7-33f8-bac0-dc8d948279e3 | -4.04749 | -53.5153 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b73f5b8-b741-39c6-934f-41c70483e95d | -3.89545 | -53.49486 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 269cf133-2c05-32e2-a458-b76472a9a4cc | -3.88058 | -53.71896 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09ebeabf-4fe8-3df1-abd1-b82d6b05dd2c | -3.82555 | -52.34259 | 2024-10-08 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b95c659-4b50-3edf-ad27-285f4eecd9b3 | -3.67676 | -53.67653 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 227e5920-9023-3afc-8a48-33e20edc6b5e | -5.85941 | -53.56506 | 2024-10-08 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 363ced20-ce87-3236-950c-b6a6a2d4b57f | -5.68466 | -53.75415 | 2024-10-08 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 710f8d55-8b23-3761-805d-2f2d646d3ee7 | 0.29605 | -53.38663 | 2024-10-08 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77a70229-4426-331c-9f70-fe94cbfd9d79 | -2.21994 | -53.69296 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41a03ba1-aac1-3b1a-8021-16a43f595100 | -2.21939 | -53.69643 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eda887bf-e234-327c-b5b8-dffd6b9f10f4 | -2.21715 | -53.68897 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 969b9126-58f9-3a22-8336-7ef1fd534f2f | -2.21606 | -53.69591 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed2b8ec5-c248-3ae1-a5b5-54045a0ac63d | -1.24171 | -54.20548 | 2024-10-08 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a98464c-4d49-3bfc-b5a2-d330d42e2b4b | -1.22926 | -54.7043 | 2024-10-08 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e20061c1-60f1-3763-89dc-aad2a314037a | -1.20022 | -54.22167 | 2024-10-08 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad64fb66-2199-38e7-924b-7dd4e9143398 | -1.19685 | -54.22115 | 2024-10-08 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7df48d83-86b1-3fb0-a6d5-b65dfa75322f | -1.12934 | -53.63317 | 2024-10-08 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 416f2c3d-d4eb-3bb9-9641-d90d96e05ad4 | -1.09488 | -54.15789 | 2024-10-08 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b0f035b-50cc-331a-9e7d-e4bdd8456b8e | -1.09151 | -54.15738 | 2024-10-08 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e5f9c04-32d9-3009-9797-ac10aea19b19 | -1.08813 | -54.15686 | 2024-10-08 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 324f3abd-05c4-33b4-94b8-58d7c2360394 | -1.08477 | -54.15632 | 2024-10-08 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9789fee9-a01f-3fca-b119-2d1ec626bd0f | -1.04269 | -53.54089 | 2024-10-08 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef1c2a85-7401-3f9f-8a89-ca190027a433 | -1.0399 | -53.5369 | 2024-10-08 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04d976b5-4f4d-3b11-aec7-ee5959117c29 | -1.03936 | -53.54037 | 2024-10-08 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bb94b0e-941a-3963-8e2a-9070676837c2 | -1.02977 | -53.73146 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63a0a8cc-aaa5-3595-998c-ab5114f94384 | -1.02923 | -53.73489 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4bdcefa-1507-33bd-b281-0ae7d8a8643a | -1.02753 | -53.72398 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93046daa-9045-379e-aaf9-f8fdeb6ab012 | -1.02698 | -53.72747 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58b242b3-8f31-39f3-814c-c2e45672e0f9 | -1.02643 | -53.73092 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07c80873-d91c-31d1-bd6c-93e45cca1cb5 | -1.02589 | -53.73437 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4eaf160f-6304-3d58-b50a-9be0f054ef38 | -1.02419 | -53.72341 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55fdccb7-eb6a-3aa1-b78d-2113deef9efb | -1.02364 | -53.72689 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d50e4985-13dd-3b51-a6b7-1e8d0284952f | -1.0231 | -53.73037 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70fe865e-1a45-3f09-b591-48b7acc43f16 | -1.02031 | -53.72633 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8a53e08-ed49-3c55-ba52-233b67d17214 | -3.37267 | -54.90806 | 2024-10-08 04:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e3d7ce7-a3c7-390e-9bc4-8008e2d166c8 | -3.07113 | -54.78305 | 2024-10-08 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ec2196f-5ab0-33e1-a14e-c62fa71d1a57 | -3.57033 | -54.33709 | 2024-10-08 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e4bce64-88f2-3ac4-a96c-f62c16bc7294 | -3.56977 | -54.34061 | 2024-10-08 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97b22246-6167-359a-9742-cd0906c862d7 | -3.56922 | -54.34413 | 2024-10-08 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1abea035-df38-345f-958f-7eae05f5ea8e | -3.56698 | -54.33656 | 2024-10-08 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c2dabcdc-4d1f-3aa0-9913-1dec488c7cb5 | -3.56643 | -54.34007 | 2024-10-08 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 344d356d-580d-3ddf-8626-117ffcf70955 | -3.56587 | -54.3436 | 2024-10-08 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65979369-6898-336f-b15f-199a034e98a0 | -3.46757 | -53.80325 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15cae866-917f-3ba4-aa89-174fc2a28f54 | -3.44027 | -54.06221 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea1e88e1-8457-3d22-9d58-58960ccb4a11 | -3.43972 | -54.06569 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daa6b7c3-43cc-3569-96a8-d298bb0898ac | -3.38003 | -54.90558 | 2024-10-08 04:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f1e31e9-e9e8-38cb-8034-8e0d021df232 | -3.37664 | -54.90503 | 2024-10-08 04:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a17e6f4-be11-3c3b-9859-404fe2176a88 | -3.37212 | -54.90817 | 2024-10-08 04:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b6b568f-6b5e-3bbe-80a3-728762e8dbd3 | -3.27659 | -54.17567 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae76e8b4-5d0a-3566-a91c-9b5cb9c756bf | -3.12522 | -53.74228 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8447c5d4-f71f-39ff-acd5-35b6c896672b | -3.12353 | -53.73495 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8a21ef78-3e0d-3de3-af70-31267b0c6a6e | -3.12075 | -53.73097 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d1edded-8649-3865-ba93-940bc66498aa | -3.07228 | -54.77586 | 2024-10-08 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aff289b6-e244-3d2a-8226-541b29d131c5 | -3.06889 | -54.77533 | 2024-10-08 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f3af460-35b8-39c5-b652-b7883564deb9 | -3.06496 | -54.77517 | 2024-10-08 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06de68b4-8fbd-344a-b5ea-67d052f894dc | -2.9521 | -53.70488 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f3ce20f-df08-37ac-a167-5183e1233e9d | -2.95156 | -53.70834 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe3f5c39-87d7-3420-a596-5fd57d6ab653 | -2.94932 | -53.7009 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ba4a421-6d9b-30e4-bd85-436afbcbc47f | -2.94823 | -53.70782 | 2024-10-08 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf4296cd-d1d3-35c7-985a-cc9a37619936 | -2.90546 | -54.00002 | 2024-10-08 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf172c2f-db36-3e3b-bace-63701f842515 | -2.81403 | -54.35985 | 2024-10-08 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a35e6a7-cfcd-3260-a838-da596bac4511 | -2.69891 | -54.59663 | 2024-10-08 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55eddc28-58d6-38bf-94f0-bddc5dddf411 | -2.69349 | -54.78403 | 2024-10-08 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa2bf3c1-95b8-377b-883e-c47e5da91a7a | -2.64066 | -53.96547 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 071d554d-b6b4-3354-90c8-8fa2ef717526 | -2.64011 | -53.96896 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7664f59d-725e-3031-93a3-a6cb91ed6de1 | -2.60533 | -54.54929 | 2024-10-08 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a559bc9b-62a8-35eb-8440-8edf04289ae5 | -2.60195 | -54.54877 | 2024-10-08 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f176cb5c-7f69-3332-91a1-0c45c1862473 | -2.30972 | -54.40821 | 2024-10-08 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96d3ed0f-2c4c-3e31-b313-d0ed8a04213e | -2.30043 | -53.52457 | 2024-10-08 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2dd31f37-57bb-3fd1-af53-1e65dce551c0 | -3.74355 | -54.3065 | 2024-10-08 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84c52e96-c317-3f70-8d9f-af1e60c660a7 | -2.21463 | -55.05247 | 2024-10-08 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c360d5a5-7da0-3d92-903d-9f21f63ed832 | -1.67063 | -55.1386 | 2024-10-08 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3125216c-a948-3c8b-a25d-e30db5fea2c7 | -1.25858 | -55.85526 | 2024-10-08 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f593ab8-6d55-35d2-84fc-834e5b1b5f4c | -4.86231 | -56.00602 | 2024-10-08 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 630cd32a-6a5d-39b2-93a3-50b37ca11d31 | -4.85884 | -56.00541 | 2024-10-08 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db0bcbd2-68a9-3f39-8d35-fcf6a73f308c | -5.25035 | -55.94596 | 2024-10-08 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a8b1fe0-a5ac-3f17-87f0-72e7947eab63 | -5.25019 | -55.96928 | 2024-10-08 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7049c1fc-b3dc-3e73-84e5-18de392cb24c | -2.54635 | -57.87159 | 2024-10-08 04:55:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f19bca92-e542-3ec8-8e0d-a42126e84211 | -2.54239 | -57.87096 | 2024-10-08 04:55:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d55bb812-1641-372b-a20d-f82bf632dab2 | -2.36301 | -57.12733 | 2024-10-08 04:55:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2da84199-91c1-3e76-a1cc-907dd41e2291 | -2.68721 | -59.57857 | 2024-10-08 04:55:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc8f32da-1c5c-3416-9bb1-8a7459952c40 | -5.09535 | -60.23171 | 2024-10-08 04:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55cb7434-6bde-310e-abc8-6d27900ccc46 | -5.09379 | -60.22969 | 2024-10-08 04:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README84.md)
