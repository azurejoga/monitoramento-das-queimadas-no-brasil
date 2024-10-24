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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d092c73-c4df-3c7d-a06f-897591890869 | -10.49892 | -54.55449 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90e13ccd-b4a3-37d9-975b-718979771f3d | -10.49837 | -54.558 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a08cd43-7c80-3763-93b5-52ad0f0b4650 | -10.47595 | -54.43896 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 067b30a2-cee1-3568-a176-ce387b6ffa79 | -10.47207 | -54.44196 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 228d36c0-e5eb-3cec-801a-fa6df1441a7b | -10.47147 | -54.42378 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ec09e62-c0b9-301b-b68e-2249b6af26e8 | -10.31952 | -55.02879 | 2024-10-24 04:57:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f6e5377-4564-3fb0-bd4a-b6889a16aba6 | -10.31897 | -55.03229 | 2024-10-24 04:57:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87299157-e211-32fe-8f99-6e838363a557 | -10.29584 | -53.72388 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5ae3403-7d83-33e1-a1ce-9e37feb25ebc | -10.29302 | -53.71975 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e3976d7-624c-323e-b960-19aa54eb44a2 | -10.29247 | -53.72337 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fc075d0-f1cf-30eb-a585-56255a673b8c | -10.20294 | -53.87207 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f507a6f-4add-3b89-8c14-87aef8b366f9 | -10.20014 | -53.86797 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cb2bfad-f3fa-3a99-bad1-ef19561b125e | -10.19958 | -53.87155 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2346b94-5cf1-3799-8e72-da6f40019942 | -10.19903 | -53.87513 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54766fb6-7bbc-3ecd-a357-a1cee08c565a | -10.19678 | -53.86745 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9639b9c6-c2ae-3ee4-b602-c82fb15e5cb5 | -10.19622 | -53.87103 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b90a5446-2aba-3b5c-b940-7e2c08046342 | -10.19567 | -53.8746 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9fecb5b-76fd-3a09-a8a5-a0dea8e29906 | -10.19512 | -53.87817 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de0bee41-dd51-375b-9473-bc4caf1bd87a | -10.19287 | -53.8705 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15800928-9a37-3b97-8734-51cd09b5f732 | -10.19231 | -53.87407 | 2024-10-24 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4b2252c-11e4-3105-a1a7-166a4368ada1 | -12.0354 | -54.65296 | 2024-10-24 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| be76d743-f157-335d-8909-b0518dffe744 | -11.52259 | -54.31929 | 2024-10-24 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 887ea2f1-5b75-3bed-b6e4-ff338d8e877f | -11.46364 | -54.41246 | 2024-10-24 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 280d26bc-a0a5-311e-8a42-ae1bd2aeee74 | -11.42333 | -54.30714 | 2024-10-24 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc5fda98-eb03-318e-b6e6-d0a4840ee1f5 | -11.41998 | -54.30661 | 2024-10-24 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0efdc36-d8ea-3a8b-80f2-986285b5c0fb | -11.3148 | -54.33048 | 2024-10-24 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27d6d674-8ab5-3af8-9e48-cca7c013386f | -11.3049 | -55.3424 | 2024-10-24 04:57:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7574201-9262-331c-a518-3e226ce8accb | -6.2171 | -55.65314 | 2024-10-24 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a276fb15-8a72-3947-8eaa-e0c7c568708d | -7.30675 | -55.31021 | 2024-10-24 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13a1933f-16aa-347c-8d70-f5fea3b60c3c | -7.27121 | -55.3483 | 2024-10-24 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62fdc7ff-73fa-37c3-9db7-decc1973a28f | -6.77487 | -55.48534 | 2024-10-24 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f718d29-b952-3c86-bc78-a04a6d088fa4 | -8.31102 | -55.10192 | 2024-10-24 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 165dc594-5fe7-37aa-a875-e3602359af51 | -8.30657 | -55.10839 | 2024-10-24 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f395a314-81a9-30b9-bf24-c715f977dc53 | -8.2977 | -55.09979 | 2024-10-24 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30c7633a-a007-389a-ae42-4019c3301293 | -9.86821 | -55.59053 | 2024-10-24 04:57:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ee0a7b9-d111-3c99-91c5-bb8c1578a3e3 | -10.48332 | -55.59939 | 2024-10-24 04:57:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e8778d0-7051-3854-9f28-629aa70890ab | -10.48276 | -55.60291 | 2024-10-24 04:57:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a51ba01-258e-35e5-b406-e89737f3cccc | -10.08984 | -55.3875 | 2024-10-24 04:57:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58ad27aa-ce81-3052-913a-652fd6daf3b3 | -10.08724 | -55.38722 | 2024-10-24 04:57:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad666139-0c0b-3d6b-87b0-10dc47ba8c23 | -10.08668 | -55.39074 | 2024-10-24 04:57:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f14377c-a7a5-3492-a310-fd300b974d1f | -9.97218 | -57.76128 | 2024-10-24 04:57:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be3b7319-b64c-38a3-9eb1-c9ee75cd83bd | -6.75946 | -59.12 | 2024-10-24 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 5c2f8815-be48-3f41-9580-b4c9af932227 | -6.75545 | -59.11928 | 2024-10-24 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bae3a42a-b849-3bfe-b2bb-d3e2cb63993a | -8.81816 | -47.93975 | 2024-10-24 04:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9bf79d95-64a5-326f-9be2-706b08e224a9 | -9.12154 | -43.14918 | 2024-10-24 04:57:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c16edcf5-ead9-355f-8426-be67e6a76ca0 | -9.64558 | -43.90996 | 2024-10-24 04:57:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 925a477e-e345-331a-a70f-3eb68cd69893 | -9.64006 | -43.90526 | 2024-10-24 04:57:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5f22d44b-2c16-3757-b2b3-94133c3e5961 | -10.60951 | -44.26818 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 65297e60-dfdb-369c-9d65-f08f15f040b8 | -10.60895 | -44.27276 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8dfa15e2-0b3f-3e1f-b3f7-688ee6475eb8 | -10.60842 | -44.27719 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1982b763-9c43-3573-94dd-815cde738893 | -10.60359 | -44.26716 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa9680a2-d81b-3af9-8d3d-857358832dc1 | -10.58301 | -44.2876 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d27dc12e-da15-30d3-8a4c-5b9553a98b75 | -10.58036 | -44.28085 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa9ba5fa-0e0d-362e-9caf-1fe9ef2abc4b | -10.57979 | -44.28536 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9e96b35-b654-3928-97e9-3a3c598d8454 | -10.57923 | -44.28976 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8bf7b83b-aeb3-3b8b-8f34-bcb3f672032f | -10.5776 | -44.28238 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59ebff20-75e7-32be-8d9c-8cda008b3b58 | -10.57706 | -44.28685 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dbfd0dc-3821-3dba-8604-351a97742aec | -10.57654 | -44.29119 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 738050f3-6cfe-3b25-82ea-ead574f89b75 | -10.57384 | -44.28466 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89f23cf9-42d4-3cd1-b7ad-9d3bea47283b | -10.57328 | -44.28903 | 2024-10-24 04:57:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5122d6dd-59b3-3c2a-956e-1a715be56643 | -12.13992 | -43.47613 | 2024-10-24 04:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cfc05d6b-c9da-3cbb-8a54-05a951ce9141 | -12.13785 | -43.4753 | 2024-10-24 04:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b395aaca-c028-3321-96d0-f56ef04a58a5 | -12.13345 | -43.47625 | 2024-10-24 04:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9ad2f8a-42c3-3bea-ac4c-8684f50a6eb9 | -12.13134 | -43.47564 | 2024-10-24 04:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5fa00732-e6e9-36a4-95bc-d7270a1e16fe | -11.95127 | -44.16278 | 2024-10-24 04:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05dc45a6-b501-3e3c-9e4d-b8e4d1974c83 | -11.95072 | -44.16739 | 2024-10-24 04:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9e2b3db-db4d-3fcf-8921-bd277f6c59c7 | -13.73442 | -44.2849 | 2024-10-24 04:57:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ad5051a-5eff-3f97-923b-531a118ca1dc | -13.50976 | -44.4141 | 2024-10-24 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23dfb8d4-4d88-3689-bbe5-84dd006ab9b4 | -13.36017 | -43.93019 | 2024-10-24 04:57:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b56b3481-a9ea-359b-81dc-ac51d85cba61 | -13.35777 | -43.92767 | 2024-10-24 04:57:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37a0777c-4577-3d5c-9fb1-72468b3cfbf3 | -12.69454 | -43.8443 | 2024-10-24 04:57:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc0d27ab-c64e-37fd-92f8-796f628fcdad | -12.68884 | -43.83847 | 2024-10-24 04:57:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 20257d0d-dcc6-3648-8f50-832d85d21204 | -12.68827 | -43.84351 | 2024-10-24 04:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21ce8c93-e07f-310c-b607-f70b13c26e24 | -12.6877 | -43.84851 | 2024-10-24 04:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 30635b72-a784-3d25-83ec-04d62e62695e | -12.682 | -43.84269 | 2024-10-24 04:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eb737047-67ec-3087-9b0d-fb8263a9de9d | -12.68143 | -43.84769 | 2024-10-24 04:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88a1a04d-00e8-328c-b7a7-0e6ab428550c | -14.92699 | -45.11494 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd100d84-ad1b-307f-b489-cbcfcd040b70 | -14.92377 | -45.11318 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f76f689c-5bd9-3983-a41c-0866fc53429d | -14.92325 | -45.11777 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c04b15c-c636-3968-be65-9cf8d6bcfd78 | -14.92274 | -45.1223 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b7a2d06-936a-3a1b-9407-316a509146f9 | -14.92103 | -45.11432 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce2d873c-0293-3033-a75e-52fcdf18b926 | -14.92054 | -45.11892 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f10c4016-c097-377f-9e1d-65eafa78f2f4 | -14.92006 | -45.12341 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b6874cf-dfc1-3b6d-81b8-cf6923eea9a6 | -14.91729 | -45.11712 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 654f360f-f4d0-393c-8c03-ab3ae7b6dfd7 | -14.91678 | -45.12162 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87af2363-959f-37ff-aa75-85d4e2fae9b0 | -14.91459 | -45.11819 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 964e8f34-e498-3f01-8467-6a7e0e64562d | -14.91412 | -45.12267 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9331817f-0ffb-3d88-b8dc-370f977d50ea | -14.91365 | -45.12709 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20d8417f-9f74-3249-a9ff-0065f5c3ad2e | -14.91034 | -45.12532 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5029740d-3cdc-3764-aad6-e9c7697275db | -14.9077 | -45.12634 | 2024-10-24 04:57:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8da9ffb6-90d8-33aa-8687-76f7f9bec470 | -14.48315 | -45.53196 | 2024-10-24 04:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb2977ed-74e4-3cc0-a084-5e6e863135e3 | -8.79764 | -44.72002 | 2024-10-24 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44184df8-c0df-3f03-a930-1fcc0e1bbf32 | -8.79714 | -44.72379 | 2024-10-24 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e1e0a52-eef4-34eb-aab5-b4a8a2302b36 | -8.79664 | -44.72757 | 2024-10-24 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26486923-34da-3e3f-b832-c472b9e34b1d | -8.79614 | -44.73135 | 2024-10-24 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc2a1e38-1f0b-3694-915e-69d450358478 | -8.79563 | -44.73514 | 2024-10-24 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24d03675-bd72-3bfc-984e-470d35bed413 | -8.79513 | -44.73893 | 2024-10-24 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f03c7778-2cf8-3ce4-b16f-3c4d954cf7be | -8.79463 | -44.74271 | 2024-10-24 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 013e41c5-1db1-3ca1-80ad-c2af94ccf2d2 | -8.78901 | -44.74184 | 2024-10-24 04:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4a8f5a4-1251-3e5c-a232-7acc4002469d | -7.92977 | -44.89195 | 2024-10-24 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README80.md)
