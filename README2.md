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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8993c0ed-5b8a-3db0-9ee7-33130c0b003d | -12.5495 | -57.7395 | 2024-12-10 00:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 72208904-ee0f-3611-ae69-def78731089e | -2.9859 | -52.8554 | 2024-12-10 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 167.4 |
| c004dc1c-eb92-32a6-832d-a2658019429f | -2.9119 | -52.959 | 2024-12-10 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c55f1793-0eac-3e42-bd95-71b9075fd46e | -3.1105 | -54.0657 | 2024-12-10 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 8d459e83-0b60-3ae5-bbc4-a63c4f9d51ca | -3.0547 | -54.2478 | 2024-12-10 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 16512ba5-33c8-3cdc-84ab-ea179cb0ef4f | -5.9185 | -48.0449 | 2024-12-10 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 29221817-910a-3963-a1f5-9ac42d0696b4 | -5.9371 | -48.0437 | 2024-12-10 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 06ccc170-ebb8-39c8-9b62-d0f88a0807d0 | -2.469 | -47.6177 | 2024-12-10 00:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 9f6a4db3-bf05-32ab-a341-125fca78800a | -11.5426 | -56.4438 | 2024-12-10 00:50:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 8e9cee02-6a35-349e-8a15-fcf6e230644d | -5.9183 | -48.0667 | 2024-12-10 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c33ace5f-163d-32a3-81b9-4da2ba7ed941 | -6.9161 | -43.4952 | 2024-12-10 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 02c86288-f535-3075-b28a-114f0d0d636c | -6.9158 | -43.5185 | 2024-12-10 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 94ef028e-2b89-3f86-b683-f43d465559a4 | -3.0043 | -52.8549 | 2024-12-10 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| e7bd68a3-2dfb-3569-8061-224f0e4d9fd0 | -3.0044 | -52.8345 | 2024-12-10 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 53b4c826-7174-3b65-b39d-2face7c74b56 | -4.2504 | -47.584702 | 2024-12-10 00:51:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4c0bb11-a1f9-3d05-b305-12243d05a8cf | -12.8627 | -58.2206 | 2024-12-10 00:51:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14950945-f2f0-328a-a644-493a0d79f534 | -9.8432 | -48.1446 | 2024-12-10 00:51:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72050513-4862-31a2-aed2-0e1503e6aaf1 | -11.9507 | -47.836601 | 2024-12-10 00:51:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96125966-7167-3272-bc58-e368e532fcf1 | -10.4477 | -44.889702 | 2024-12-10 00:51:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e395535-b7a7-31ad-af92-ba04e7f9c087 | -3.0739 | -54.0672 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b478cce-0ed7-36c7-893c-1606b940f70f | -10.4575 | -44.887299 | 2024-12-10 00:51:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40c791ab-f68a-3676-b377-f989c1954977 | -14.7965 | -47.412899 | 2024-12-10 00:51:00 | METOP-C | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 23aed29e-7fa5-3df1-8e37-61d23a6280ec | -16.8666 | -40.813 | 2024-12-10 00:51:00 | METOP-C | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8f48a794-adbd-3c73-93d4-6f11af29d102 | -6.6511 | -54.929798 | 2024-12-10 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 117ede1c-5db6-33b8-9a6b-14bb73662b89 | -6.9222 | -43.524799 | 2024-12-10 00:51:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df477153-0398-39f6-820b-df863a9f0e61 | -6.9008 | -47.8414 | 2024-12-10 00:51:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78f9e8a7-e7c4-3f55-89b4-f5e5d8fadbe5 | -3.2787 | -51.083401 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0658f30a-d660-39c1-a7da-4785451a5991 | -3.6863 | -54.315498 | 2024-12-10 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7132add3-9b06-3c2a-8251-b73a5dc0539c | 2.4331 | -60.648399 | 2024-12-10 00:51:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ea7394eb-e7c7-3527-9379-5a1cae342aae | -12.707 | -54.9608 | 2024-12-10 00:51:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d00dba2-8ec3-330b-a253-830c9a613c61 | -2.4782 | -53.713699 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe96fd8d-d0ae-3187-8ce7-2bb699653f7b | -8.2271 | -49.721199 | 2024-12-10 00:51:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7df0fc3b-64ba-3e70-a1bb-31352d8cfae9 | -3.5106 | -54.676399 | 2024-12-10 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 006ee39d-6031-3438-bfa2-d6311b7ae766 | -3.6913 | -49.564098 | 2024-12-10 00:51:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17fd42b2-a671-3ae4-93a9-cded218c3e7f | -3.5973 | -53.741001 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03d15983-2c3b-3abd-b0f5-56f93f2d0a74 | -2.4553 | -53.703602 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ae4cef0-824a-304e-b426-72fb3f9d24c6 | -15.2561 | -53.556999 | 2024-12-10 00:51:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54203916-eb8f-38c4-ad4c-31edf201a6e2 | -4.4539 | -50.586102 | 2024-12-10 00:51:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f88ff827-e623-3438-9d28-d8f1de527e8e | -3.1048 | -53.75 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51e82daa-f7ad-32c3-8390-e71900590401 | -15.8818 | -53.270901 | 2024-12-10 00:51:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ca798df5-2a0b-37e2-9605-1500d0d5f069 | -2.9624 | -53.7127 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20f1f4de-74c8-37c8-9524-e23281528903 | -3.1557 | -54.473301 | 2024-12-10 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 566fb90f-ebff-3add-98c2-8fb9380036ec | -6.6609 | -54.9277 | 2024-12-10 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b3cdd6b-5335-33dd-8766-c00da6a28c43 | -2.99 | -53.0196 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5200e0f-959d-33eb-8713-67e790af3c7f | -2.4845 | -47.614101 | 2024-12-10 00:51:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f784b1dd-40a9-3ef8-8435-08ba294dd722 | -3.0739 | -53.7952 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e248e73-7e5d-39d3-b5fb-b5dbd526e08b | -5.9163 | -48.044102 | 2024-12-10 00:51:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bec092bd-5121-3527-8743-cc73d343f519 | -14.7983 | -47.420399 | 2024-12-10 00:51:00 | METOP-C | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0f0a08cb-569b-3757-9ed4-dcc30565e4d5 | -2.8316 | -53.003502 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a748a1f4-7a51-3aa5-93fc-15071c4048e3 | -3.5235 | -51.474998 | 2024-12-10 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 656164de-6273-3821-b372-f14601f1957a | -6.6629 | -54.9366 | 2024-12-10 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf46ed2c-81a6-3ed3-9501-44030825f2ef | -4.2705 | -50.685902 | 2024-12-10 00:51:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e61befb4-5573-3955-bfb3-72399df412d1 | -2.8264 | -53.070702 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a411c409-5ee4-3bcc-9291-5670563bb8dd | -12.7093 | -54.971802 | 2024-12-10 00:51:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6e66d5a5-3cf1-3b42-8720-5981f7273a18 | -5.7137 | -46.533798 | 2024-12-10 00:51:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7053467a-d0cf-3eae-8f47-f1eb3b00afcb | -2.9486 | -53.1096 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5e574bf-d376-33f4-a6fb-1e9307553015 | 3.2294 | -61.183899 | 2024-12-10 00:51:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b4b0e3aa-4099-3943-9dda-b20e9599ffa7 | -3.2361 | -52.833302 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82a493ba-63cf-3fc7-bc0e-3a4a2829fb20 | -1.4259 | -53.484798 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f24e826c-50ee-3afb-8257-5b9143ba0a37 | -17.4723 | -47.866798 | 2024-12-10 00:51:00 | METOP-C | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 68cca8f3-f1a5-3472-8fba-84cea6b391b8 | -6.6531 | -54.938801 | 2024-12-10 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 822a702b-f5f6-3f5d-a2ac-f6006c4b12ff | -3.6324 | -52.672298 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d8bc3f6-d6ba-3b5a-aa71-e91d00cf43ea | -3.8223 | -52.239498 | 2024-12-10 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0ec5316-9517-3344-96c7-2a4e2258da9a | -3.0854 | -54.072498 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc6173ec-edfb-3846-a623-1c472102ac79 | -3.5251 | -51.481899 | 2024-12-10 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb1a0b06-9dda-3e23-bb8d-b63bfff5180d | -3.1195 | -54.041401 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 756fd485-00cb-38bb-a3f2-1850dcacfe9e | -13.9362 | -44.350498 | 2024-12-10 00:51:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74c38564-4ccc-35a3-a2e0-90ef1f5f64bc | -3.3178 | -51.4781 | 2024-12-10 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c97af59e-13bd-3fcf-b79d-3e12b34b3782 | -3.0722 | -53.787899 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71674b99-332f-3743-87e0-f3e48f0a6db1 | 3.2333 | -61.167599 | 2024-12-10 00:51:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4eb2700d-4e69-3ec3-a331-d29165292980 | -2.9895 | -52.8372 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aabe0ad-565f-35b8-961e-7a88ff6570fd | -13.9388 | -44.361099 | 2024-12-10 00:51:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c5d9e840-6ba9-3dcd-a0d3-1223616c69c6 | -3.5298 | -53.942799 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f88c2704-09e5-3fa2-9b39-12a99191f61c | -2.4716 | -53.639599 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc8728f7-2242-3f9c-9653-624e8e51838d | -2.833 | -53.054501 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 493edd4f-9ae7-384f-be92-c1b5eca59d70 | -3.0723 | -54.241699 | 2024-12-10 00:51:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb60543-0582-3f13-af0f-76bb1592c3e8 | -2.9982 | -53.010399 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32a642b2-9af7-3bf5-ab3a-f6ac1e025dc4 | -12.8495 | -58.2043 | 2024-12-10 00:51:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20b2a4eb-7741-387a-ad0f-8baaa0f06360 | -3.814 | -52.2486 | 2024-12-10 00:51:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 177ce2b6-7348-3a8b-9dc7-485d183989a7 | -6.9281 | -43.507099 | 2024-12-10 00:51:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 69317e26-6010-39d1-953f-6d167030e8f4 | -8.1431 | -54.856201 | 2024-12-10 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eacf774-8941-387d-a344-1a3602addd3e | -8.4413 | -49.6203 | 2024-12-10 00:51:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 802e97ba-3eb8-3468-9231-aa51006643f4 | -5.3853 | -43.09 | 2024-12-10 00:51:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6041073e-4911-3773-b533-428cef52504f | -3.1178 | -54.033901 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a137192-8b44-3a6c-b4f5-b2dc93ae79de | -2.7814 | -53.235199 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 398352cd-371a-32e5-a34b-27dddb65aa7d | -3.9483 | -51.034302 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e2d8785-61ba-3bcc-aad8-e7f4d40ea5cd | -8.4429 | -49.627399 | 2024-12-10 00:51:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6675c5df-f80e-379c-b5dd-f8a7dc59f8e7 | -2.8237 | -52.9688 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1585a4d9-6031-325b-94c3-83c9c9320622 | -3.1048 | -53.2523 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc15d7c6-9193-3c81-95dc-26ce626b7012 | -12.8643 | -51.931301 | 2024-12-10 00:51:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6c955bc-433a-309a-b77d-3f484f514864 | -3.9178 | -49.029301 | 2024-12-10 00:51:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdf35aa7-096f-38dd-8e24-debca5c85421 | -8.6965 | -50.191799 | 2024-12-10 00:51:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1a2fe95-9413-3556-aaaa-c66da1fec61a | -3.5779 | -53.0214 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6093ce-52a9-3d5a-86e4-548000462872 | -5.7161 | -46.5439 | 2024-12-10 00:51:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47b3ab25-65d9-3a6b-a205-15e5e33b4e77 | -2.4193 | -53.6814 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aee015f2-7550-3b45-80e9-76424811cba7 | -2.9963 | -53.047501 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 853394b9-d233-3ba5-a25b-a19de3f316d9 | -13.9485 | -44.358601 | 2024-12-10 00:51:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8725856a-28d6-3ace-9099-48e97f115278 | -3.3001 | -51.625401 | 2024-12-10 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4047ab91-fdea-335a-a60e-7bc369e67d3d | -3.3941 | -52.667301 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82f6e7ab-96e9-3768-a059-0dcf95813e0f | -2.4782 | -53.6231 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
