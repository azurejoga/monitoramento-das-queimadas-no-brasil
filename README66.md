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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d4c4127-afab-3599-835c-e7b3cb6ed7d1 | -3.94787 | -52.25074 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5d13177-5b39-37f6-b928-27604bcf332c | -3.94717 | -52.25507 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 988e164c-ae24-3db7-8eeb-5dbe977c0bc7 | -3.94646 | -52.25944 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5142fde0-ac36-3e2e-a66b-0a0f4e8c2fe5 | -3.89865 | -51.81693 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0bb23fe-5181-3fc9-850b-2edf6edf9217 | -3.89024 | -52.12466 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9eba371-b980-3db4-9b35-a138d45338f6 | -3.88658 | -52.12407 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01f72a7d-7528-34cc-8072-5ab83d0752d8 | -3.87742 | -52.08757 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15ea628c-c2ca-3158-8b68-e07de8c9f13c | -3.87518 | -52.14842 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24320996-cd4c-3cc4-89c9-d361d2a20084 | -3.87375 | -52.08706 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c4e723b-d57c-34e7-8677-3e3a1406eba9 | -3.8683 | -52.26225 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0be39712-88ac-3977-850d-2c0361cc4c3d | -3.86624 | -52.13387 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 611cfe3e-fb2d-37bc-ba58-6999fd345787 | -3.86555 | -52.13814 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3452f519-6f6b-3440-9b9c-5935041ee68d | -3.83094 | -51.36168 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e03862d-ed00-3825-8731-f456f34c93a7 | -3.82806 | -51.35715 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d0798f4-df2f-3731-9990-3c0638a30056 | -3.82742 | -51.3611 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28159f83-9a95-332e-9849-7399ed0169a0 | -3.82166 | -51.39656 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a27faadb-ec5e-3574-bd74-fe52028d8efe | -3.80872 | -51.05247 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d4286a6-7786-32c6-8f37-e04e2ce72022 | -3.74634 | -51.05481 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 503456cd-f158-3b67-9d73-82413c8c2653 | -3.6934 | -51.11753 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ced545c-3c9c-33d3-9514-b8c1a2f4594f | -3.68438 | -51.08447 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a9b758d-3823-3512-a5c8-ae34176289b1 | -3.68376 | -51.08832 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe44a9a3-1f08-3c60-9fa5-c81dc6255dfa | -3.68313 | -52.09072 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f896ee2-0240-3b6e-a337-d002febbe8fc | -3.68313 | -51.0922 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da8dd10d-defc-3516-a637-78f3b0f562af | -3.68244 | -52.09502 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55859ddd-9fd7-3250-85ea-9d99cec16a03 | -3.68213 | -51.84044 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 681df021-2e7a-3e47-a4ac-6fddc677e667 | -3.63967 | -51.43018 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ed6a469-566f-311e-be4f-6be52913d6c2 | -4.67379 | -50.97171 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd97bee1-5681-30bc-b574-49eff4b4c51c | -4.66974 | -50.97491 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 35c447e6-f84a-3e1d-a3f5-0913b8c1085f | -4.66913 | -50.97867 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cd0ba912-dc54-302e-92e9-afcbc2a7ec0c | -4.6669 | -50.97061 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f20b4438-17f2-34fc-bb25-f3d24d40a476 | -4.66629 | -50.97436 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3b43409c-0393-3e9f-aa05-a4530049874c | -4.65981 | -50.9926 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77d9abd8-361a-3e22-aad9-89dc01f295eb | -4.65697 | -50.98829 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5050bf5e-6c42-3a56-95cb-1efb0b1ea221 | -4.64843 | -50.91011 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 573ec292-5cc0-37e7-9137-aad63dd2b26e | -4.64574 | -50.9102 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ca527b1-5621-3636-bdd9-d04311a7267a | -4.64515 | -50.91389 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79e57f82-219a-37b9-bebc-a645adce5952 | -4.6417 | -50.9134 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c7e247b-3c7d-3f3f-b3c3-12952d9126c3 | -4.54013 | -50.97411 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1c382b4b-3d0c-3337-9b8f-0bc6bc781916 | -4.12086 | -51.1077 | 2024-10-25 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47c67598-dbc4-3a20-b78e-ab4ef3c6afb7 | -4.07884 | -51.12465 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee2504ff-51cb-3728-9b07-60ddb4eb4f53 | -4.07821 | -51.12849 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| baf1d005-91d7-3458-8ee7-42dbe7d897d9 | -4.07536 | -51.12405 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d319741e-2722-387c-a087-8347bc786e2e | -3.93152 | -51.0046 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2e828fd-2dd2-3d19-9f5a-ac12f2b05fdc | -3.88882 | -50.98238 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a541f177-bcf3-34d2-a11a-d962552cec4e | -3.8882 | -50.98619 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 886b2653-c02b-39ca-b90e-c10188ef8b30 | -5.88934 | -51.29517 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1d19a2f-f3dd-3aef-823f-f02420d050d6 | -6.39073 | -52.65064 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fd95221-735a-3c64-8bcc-254428b8e0d5 | -6.38708 | -52.65003 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 390bf857-6f71-3de9-94b6-072c5dbfa594 | -6.38343 | -52.64946 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8655acba-a1de-33f0-bb94-74c84db44d42 | -6.14524 | -52.64452 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8577244-5210-37fe-b7d4-ca75b356b512 | -6.14454 | -52.6488 | 2024-10-25 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 976ac166-beff-3256-b224-87c86acedf95 | -1.97259 | -52.07191 | 2024-10-25 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98842233-b181-31ee-a528-10c10b426e63 | -1.97234 | -52.06961 | 2024-10-25 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9c39abd-b930-3aa8-a36b-b7fcbf5e384a | -1.94783 | -52.94215 | 2024-10-25 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 162de518-820c-3150-8c0c-0581715f0521 | -1.94748 | -52.93885 | 2024-10-25 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88e3ee27-eacf-3af0-bd99-2b0b00a868f9 | -3.10906 | -53.13517 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e273b82-d984-364d-b17f-584711b363e2 | -3.10874 | -53.13183 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4df26cb-8737-35ae-aa1c-11b59376e335 | -3.08303 | -53.22353 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd4438e8-108c-3156-9f6f-eae18ef8195e | -3.08127 | -53.22489 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e57870d6-05c0-31ce-9386-ab12ce2b2a43 | -3.07963 | -53.23481 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd4474a1-4ba6-32e0-bb92-6a429818d922 | -3.07908 | -53.22289 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fb775a9-de09-31f7-b9cf-1ccd55734c3c | -3.07672 | -53.23781 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0cbee8ac-044a-3717-8c73-ed85cc8c7e3f | -3.07593 | -53.24277 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13543aa3-3eb0-3fcc-9b4c-9142e0d571c4 | -3.07514 | -53.24775 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e15cd705-26d1-332e-b862-122aeea889dc | -3.07486 | -53.23914 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69e9a6bc-2f30-3056-a132-f8f9f954a868 | -3.07404 | -53.24409 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2d5d918-7bbb-332b-bab9-2e859dfb8590 | -3.07322 | -53.24905 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f1f722d-2591-3c3c-be48-2d667253874b | -3.07276 | -53.23723 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f161bffc-48d1-3baa-b041-d004b8b13001 | -3.07197 | -53.24219 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 854e881b-a500-321e-94bb-ba30c48eb7ce | -3.0688 | -53.23664 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fcf2e19-a112-38b0-915c-48b31e3ca0f7 | -2.99963 | -53.43919 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 332c62df-ac75-3b06-b3d9-ffc8a3c75b76 | -2.99906 | -53.44272 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4d2e09c-578c-3581-9b74-c9ebd853744b | -2.9967 | -52.85991 | 2024-10-25 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3515ccc6-b084-3405-bd9e-143e3f4626a4 | -2.99458 | -52.36747 | 2024-10-25 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3be1e75-b54a-3ac0-8c9b-54f77f6783ad | -2.82253 | -52.99917 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 075744e4-e752-3c21-916f-298ef91a93c8 | -2.75307 | -52.04839 | 2024-10-25 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e5a7be8-6c25-3da1-b1c6-e14d41a48b9e | -2.73794 | -53.20285 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fec08013-ea4c-32f9-beff-69bdf26de5b2 | -2.61914 | -52.44481 | 2024-10-25 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 89c2ad86-bd89-3936-bb63-ee80cdf10440 | -2.19337 | -52.80581 | 2024-10-25 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69bf4e40-f015-3bc9-a869-401ba9c52554 | -3.2229 | -53.36868 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b972c92-d82d-3991-9022-a970730309e8 | -3.21976 | -53.36288 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53567d2d-dea6-3e34-8e6d-2ca014de3ac5 | -3.21894 | -53.36798 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eed2bf30-74e5-3beb-b44a-5917b8e42ef3 | -3.2158 | -53.36217 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8e468fe-ba55-3a93-a94a-8d2d6e1e3e30 | -3.21498 | -53.36726 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f409c5f9-1668-3bde-814f-29c051146dcf | -3.00306 | -53.44341 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb53fa6e-e38e-3e97-b3d1-0fb5ff512cfe | -2.73397 | -53.20228 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c74a367c-67c6-3199-a198-01c16225906c | -2.62292 | -52.44543 | 2024-10-25 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f3abd93a-5ae9-3f37-b50a-14db85d56386 | -2.6222 | -52.44997 | 2024-10-25 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| dd34747e-0c21-3112-ab1d-4122a75713b5 | -2.61841 | -52.44937 | 2024-10-25 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 692d4790-6ec5-347a-b681-9c92cfd67ac7 | -2.61535 | -52.44422 | 2024-10-25 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98fb1778-3e62-3a6d-a472-1f3cef14c0fe | -3.54026 | -53.01286 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d94e648-47de-31ad-9e21-2725fbb070c0 | -3.53524 | -53.51486 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47a9e9ef-5259-3ec8-81e9-4effb7d4dfc6 | -3.53137 | -53.26442 | 2024-10-25 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5038fde4-1e3b-318c-a99b-0d9fdfed9f74 | -3.47672 | -53.4476 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b97a251-89fd-354e-a505-f5d332699d06 | -3.46334 | -53.29292 | 2024-10-25 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a877a332-a995-3471-b6bb-c7b0f2fb196a | -3.45551 | -52.62101 | 2024-10-25 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0eaa5486-206d-3f3a-afd6-3919d52c9e14 | -3.45173 | -52.62045 | 2024-10-25 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30f6851f-4729-3d5a-b167-0d2dff08419c | -4.2227 | -53.78776 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1339b5eb-64d9-33a6-9553-8d5d29d39b2f | -4.17098 | -53.59252 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c76b4b3-2ee8-3868-b843-0293f3fc71b4 | -4.16458 | -53.48235 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README67.md)
