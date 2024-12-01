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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e7f9208-97d0-32fe-8bb2-2488b6e5cf28 | -2.10479 | -50.73796 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14afce1a-f30f-3d40-bfed-51a1b7b7ce57 | -2.79974 | -53.05076 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddd434db-5cd6-3c96-a1f2-7ac175802bf1 | -1.33175 | -55.8483 | 2024-12-01 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58791e3a-e56a-3025-ab3b-6e8e086b2a99 | -1.39054 | -51.59306 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 265e6b0f-3798-37ec-9b32-d82a610d45c0 | -3.12674 | -54.53277 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 5359cb54-4e6f-360f-958c-28f92f29d2f2 | -2.26073 | -53.45726 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35804ca6-9899-3816-81c3-6d7999defd7b | -4.00678 | -54.61687 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36d3fcc9-0eaf-3504-a290-62e72e95105d | -4.06112 | -46.67933 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 992696fb-8821-391a-a12f-ff43bff3591c | -4.26487 | -50.83831 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 172c0c78-18bc-39e5-83f0-53b020b539af | -2.01035 | -51.1839 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad5423ee-d64b-3ab4-9b64-b80dd9d0dd5b | -3.99452 | -47.91557 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faf7449a-4742-3a35-936d-b65f4103b7a1 | -1.25469 | -51.78784 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a08ea19-e6d0-3261-93d7-7c7d6c65f1a9 | -2.86141 | -53.32002 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 290c4d1e-55a9-35a8-a8bb-2c8e2304a515 | -2.8076 | -54.04107 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9742dd3c-2253-3f44-95a6-00daf09e493b | -2.88244 | -53.32782 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72581188-5625-3b8b-a922-a6d84ede088d | -1.66505 | -52.49873 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 030c01f9-6519-3c1e-b3c4-333cbedf4d62 | -1.3219 | -51.74127 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a07cc6f0-fda2-349b-996d-60d8e5c394ee | -3.70471 | -51.06707 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7b0f9d9f-e73c-36c1-8069-6bc2e9d10cf7 | -1.62575 | -52.38131 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b291aea4-3293-3829-b996-d45fc0c24c79 | -1.70759 | -52.7697 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 659ad978-12f5-396c-af79-aa62f8d4de66 | -3.98652 | -46.64025 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9b86b003-5029-3d9c-87bb-29879b508aee | -3.52319 | -50.47794 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c85eddcb-b780-3c99-b64e-3ab1dd6e3a53 | -2.46537 | -46.56853 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 509db850-a4ec-3d4b-80d7-f94a2d131683 | -4.99749 | -50.74135 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a097573-fe50-39f5-bdb4-aa93e941735b | -4.69199 | -42.39266 | 2024-12-01 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 765595ea-1cdf-38bd-9dbd-faf22b3e10e3 | -1.61601 | -52.35192 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0565641-b5ce-3944-8bd8-9b6d94577e7c | -3.3258 | -52.07576 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21ae15f5-cc6c-3864-a1a6-2873e2a7e1f0 | -3.49829 | -52.13198 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b068066-c6fa-33df-99c1-670b725506a1 | -0.99443 | -51.71471 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7be09dd-0d64-3543-b4ba-c500788c5959 | -4.25547 | -53.53451 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1c93723-2cbe-3883-8de9-e522e837cea6 | -2.88262 | -51.78618 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76a76ff5-d0c7-3a51-89ed-8ef1ee2d1abb | -5.5075 | -42.87271 | 2024-12-01 04:44:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 8c3a6a4f-d4fc-38a0-bf49-6eebaff57119 | -2.57304 | -51.88765 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07c86e72-8cbb-36d8-8fe1-3e4568c1d299 | -1.12922 | -53.09476 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3144f7c-fa0f-319e-8de0-2e011c03ef51 | -2.27477 | -52.83723 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09a9da6b-7cd7-33b0-8255-6cb96dff1156 | -4.53714 | -45.7035 | 2024-12-01 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 824c06cc-ba12-3c9c-8973-7b7dbe682ce8 | -1.72118 | -52.62494 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fee40e48-334e-371f-88af-99c9afc6ba08 | -3.25177 | -53.63108 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3e32dd9-b77c-3778-88e3-e91afec69a62 | -2.83353 | -54.09405 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3793176-a990-3a07-8f9a-0ff17d85662c | -3.30538 | -53.82777 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6daca931-0492-380d-87c3-cc240509dbf3 | -2.89024 | -54.00542 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1ae910d-21e8-3938-ab35-7602f80c4878 | -1.29262 | -51.373 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16de8d8c-37a2-3edd-88c6-7d5200eaadf2 | -1.08461 | -53.39602 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ffa210f4-a4e5-3dc8-9961-7e6ce39ac224 | -2.8929 | -54.15998 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e96a7e71-6de9-36ae-9d04-60e5d9e5debd | -3.95159 | -48.17365 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| efad251f-4478-3e0e-979f-37b5ae27dea4 | -3.98277 | -46.63964 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9eb47a53-a9a2-3e00-a014-b5d45388cc05 | -2.55896 | -46.563 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 234c1863-4fd0-3dbf-a445-8554dd9a3e73 | -1.71701 | -52.62836 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5bfd75f0-5076-328a-bf44-078bbcd5b3d8 | -3.10723 | -53.80943 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1d0ad71-e43b-3f90-8d18-b28d2d170684 | -2.86914 | -53.99285 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01f773d1-fe3d-3e8d-9c01-68abce497e61 | -1.00888 | -51.72768 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 60b051e9-3106-3164-9aa6-0a45255b1821 | -3.88723 | -46.40398 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9f91c67-1f88-3c84-8300-3fc4b79d5e33 | -1.50385 | -47.47247 | 2024-12-01 04:44:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e907692b-14b6-3d7c-ad38-b354fff07ae7 | -4.85915 | -44.2351 | 2024-12-01 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85a61006-ce8c-3788-b537-04f191de97e6 | -2.73213 | -47.98985 | 2024-12-01 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1741ce8-8b37-384d-bd1a-6ea09dcae000 | -3.89031 | -45.0086 | 2024-12-01 04:44:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3069d5b3-69ff-3df9-a31f-319f664f478f | -2.90478 | -54.17924 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35cae3e1-6efd-3639-a1d3-70a555ba9565 | -3.30143 | -50.27324 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ed34a24-82d0-3d97-b8d7-c5bc3babee2e | -3.51968 | -62.7612 | 2024-12-01 04:44:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c7f69cd-ba77-3627-bcb0-e8eb97ad548f | -2.82816 | -48.47118 | 2024-12-01 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a18f5e5b-2760-3594-861e-49a174c359fc | -4.17809 | -48.61063 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db6702f6-3c3b-32d9-a32d-e50ba4dd48ea | -3.81649 | -52.08364 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1cf63927-b625-3fec-82ce-c8c614bc6c0e | -3.39332 | -50.35455 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0aeda33b-3f3d-3356-b99c-6f7f629f2d31 | -1.62757 | -53.86306 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 272baade-2f34-3c65-b702-08466300bc24 | -3.20928 | -53.12811 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffd61232-5434-3f7d-817b-657d34da3768 | -1.27633 | -51.82946 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4405b63a-26b7-3d12-a2d3-7b693e90ed9f | -3.26806 | -45.37661 | 2024-12-01 04:44:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41ddba7d-04aa-31de-a29e-c29ac2f790be | -2.01147 | -51.19862 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78ea2ee4-0549-3272-afdc-8c12fd0118b9 | -4.34762 | -48.12603 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf61292e-841a-30ea-847f-b19c129fa585 | -4.01764 | -49.93526 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 729cf801-565e-3b93-a7c1-604f06276672 | -2.8891 | -54.1594 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5de13a13-dedf-3b77-a1cf-4c4c2cdf93b3 | -1.59844 | -52.28182 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6557590-a25e-3e33-8952-d1943db0479a | -3.27115 | -50.20839 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a4fe527b-68ac-32ad-89e1-5f30a1829aac | -4.07507 | -46.82083 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65c202a1-5281-3cec-bd7d-9f8eedfb5233 | -3.655 | -50.2191 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5c44ebc-5875-398c-83a1-4a0cabc59177 | -3.37057 | -50.82201 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13864c48-23b2-38cd-8f0e-15d279fe8a2d | -3.60365 | -49.9883 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 198b83c7-99b0-3e40-88af-a3726222d95b | -1.31788 | -51.74444 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68afdae0-a446-3e91-914b-a6155bdc90e2 | -3.81383 | -50.95204 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c36a14b-3ad6-341a-b930-37a2dcfa5783 | -3.12334 | -45.9808 | 2024-12-01 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e83953a0-b8ad-318c-9128-570f0b66a7d5 | -1.29659 | -51.36992 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa14a184-2078-321f-90a6-90e6dd43b1c6 | -2.89539 | -55.22554 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94943cfb-c4da-35ca-8cc4-441cc8325db2 | -3.3278 | -50.21375 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0d756dc-fa75-3e54-9a46-f01de0d182f1 | -3.89457 | -50.07223 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88b8743b-5dac-37a4-80c5-395dffe3eff0 | -2.42247 | -50.3968 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a220956f-2ff3-34b2-9eb6-2a881164375e | -2.80625 | -53.05593 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ada58c06-2a7a-3230-a0c5-f36e316138f7 | -3.06306 | -50.32735 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3acdc28-8ac2-3965-a162-e2ec51205369 | -2.88408 | -52.18956 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0ef0890-c7ce-3ace-a52d-63a0da85745f | -4.25768 | -50.84072 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9149b02f-4dc0-39ec-9208-53c21bfcf8c6 | -3.11201 | -53.75611 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87ca9c50-feb2-37cf-95cb-42d10d73491c | -2.28579 | -45.60141 | 2024-12-01 04:44:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 12a9d9fd-8a07-390f-9119-3226faa9ad4c | -2.80017 | -54.03741 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d59b0e0-8681-3722-90da-8e8fc2114c05 | -3.79029 | -58.97529 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fef5f3d6-127f-3900-a59d-43519738a450 | -1.07788 | -53.39055 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69e3f2a4-0b49-3744-91a9-bc4b7043cb0d | -3.30136 | -53.68969 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f329ec0-8239-3dc7-9a1a-74dbeabf7b6f | -2.57398 | -49.99657 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cd5825d-0b11-3ad4-885b-2f00ffd8dce8 | -3.52651 | -50.47846 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7f161841-7457-3357-a897-c1e37c50b75e | -2.47425 | -46.57217 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45396c22-92fa-3d33-aa99-c5a03adc1139 | -2.91451 | -54.11957 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce215aad-4631-312a-9d4b-a8cfea9ac925 | -3.11419 | -54.26928 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README64.md)
