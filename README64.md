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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ec0fe2b-cd4a-3ab9-9498-79393e2c50ad | -3.3943 | -50.80556 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55654c49-6608-34dd-8897-d0159b2e8da2 | -3.39375 | -50.80903 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da7b97ea-f897-3a3a-8ed8-aa788d06d1b1 | -3.37908 | -51.07437 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 191877db-3fa4-3358-9312-82d6bad03827 | -3.37852 | -51.07787 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dbf7281-6a8e-343d-bcc3-149ff6b0dd0d | -3.37518 | -51.07735 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3389ac1-c667-391b-ba57-1e24f8e79a89 | -3.32644 | -51.04844 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fdfae0b8-9dbb-3912-8df1-cafa34220512 | -3.30257 | -51.09129 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84dc1881-2f86-3e26-bef7-5b0befd4fe0b | -3.29235 | -50.9394 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ccd2661-4298-3a05-90b9-80bbdae1db2b | -3.2918 | -50.94288 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54e8cef9-5446-3d7e-b4a1-83b44cf3e358 | -3.28847 | -50.94236 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e74047e-aa29-3fdd-b096-b1a9473e177c | -3.27316 | -50.69738 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3324522-f3fe-3264-b475-bd8bf3201a1b | -3.27262 | -50.70085 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16002c98-d851-3118-bcf1-3a55c0f562be | -3.26984 | -50.69687 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6ab1c8bb-1b44-3273-83ad-294c9ba51023 | -3.26632 | -51.01753 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13addf46-ca68-3248-9614-1215543dd913 | -3.26576 | -51.02103 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| faca45ce-8f75-3673-88b2-f639579c498b | -3.26353 | -51.01351 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 813a85eb-384b-333f-8093-516601abefbf | -3.26298 | -51.01701 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5adce3b6-4df4-384b-a072-eef1d546630a | -3.26242 | -51.0205 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d90d508-a2ed-3f07-a7cb-7ab845ecc07e | -3.25964 | -51.01648 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a2148a9-3415-3aa6-ae1e-b05d0653aefc | -3.25909 | -51.01997 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7c26822-8d20-3d11-b2f7-fd6811cade3b | -3.25756 | -51.26783 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 000d81d8-4135-3cab-94d3-3041bae6130e | -3.25197 | -50.63731 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1de1302b-f950-3245-9cad-8e4429c1319f | -3.25142 | -50.64077 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 309b7e37-06bd-3e83-862f-5be01f0b11d6 | -3.25088 | -50.64423 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 032a8985-b972-3b68-a936-a1fc097e18cb | -3.24864 | -50.63679 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d6bb639-4c99-3360-a4b8-01f775c24198 | -3.2481 | -50.64025 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f54cab17-d30f-37dd-9730-f21c28ef30ca | -3.23723 | -50.73082 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69d8da60-5630-3757-bf83-99c64d585cf1 | -3.23445 | -50.72683 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1214d48-92aa-3cb6-8f05-4c6a1582e54c | -3.2339 | -50.7303 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a229bf4e-cdc2-3fd1-89f5-1dffb5c982ba | -3.23335 | -50.73377 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a496046-637e-391a-9c5b-fec4ac0e5ad4 | -3.22626 | -51.03275 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91b6e438-affd-3c9e-8709-13aa3f04ba0d | -3.22396 | -51.03183 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 448390c8-5534-3581-93b9-41e46dbe0f7d | -3.20946 | -51.01522 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 111e79dc-8fd8-3af2-ba4a-235cecc551c7 | -3.20891 | -51.01872 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70ca8dc0-a557-356b-b773-e479d19678d2 | -3.20613 | -51.0147 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9220e6ab-f947-3a38-9e74-c8fa41ef8d02 | -3.20558 | -51.01819 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0803fda9-46c0-38f1-b7b2-10e168c77283 | -3.20525 | -50.82539 | 2024-10-30 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0368ec5-cf80-3867-8e25-f7e8ac2f6766 | -3.20472 | -51.58 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3d05338-698a-3139-ae8d-7b4af986ca28 | -3.20416 | -51.58355 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 118c412f-db4f-3d0e-afa3-7bcffb74e54e | -3.20326 | -51.3716 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 93a5c63c-dda9-3c2a-b076-e8b24a71cedc | -3.20279 | -51.01417 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b445fe4-5117-3e8a-8040-3bb064d538bc | -3.20224 | -51.01767 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92a058c7-8dcc-369b-9504-0d76b815d7ed | -3.85671 | -51.6959 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ff7dfde-9455-3801-a257-42aaa95d8035 | -3.85501 | -51.70662 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a78e6a2e-3d36-3aaa-ad09-e6cc060761fa | -3.85401 | -51.13443 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dc81403-ae18-33d5-9be4-6e3bd4be45f7 | -3.8519 | -51.3785 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea6ffb10-ea60-31bb-84cc-bc77f56216ae | -3.85176 | -51.12698 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2962e541-d95c-342a-b522-4aec1738163c | -3.85121 | -51.13045 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49609a8c-c413-30f7-9911-3c0078fa4456 | -3.84653 | -50.98686 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e897d129-4404-3e24-87e8-1c171470da31 | -3.82943 | -51.05192 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33126110-f447-39bd-80f3-e36bb818d2e5 | -3.8261 | -51.05136 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce8d49f2-66a2-314b-8b1d-8187a1c94083 | -3.804 | -51.16944 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb490637-b041-3ca3-b8b4-62dba5c77464 | -3.79352 | -51.96323 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 043e92c4-4590-3dae-9c15-00e84c3536b4 | -3.72091 | -51.34724 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95c9c45b-c79f-31a3-8dfa-edfb5dea17fd | -3.69189 | -51.85455 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58c5d7d1-d137-3a39-9777-bc7050e7af94 | -3.65025 | -51.94102 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6484954-1d0f-3cc8-ab11-5d3d4242e9f1 | -3.64966 | -51.94466 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b77cd5a1-5f74-373a-85b4-5b97c7eea473 | -3.60015 | -52.01591 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cdf07e9-c2de-3800-9027-94ae30e0d22b | -3.54097 | -52.14613 | 2024-10-30 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ea38f44-8c6e-3f95-ad39-059bf888c45a | -4.47756 | -50.9969 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b68843f7-4f4c-3c76-b87b-c8b3af727a7c | -4.05188 | -51.07935 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6279eb08-e5df-348a-8450-f558166605da | -4.05133 | -51.08284 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7438db4-da36-3e52-87f6-9a8ca3a2e6d2 | -4.04855 | -51.07882 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7aa72e0e-a16f-350e-addf-5b7bf7235773 | -3.98214 | -50.90128 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75bd98c2-f9b3-37e2-8ffb-3926c9d77611 | -3.95582 | -52.19411 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe5bfaa6-1538-3652-acfb-9dd055748541 | -3.94127 | -50.98737 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 475c38ec-d5ad-3db6-b687-a595a44a5595 | -3.94072 | -50.99086 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d50497bd-f7c2-36a0-a3ee-77616769c700 | -3.93794 | -50.98685 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5f5a33e-b94a-3590-b885-e6c7d51ad00a | -3.93739 | -50.99033 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7db6c50-7894-30cb-992b-a162fe8469aa | -3.90969 | -52.26281 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78806486-8741-3d58-ba5b-52b83bb1d9c9 | -3.89527 | -51.91541 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 535b5d6c-60da-346b-998c-6032d8dea08c | -3.89469 | -51.91903 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1639cea1-babc-3c1b-ba89-0fa6d50f1649 | -3.89188 | -51.91486 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7280804e-536a-3004-8dd9-cdb161e5c511 | -3.8913 | -51.9185 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 96ac6aea-23d7-31c2-8c33-739d028f68ee | -3.89072 | -51.92215 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54c164d9-0da5-37d6-b573-c3be0d497029 | -3.8879 | -51.91796 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c66eaa4b-5495-3425-9ddc-31080996be5e | -3.88732 | -51.92161 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce7f4e5f-36f8-3174-88e3-9ecc730414b1 | -3.86224 | -51.81772 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f907526-4fc5-33eb-b58b-45c6da49cd9b | -3.86008 | -51.69644 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f91196df-82be-3e84-8ae5-37669c4c42ed | -3.85525 | -51.37902 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 526f9be7-7590-3409-9810-8165f815c845 | -3.84843 | -51.12646 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab1b0d8d-d93b-360f-9961-fcd8ec65119e | -3.80066 | -51.16895 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2078fbc0-5a9b-33ad-a6d4-8a146111fe0f | -3.79012 | -51.96269 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce98ba5e-62cc-367b-a8f6-9671cce170f5 | -3.76012 | -51.06634 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 976bca90-2201-3877-90cf-d68362f4d9af | -3.7438 | -51.37611 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b76a9c8-a3aa-3d67-b7fc-184fd605031b | -3.71756 | -51.34671 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48e7812a-4477-3805-a7e0-687d2a095427 | -3.717 | -51.35022 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4180d798-a214-387b-82c0-74ee9806373a | -3.71626 | -51.106 | 2024-10-30 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 612b0d49-8b41-3220-b2c1-e78e83523fc3 | -3.69544 | -52.00796 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2eeb1efd-a8c6-3e68-9744-4695a6ce0815 | -3.6885 | -51.85402 | 2024-10-30 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97189fb3-eb93-37d2-8652-19806698241e | -4.66881 | -50.98477 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb3eba80-a6ab-334f-a8e4-78a20305255b | -4.66658 | -50.9773 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0c01d67-2435-36bc-aa50-b10ee2819a69 | -4.66603 | -50.98077 | 2024-10-30 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8876d7d-7be1-37ae-9ffa-4e002f7b346a | -6.41437 | -51.65273 | 2024-10-30 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01a9036b-ee77-3d1f-baba-d3386a748e76 | -6.41381 | -51.65624 | 2024-10-30 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb91a0fd-90ba-38a1-8ffd-542ca1991125 | -6.26398 | -51.70091 | 2024-10-30 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d278f369-97a1-30c1-8fc2-d3fa3ab91a40 | -6.26064 | -51.70037 | 2024-10-30 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9567b19c-e71d-399a-bc91-b55dad20d0d7 | -5.65669 | -51.69147 | 2024-10-30 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54fcb644-8c8b-3af3-9637-f06da8db004b | -7.00376 | -52.05355 | 2024-10-30 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69815843-b2a5-3c2d-8496-07e801455c54 | -0.7058 | -51.98447 | 2024-10-30 04:44:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README65.md)
