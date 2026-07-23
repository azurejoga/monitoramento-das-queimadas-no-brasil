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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d135960f-8e9a-367b-b523-32bbea7432dc | -11.95081 | -50.3783 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e8c78588-6995-3d85-8f9c-504718936264 | -11.96296 | -50.3658 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 2f4405d0-c478-37cd-9537-7e8b135155ae | -11.68305 | -50.35289 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8be7800f-8e7e-3779-b21a-fa2649c6f0ad | -11.95522 | -50.37179 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 950e89fc-213a-3176-9151-e52f7fbb3410 | -12.32775 | -50.00511 | 2026-07-23 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdc82e9e-27ac-37ed-8eba-a9f26378f1b7 | -9.12751 | -61.07052 | 2026-07-23 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f435331b-418b-36f5-8029-469a9f01b05d | -13.37607 | -54.29951 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89972e41-77a2-35f8-93c5-87ff1f86ab9e | -11.95136 | -50.37477 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8f1d1770-4c7b-31c8-adb4-4d056c4dec05 | -17.0611 | -45.03874 | 2026-07-23 04:46:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44a4924f-204d-3b3e-baa1-a1639c1830b9 | -12.25131 | -43.57294 | 2026-07-23 04:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f639cd3-11c6-3349-be4c-8b4e6f50ae89 | -11.95356 | -50.36067 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b765d33d-8b41-36cf-8a7e-fda89befee0d | -12.14223 | -48.26135 | 2026-07-23 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5197d03b-facc-3a0f-aec7-72d98eabe2b6 | -11.59873 | -48.02824 | 2026-07-23 04:46:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1af8ce2e-c8d2-30cc-b11a-b107c3344e71 | -11.9729 | -50.3674 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71a83a52-a539-3df6-9dab-3c209f83daf2 | -13.37177 | -54.30305 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47b36bfe-7e0b-308d-8962-c1a105234623 | -11.79149 | -47.10129 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bfb3dd35-ec7e-36ea-bb42-1f3e173c0cf7 | -12.4063 | -50.39705 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fdb2e11-4a49-30b7-8b49-3a96933f2234 | -13.36746 | -54.30664 | 2026-07-23 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4d49b2c-e35f-3a44-991d-02f809fb24b7 | -12.32211 | -46.74004 | 2026-07-23 04:46:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba3f472e-f1dc-3a61-a544-3b74f32e66c7 | -11.67531 | -50.35886 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fa1373dc-cf34-3197-9967-729db14f29fa | -11.5952 | -48.02769 | 2026-07-23 04:46:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfd7da22-9827-3e0b-a514-4e2e1c409276 | -10.85679 | -49.44779 | 2026-07-23 04:46:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad432f79-c499-3148-8a22-a98d6377d5b7 | -11.95853 | -50.35062 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbfa9def-8f56-3bd5-ad52-9be0a877f367 | -11.9613 | -50.35468 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b4885dc6-2d6a-38a4-ba86-d05792e2f623 | -14.30886 | -52.08975 | 2026-07-23 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49d13d1c-e513-3f35-b528-6e9829120b8b | -16.85554 | -49.5589 | 2026-07-23 04:46:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24479046-beb0-31f9-80b2-9e484095ca02 | -11.84531 | -50.33578 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 61076a4e-b416-3cd1-903c-c1655dbdf256 | -11.81762 | -47.33587 | 2026-07-23 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 68fc0fa8-d72e-35e3-8e3a-40e3d3114fd9 | -11.95743 | -50.35768 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b5316e1e-ab85-3eae-be33-4ccdb027cdb3 | -12.03525 | -50.35867 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bd2d517-c96f-3fe3-8124-55621a191d90 | -11.77664 | -47.0991 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a498feeb-b7a4-3a90-81cf-938b70c6844d | -13.99036 | -49.59071 | 2026-07-23 04:46:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25b4cefc-a96d-3330-a818-f5b78608ad23 | -11.68249 | -50.35641 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 046cf060-34b1-37ac-8524-81283ef21419 | -17.73885 | -52.73925 | 2026-07-23 04:46:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 389e2a50-ff92-3239-a86a-0995588d9022 | -11.91933 | -50.38408 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7024f37-906b-35b7-8b1e-9e29eb4452c7 | -11.94915 | -50.36719 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ee6cbcee-ca1e-3a2f-8b5f-c8c7b4edfe35 | -11.56882 | -48.40427 | 2026-07-23 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ccedf3c6-1491-3435-a330-fdb746546fc3 | -11.94307 | -50.36259 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3ca30930-1457-324f-be01-3722d78313fb | -11.00558 | -54.31099 | 2026-07-23 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe239991-c692-375e-89df-8277236f4976 | -11.69022 | -50.35043 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 63e77de0-cee8-3fe9-8adc-0ebae18b4e2d | -12.66174 | -48.21618 | 2026-07-23 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36c72407-5d7e-3ec0-9d51-9c278693b3f3 | -11.78778 | -47.10073 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 98d84825-e846-3082-8d90-026ecb3b1d86 | -17.57827 | -47.50286 | 2026-07-23 04:46:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eac06776-0305-3430-a1a4-efe3adeae6e9 | -9.1233 | -61.06059 | 2026-07-23 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8d6e12c-37f1-35c7-b8ad-dce278a62631 | -14.3806 | -58.33782 | 2026-07-23 04:46:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e29bf12e-9f4f-3a66-9cdf-d156e2bde06b | -15.67107 | -50.28273 | 2026-07-23 04:46:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb9b8eef-756e-3629-a162-25d3ca544171 | -9.1234 | -61.09217 | 2026-07-23 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b8150bd-1e7d-3900-b266-06e3ead5a181 | -11.94473 | -50.37371 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d028a6e-7fdb-3fe9-87cc-3ebbbe184d8b | -12.39745 | -50.38837 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0510a3af-3808-32f7-b1e7-b0554aadf7e8 | -11.33685 | -62.22548 | 2026-07-23 04:46:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 350145f6-be9a-3fdb-b934-f988432ef723 | -11.91047 | -43.84599 | 2026-07-23 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ad8deac7-5286-3166-86d5-b5386c228108 | -12.84776 | -44.38361 | 2026-07-23 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e784634b-b8a9-31ce-8a13-524311c3ab9e | -11.95798 | -50.35415 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dff8a80f-f352-31a6-9f4a-b8615a5b4930 | -11.96903 | -50.3704 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| ef8deb6c-b39c-360e-9cb2-a1d0f587eec5 | -11.58388 | -48.39861 | 2026-07-23 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3bc33796-7fc0-3e97-9bec-bed58f1654cc | -11.67587 | -50.35534 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 092a7434-13c7-30b1-b8d4-3dc2eac946fc | -11.94197 | -50.36965 | 2026-07-23 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32a8fea3-a6ed-3645-96a1-4462a46fa823 | -11.33647 | -62.22885 | 2026-07-23 04:46:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edc2f75a-217d-3aed-a8f5-05ce06c0a054 | -11.79456 | -47.10631 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 08493cfe-a797-3221-b152-a943f3bf6532 | -11.79521 | -47.10184 | 2026-07-23 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 76c072ea-e040-3fa9-b08f-3ec02f5cc1ae | -10.91339 | -50.25857 | 2026-07-23 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e438c01-12a9-3c25-bd23-891392beb538 | -19.72282 | -46.16969 | 2026-07-23 04:49:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 161bf248-4a27-3182-aaaf-043b6cac27e4 | -20.16176 | -43.92256 | 2026-07-23 04:49:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 44495a2f-c5e9-3a59-977e-c805828fb7e7 | -20.1672 | -43.92002 | 2026-07-23 04:49:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a2a8cd22-b75a-35a2-96ce-64f923ba463c | -20.23041 | -42.82681 | 2026-07-23 04:49:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| da91a61e-2a9a-3dce-9451-db757f1ee9a9 | -19.70871 | -48.07912 | 2026-07-23 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4632161-41a6-30c2-9758-eafd0898075d | -19.70802 | -48.08419 | 2026-07-23 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 897dffab-a2f5-3fca-bb11-95a42485bcdc | -20.16686 | -43.9232 | 2026-07-23 04:49:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 14118ae3-e6c6-36f3-bd73-74cc7a632e64 | -20.58312 | -46.91758 | 2026-07-23 04:49:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 63fb1ec4-d900-37c6-9839-73a08e390816 | -20.23592 | -42.82721 | 2026-07-23 04:49:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2002efb4-e867-3944-b352-7956146da695 | -20.16246 | -43.916 | 2026-07-23 04:49:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ef42999f-a9ad-3345-9c8e-5488ef0e821c | -20.23659 | -42.82734 | 2026-07-23 04:49:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f3ecd7b4-cc91-342c-8bf0-5d2cfb7dae5f | -20.16211 | -43.91931 | 2026-07-23 04:49:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 055ae161-c4f8-3d4d-945e-84e3406442b4 | -20.42967 | -46.49128 | 2026-07-23 04:49:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8526a12a-0530-3298-a7b8-2255e31904ab | -19.70482 | -48.07857 | 2026-07-23 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c27cc343-cb13-3136-ba7d-2901ca9a595e | -20.23108 | -42.8269 | 2026-07-23 04:49:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| cc5ab57d-8980-3818-a523-553002aa6eb0 | -20.23076 | -42.8235 | 2026-07-23 04:49:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c3ab0184-f0fa-322b-9516-d91553f2117e | -20.16755 | -43.91683 | 2026-07-23 04:49:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f9de47ae-c6da-3684-9c32-7a1021d5f92e | -20.23141 | -42.82356 | 2026-07-23 04:49:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2bdfce7c-bb0d-3a69-9d11-60e4a95baa32 | -21.06849 | -45.94069 | 2026-07-23 04:49:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c6a97566-8bc9-361a-95c5-b7c5cfa3cb50 | -20.2363 | -42.82363 | 2026-07-23 04:49:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| eb48c447-4e59-3da2-a975-e93e1011fc5a | -21.89363 | -41.17911 | 2026-07-23 04:49:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| abcdd435-98f9-3d1b-8dac-ec08b3619fe9 | -19.16791 | -46.58888 | 2026-07-23 04:49:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69ca34d9-8798-3ee1-b147-3d426c64b943 | -19.55759 | -46.94821 | 2026-07-23 04:49:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 397f9ce4-81e5-34c4-9bdb-35890e27141a | -20.09483 | -44.26098 | 2026-07-23 04:49:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e91b414-85bc-34ce-9c54-8baa83679436 | -20.23695 | -42.82373 | 2026-07-23 04:49:00 | NOAA-20 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 03cc9b0d-62ba-3061-9da2-3c5eadbb46a6 | -11.9641 | -50.3747 | 2026-07-23 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 0adbe8c8-95d7-36d0-bead-b30348f1e00e | -11.698 | -50.3629 | 2026-07-23 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| a3af1335-f90e-383a-816b-b1a91ec817d7 | -11.9451 | -50.377 | 2026-07-23 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| eefe9104-d310-351e-babb-12da1d75ba6a | -11.6792 | -50.3437 | 2026-07-23 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| d18921b8-8bf7-3d8f-9fd4-f64b77e67380 | -11.6789 | -50.3651 | 2026-07-23 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a545967b-0863-3e02-8137-de4b5bf7b5d3 | -11.9645 | -50.3532 | 2026-07-23 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0ffff65c-65ba-3119-a2e9-2b104971017f | -11.7879 | -47.0884 | 2026-07-23 04:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 377ee41b-6a98-380b-85c0-3d3dce788b5a | -11.7875 | -47.1108 | 2026-07-23 04:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| bc3447ea-5ffe-3c43-aab5-23d1c64ced5c | -11.7875 | -47.1108 | 2026-07-23 05:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| eb61947c-8499-3c82-ac4b-4c383f75015a | -11.7879 | -47.0884 | 2026-07-23 05:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| d67b75b4-0f98-31d9-a654-1fab86c33ea4 | -11.9645 | -50.3532 | 2026-07-23 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 0b55bc17-89f0-3314-b829-5802a4ea8cc0 | -11.6789 | -50.3651 | 2026-07-23 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 49cd8dbf-9de6-36a6-891a-3ecec638f49a | -11.6792 | -50.3437 | 2026-07-23 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| a51f0f7f-1eb9-386e-a347-326336ff78f8 | -11.9641 | -50.3747 | 2026-07-23 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |


[Clique aqui para ver as próximas entradas](README17.md)
