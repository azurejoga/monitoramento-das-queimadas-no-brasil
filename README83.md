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
| 31db1117-f027-3b00-8a82-7dc8ae0b060d | -10.28467 | -57.70431 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1aea80c9-25c1-3aa0-9168-3e733db6909a | -10.27949 | -57.69781 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11e05407-9781-304a-8acf-f78c655fabf9 | -10.27927 | -57.69793 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39a75612-fa73-3fac-97a2-c97fce989b18 | -10.27849 | -57.70292 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1b17902-c03c-33f2-97d1-a409af2903a6 | -10.27824 | -57.70301 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd3b1f98-ac8c-316f-9777-0b08da9237e1 | -10.22914 | -57.81706 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21bd4884-fbcb-39b0-9dba-dd57858801b6 | -10.22807 | -57.82248 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f5e94bd-a5ae-3fac-bf42-c708f1cb5765 | -10.22374 | -57.81033 | 2024-10-10 04:19:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17055d1b-be97-387a-8a35-87d40369023f | -11.04737 | -57.21164 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d932554-3540-3d80-b722-71eb860973e6 | -11.04341 | -57.20985 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 421a76d3-26bf-373a-ade6-3d3709fbbef6 | -11.04154 | -57.21946 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a247d529-4f46-3a18-ab05-2b23720b2769 | -11.0412 | -57.21041 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 269a652b-6341-3c02-bbfc-a2ffc20e5c5b | -11.04061 | -57.22422 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e696e0a-a42e-3812-b7a9-6302a84a6d7e | -11.04025 | -57.21516 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d6f56f77-0a2f-32d8-a61f-491c832bb82b | -11.03969 | -57.22895 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60ee16ff-3356-3632-8ef5-623a51625bc7 | -11.03926 | -57.22002 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6a664c92-68e5-32f3-8d39-573d1257d74e | -11.03831 | -57.22472 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fa87b51f-15c3-36ea-877d-af1ee0b3d41d | -11.03736 | -57.22945 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d39d375b-ed2e-3ab8-a82e-527a420765f1 | -11.03722 | -57.20871 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e9bfcf63-f604-3c2f-a9e6-c932f80b86d5 | -11.03631 | -57.21339 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4fc16ab3-6ad3-3afc-aedc-edaa214b5df3 | -11.03594 | -57.2047 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6105deda-b396-3175-9d0a-d739275a890d | -11.03536 | -57.21825 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cf09351a-de29-3564-998c-a13dd86516e4 | -11.03501 | -57.2093 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67e22d89-e110-391b-a192-9a7f9781f240 | -11.03442 | -57.22304 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e2c08e5-1236-38fe-9c3f-e8da3896a8c4 | -11.03406 | -57.21399 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0c09353-d5e4-39a2-aaca-3f926205b69d | -11.0335 | -57.22776 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df64890a-fbd0-37e0-a653-1ad9d7320960 | -11.03308 | -57.21885 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4cec57d0-b490-3b51-a1a3-6e06d7f2aaeb | -11.03253 | -57.23273 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8944b3a1-01ad-3067-99a0-43ee17924e45 | -11.03212 | -57.22359 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ec3a11fe-fd1d-3312-ae19-cf66f1f4b4fa | -11.03155 | -57.2378 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52d8ba6f-51ce-3ac8-8a4c-dfcf12148833 | -11.03116 | -57.22832 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b82d45e-7888-3699-a73d-2db7cd111101 | -11.03103 | -57.20758 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b9224e6f-08bc-3e76-9381-35798afedc75 | -11.03015 | -57.23333 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cf316eb-32b9-3d58-8d26-217f9ed4eed4 | -11.03012 | -57.21222 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ef3baae1-192b-3998-905a-31e807d943f4 | -11.02918 | -57.21704 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 04606777-6e9d-334d-a9b4-976fe5bdabb6 | -11.02914 | -57.23834 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2024aed1-d939-3525-beab-02930a6b3cc3 | -11.02882 | -57.20819 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c835d6a6-66dd-3710-941e-3738c682308f | -11.02824 | -57.22188 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 21adceb5-af53-3540-ae41-399424898cd7 | -11.02788 | -57.21282 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 59e264b1-006b-3244-9a6b-3ed3c747588f | -11.02731 | -57.22663 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fb0c9f93-aaf2-3ec8-a89a-7463a3a935f8 | -11.0269 | -57.21766 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c66aa48b-fb7e-31ed-bdc4-403a8b9f8afd | -11.02635 | -57.23154 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 730f176c-c4f8-3cd9-b471-25e1b2518620 | -11.02592 | -57.22247 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f324207-148d-3f58-acd4-e93cf7097d09 | -11.02535 | -57.23664 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35631575-7b65-3f86-ade2-055cd6e63b44 | -11.02497 | -57.22718 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e4e0b14-8d79-345a-8c53-46c50183b839 | -11.02397 | -57.23212 | 2024-10-10 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04f859db-6f65-3430-a205-c0ca8c02d8fa | -6.47337 | -58.43571 | 2024-10-10 04:19:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7842609-7d11-3447-a93a-9154caca3d91 | -6.52971 | -58.42439 | 2024-10-10 04:19:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a24a6e7e-6568-34ca-90f2-2771bb07cee4 | -6.52696 | -58.42536 | 2024-10-10 04:19:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07ac2bbc-6a4f-3b03-8891-32c5ca814934 | -17.65825 | -43.89487 | 2024-10-10 04:21:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44e87409-b52e-35f1-9b6a-af7d12b88d69 | -17.65524 | -43.88997 | 2024-10-10 04:21:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27de0fd8-8df3-3e7d-a06b-4349dcfc1f32 | -17.65462 | -43.89431 | 2024-10-10 04:21:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb011a83-b795-3ee7-8a7f-70eea805fe21 | -19.34691 | -45.84076 | 2024-10-10 04:21:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ade387c7-165a-3ea5-8e63-63eed815c9aa | -19.34635 | -45.8446 | 2024-10-10 04:21:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8acb23f7-596e-32c6-b931-2da76d8586ad | -21.61809 | -44.63998 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ccb97228-30b4-3465-bbd4-572b5171cbc0 | -21.61746 | -44.64455 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1b7039f1-b71d-3aab-9fa1-6d852e16b41c | -21.61685 | -44.64906 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7ff85d2a-9132-3b22-9b36-b08cdc25e425 | -21.61444 | -44.63935 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3cdf7ac5-23c9-3ea6-a37d-e6e680e5957e | -21.61382 | -44.64392 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e016f069-2ca7-31d5-96f7-c9d89627c707 | -21.6132 | -44.64843 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 992e7b79-225c-3e2c-8f54-148c4d6fac6b | -21.61081 | -44.63869 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 850a1e53-6cf9-31ec-a9ae-b935736becbc | -19.34579 | -45.84842 | 2024-10-10 04:21:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55875148-b0ee-365f-94d5-80c49a527ed6 | -19.34238 | -45.84784 | 2024-10-10 04:21:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dec7baee-e1ff-3f28-9b2b-1a31fe7cb42f | -19.34182 | -45.85165 | 2024-10-10 04:21:00 | NPP-375D | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb76942d-9774-3075-b068-3acbe469667b | -18.2491 | -46.98737 | 2024-10-10 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c30a639f-5486-34a6-ab1d-b8fefa99d21d | -14.99542 | -44.40478 | 2024-10-10 04:21:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ec6beae-d37e-38ac-ae69-d9f2824cfb0a | -15.37714 | -41.29141 | 2024-10-10 04:21:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5e6d6d41-ed1d-31b4-81fd-a4de341ab56e | -21.61018 | -44.64328 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5b61a74c-f30b-3dfd-b772-ba4c0e2cd542 | -21.60956 | -44.64781 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c81c2888-ee4b-3cd3-b89c-24d94c473751 | -21.60655 | -44.64262 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7b8b3dd7-cf8c-3c47-9bfb-ff478d90c635 | -21.60592 | -44.64721 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fb98ed36-12a6-31df-ae79-d9b874121154 | -21.60532 | -44.65162 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 37c0d34b-3f46-3304-acca-feee29f14c01 | -21.60291 | -44.64194 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5201fb00-758c-31a8-b464-36e69ed1df55 | -21.60228 | -44.6466 | 2024-10-10 04:21:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dc9653e4-51ad-30af-964a-d2e8e93b9206 | -21.08351 | -43.93837 | 2024-10-10 04:21:00 | NPP-375D | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 396b052a-9a44-3548-b8ab-9238c78d2709 | -14.99484 | -44.40867 | 2024-10-10 04:21:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c4b2462-4e9f-3174-ac09-60acfd2b167f | -14.81519 | -50.80871 | 2024-10-10 04:21:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53c0c780-f0dc-3e84-83db-b1ce9a001ecc | -16.50446 | -50.84712 | 2024-10-10 04:21:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc9deddb-902d-38e4-989e-48106a3ee954 | -16.3999 | -51.0899 | 2024-10-10 04:21:00 | NPP-375D | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daf6f467-6876-34c4-aba8-667b1e078626 | -16.74077 | -50.93548 | 2024-10-10 04:21:00 | NPP-375D | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 517a7314-861c-3014-ac3e-a594c09c39a4 | -14.20936 | -49.74629 | 2024-10-10 04:21:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dba2d328-11fd-3a72-a89a-cb3664889296 | -14.20861 | -49.75069 | 2024-10-10 04:21:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b9a906c-6bb4-3709-a6d5-4926416b1e25 | -14.20572 | -49.7456 | 2024-10-10 04:21:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2661dd70-7d34-311a-bd89-6a134765ef40 | -14.20496 | -49.75 | 2024-10-10 04:21:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| defde4c7-f8a0-3167-917e-427e0d9e0339 | -14.82372 | -50.80524 | 2024-10-10 04:21:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 486873a1-3e49-3e3e-b687-44417a06196a | -14.82074 | -50.79959 | 2024-10-10 04:21:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dbddcfc8-3efa-3280-b1d0-d57360c702d2 | -14.81989 | -50.8045 | 2024-10-10 04:21:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 291ec324-e1fc-3a39-ae43-4fe03c23123f | -14.81903 | -50.80943 | 2024-10-10 04:21:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc8e27d3-efab-3afd-aae2-bd6d2f885d2c | -14.81605 | -50.80379 | 2024-10-10 04:21:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65f2dd33-af39-3583-8209-8e369e95ac6a | -16.99157 | -52.89016 | 2024-10-10 04:21:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fad6cb92-6c25-3b84-9d47-0e3079001860 | -14.15757 | -53.36964 | 2024-10-10 04:21:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4eae0edb-d45d-3a61-b7d4-9ef58554537b | -14.15647 | -53.3713 | 2024-10-10 04:21:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d17a5e14-0dc9-3419-9489-6ec8e8e22834 | -14.15301 | -53.36874 | 2024-10-10 04:21:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f841ce43-3a2e-3bfd-8ef4-feb064439e93 | -13.43248 | -54.6936 | 2024-10-10 04:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 057c9ac3-3855-31c9-b5d2-7db4e32ef1c3 | -13.42745 | -54.69254 | 2024-10-10 04:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78fd5d79-bf7c-3005-816b-ce3bc8261bfd | -21.65281 | -54.4907 | 2024-10-10 04:23:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9ff8ca5d-10c9-3214-9841-85ec9bb6f524 | -2.6533 | -53.3506 | 2024-10-10 04:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 096f0c22-8e16-3e33-ad73-1f1544c393b6 | -2.6533 | -53.3303 | 2024-10-10 04:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0f7262ea-02ec-390a-880b-89ce1251fda3 | -2.6716 | -53.3502 | 2024-10-10 04:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 242.4 |
| a3e8af5d-141f-350f-a0d6-f58dd04217e4 | -2.6717 | -53.3299 | 2024-10-10 04:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 145.0 |


[Clique aqui para ver as próximas entradas](README84.md)
