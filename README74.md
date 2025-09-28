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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db6473fd-9a96-384e-a88c-cc3c8975b313 | -13.63816 | -48.06334 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c0a9421-a571-3a9c-8b5e-77ccf50fbabf | -16.40215 | -47.01809 | 2025-09-28 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 747a3d1b-f962-3d14-b262-5f1c1db8fc4d | -15.5361 | -47.91246 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f7211b9-cb48-35f5-a5c2-da96590a6d62 | -19.93839 | -43.62136 | 2025-09-28 04:27:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 144d54a4-1969-35fa-8e09-930c340f2f5e | -19.32188 | -43.81665 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8d91cf5-82be-3c1b-9c76-68a093a9d162 | -13.77709 | -47.87144 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22daacba-9848-3d58-9e23-dedd86ba1de5 | -15.29127 | -49.49057 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99f88599-2df5-38d7-a189-9e4175ac4cec | -15.27174 | -56.80623 | 2025-09-28 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10380d58-76f1-352a-a326-eb713c3dfc13 | -15.08594 | -48.33585 | 2025-09-28 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2d00a5c-5f88-3c8e-a893-6c5035f7f42b | -13.59119 | -47.32552 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9e24ca9-6dfd-3e8a-b2ee-a9e199d7aa0b | -16.96829 | -53.69994 | 2025-09-28 04:27:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 931e367a-bfe8-3c2e-bba4-8c0fde4c54ec | -14.53537 | -48.42295 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f22877c3-1573-308a-bfcb-276bbaadafc3 | -12.76817 | -50.49349 | 2025-09-28 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efa3f1ab-18bf-3467-9090-291ae3813704 | -19.32096 | -43.82394 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0cd6623-3111-3f20-87ed-88e402a98d39 | -17.71806 | -46.70021 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6215dbaf-4942-3314-800f-99a1631fe963 | -19.31688 | -43.8235 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88ef5f38-071b-3958-9a86-9e6c1cbfce45 | -15.01469 | -54.98534 | 2025-09-28 04:27:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a9b771e-e067-339f-87d2-7ce034914671 | -13.56948 | -48.28112 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4fb17fe4-316b-382b-9ab6-86de473274b1 | -15.28178 | -49.48534 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4774e229-7466-3600-bf19-21c8fa411d9f | -15.84415 | -56.40195 | 2025-09-28 04:27:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18e17aaa-5f83-32a7-94e5-d365b432fbdd | -13.01539 | -49.46167 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 94d66346-7c25-3e77-b2c0-f8e4c4f09c3b | -17.19847 | -56.35859 | 2025-09-28 04:27:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e362d7d4-22ab-3c23-a524-87b15553edbf | -12.99471 | -49.4386 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d067ea2a-0869-31fc-9fd4-683c9d0466d3 | -13.59613 | -47.2937 | 2025-09-28 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78bc8c89-2ae0-3eae-a31f-a20136d5ffd7 | -12.23343 | -60.84531 | 2025-09-28 04:27:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91e5ba6d-3719-37b8-a439-1daf2c629f81 | -13.58399 | -47.30618 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b784b6c6-7126-3db6-88b4-c25cb9f3647d | -15.18454 | -50.09838 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8558a2e0-8a58-397a-9005-2c8fe94e548b | -15.20754 | -48.06011 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d7b1c56-9c88-30ba-8cb2-a6e461261e96 | -17.72036 | -46.70864 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8543fe42-e3c6-3fe8-9468-8c893f4fb634 | -15.24111 | -46.45467 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7fe524c-01a2-3578-ac65-b877206918cf | -15.33136 | -47.89754 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 803b5d4c-b52e-3c9c-b862-399e89f95dbf | -20.71061 | -45.01499 | 2025-09-28 04:27:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e719e399-08fb-3036-a59d-10d367d2c0c2 | -13.17376 | -47.43241 | 2025-09-28 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f57ddb2f-5100-397e-81e9-dc04eec67680 | -16.40153 | -43.71743 | 2025-09-28 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 083856fd-7167-3992-8acb-e6aabdbdcc34 | -15.35337 | -50.13863 | 2025-09-28 04:27:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3626c7d1-b87c-38a7-b1c3-758f3bb15d99 | -13.31851 | -47.31029 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 89415f4e-c1d3-38ef-b358-c03f0edd7977 | -19.2456 | -44.08447 | 2025-09-28 04:27:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 879463ab-efff-3f98-9011-66374c3ae7c1 | -12.95089 | -48.91383 | 2025-09-28 04:27:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec8e8044-8108-37fc-8547-b6006d440f87 | -15.5527 | -47.89321 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06ece15c-c5f8-30c1-81f2-41b261a68cdd | -13.62923 | -48.09822 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83948453-8f11-3a8a-bc7f-bf3770e6fe4b | -13.61132 | -47.32515 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f64638f-b725-339d-9ee0-8a1ebb7c9684 | -16.17901 | -43.65025 | 2025-09-28 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f04cc95-1bb1-3261-a8c2-8e5277920d32 | -15.02701 | -46.96796 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1224df0-9996-39c8-9687-a8b2942398a6 | -17.24729 | -43.87006 | 2025-09-28 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 428f2bac-547e-3a89-9790-bf27137bcdea | -15.29363 | -49.47607 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e16326e0-39af-3299-b9a4-1575254043ea | -13.62347 | -47.31264 | 2025-09-28 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d6bd00c0-1efc-355a-b3b9-90a2b6ae37a5 | -18.17887 | -53.32441 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 06031c3a-c507-36c5-9a7c-e125d33fac47 | -15.31868 | -47.89176 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ba8acc2-c3ec-3873-9bf7-759ea0f7a929 | -15.42559 | -48.22729 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e40d3614-7bea-3d7c-bb39-32249d78afe9 | -15.69875 | -49.13738 | 2025-09-28 04:27:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b04001ee-9d70-3720-89f8-c7b3f1135e5f | -13.62711 | -48.06877 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e22db54-eca5-3b3b-ac1e-f54b4364b4a7 | -15.6233 | -48.35193 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e466689c-37ce-30f6-99ca-68f605e5a39b | -14.83457 | -45.57243 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 544a1d1a-bbc7-372d-b228-c9ad955b554e | -15.53558 | -47.89403 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09567af0-6ee1-3aba-8ac2-01c8d0204212 | -13.78643 | -47.89841 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e4f6da3-395d-332f-be53-971fa702c160 | -14.3204 | -52.92443 | 2025-09-28 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8be2e99-9ab2-300c-8b0a-004ee0724dc1 | -13.7616 | -48.31217 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 916eb919-7a6e-3ea5-9211-539363f9e837 | -17.75513 | -48.7648 | 2025-09-28 04:27:00 | NOAA-20 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fafd4e6-4f90-34e8-9096-2eb1c61ecb5a | -15.60042 | -53.16367 | 2025-09-28 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b739d1f-7334-316e-a669-8ff341824891 | -13.79246 | -47.92484 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e988f19b-c11a-3288-9553-6b03a54bbbd4 | -15.0865 | -48.33228 | 2025-09-28 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6923b2b5-d877-3952-98bc-e9ec563df57a | -13.60662 | -48.09081 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f7ca6d0e-bf10-3038-ad36-cd9993865ae6 | -12.65355 | -51.66998 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c092207-8b9a-39f0-9d40-f07d6ccc8261 | -19.12721 | -46.65989 | 2025-09-28 04:27:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38932018-c935-3e32-8169-3396ffbb8fff | -16.0887 | -39.41061 | 2025-09-28 04:27:00 | NOAA-20 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9781347c-780e-36a8-8413-e9c9e956d548 | -13.59174 | -47.32199 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc453e85-7332-35a0-a98c-99c8ba6c7ec6 | -15.81759 | -41.8946 | 2025-09-28 04:27:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a71beaa-c222-337a-ab9b-69293edd0027 | -17.43085 | -45.8071 | 2025-09-28 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7835e3d9-9396-3121-8386-dbf2e29859f8 | -13.77375 | -47.89268 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c413b72-6a12-3dbb-a9ca-a1f1a7b5a4ef | -11.81072 | -55.13478 | 2025-09-28 04:27:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d222cbc0-ccc4-3ddc-b6af-c75239a9ee90 | -13.28673 | -46.44164 | 2025-09-28 04:27:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 970bb5ed-ac71-3118-ad7f-ab4beba4f5fb | -15.32474 | -47.89643 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d011e73-7f62-30bc-802e-17ba04b0b3ae | -13.51489 | -47.4005 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b6584e9-cb96-3d84-92b4-54c2b67f3aa1 | -19.32772 | -44.39746 | 2025-09-28 04:27:00 | NOAA-20 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b879cb6d-db66-3b9a-adde-30103c75abd4 | -13.18701 | -47.43457 | 2025-09-28 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3298cdee-7ab7-3249-8856-797dda9f7746 | -13.80407 | -47.91586 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 994f1798-0930-3c54-94bb-e93adedff364 | -13.51544 | -47.39693 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd2f3adb-58cf-3544-939a-fb6984084478 | -12.76463 | -50.49287 | 2025-09-28 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9cf7ae54-4bde-3efc-bbce-32e07ff3e396 | -11.86962 | -56.87571 | 2025-09-28 04:27:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 349b275f-7d9d-3610-96d2-b71fd8d31c02 | -18.39128 | -44.53726 | 2025-09-28 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d3da153-505f-3e5a-9542-623245d579ce | -15.96515 | -50.87367 | 2025-09-28 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ce4e399-0192-3eea-8488-8c2a6fc41c69 | -19.49206 | -41.10344 | 2025-09-28 04:27:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| c806cc1b-5780-301f-8178-e9b76be4c44a | -15.21635 | -48.0689 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1edf0f5-f00c-3f96-9bf9-54e6a3f11c26 | -13.25241 | -48.45776 | 2025-09-28 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17c6848e-3dc1-3ff2-8a2d-8654b596537f | -15.32805 | -47.897 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f326d0d9-bfcc-37da-ad66-a54fea35a017 | -19.32919 | -43.82433 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0a7db28-8802-3a4c-827b-851eecfcaebc | -13.00029 | -49.44717 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33349594-0a58-395c-bc69-bb614e4b70c5 | -18.06147 | -42.39573 | 2025-09-28 04:27:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 73ccf4c8-3d40-3985-9620-c6e4642bf606 | -15.13867 | -48.00113 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80031810-fd72-3822-bdd3-7ec7d2e7878a | -15.59837 | -53.15256 | 2025-09-28 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 31fc8d9d-ea90-338e-b8e5-1996a3fdc127 | -15.27954 | -46.45601 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91f40ea1-7360-31e7-b5f9-c209e62de2fd | -17.19702 | -43.38656 | 2025-09-28 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d5ffdd31-460c-39c9-b639-71986989568f | -15.29639 | -49.48029 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c2b60ab-c721-3c8e-98ca-da5b14d330c9 | -13.60718 | -48.08728 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cfe8e82b-d6f2-30bf-8b53-bfacdebb91bd | -15.81374 | -41.88966 | 2025-09-28 04:27:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55f27087-a4ce-3721-89c5-f742ad48b650 | -14.53869 | -48.4235 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d3a85367-c613-3991-aa20-602b1c258f48 | -14.06928 | -48.8297 | 2025-09-28 04:27:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3abb5a2-d162-3bb2-a6a4-68d088f2c46d | -20.54474 | -45.10148 | 2025-09-28 04:27:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 012b065b-e58c-3388-b6d4-a2d0f801ce0f | -17.95649 | -46.24216 | 2025-09-28 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a98ada5c-85c7-3cdb-96ce-fae4576d12ca | -13.79026 | -47.91721 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README75.md)
