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
| adf6a99a-8dfe-3a14-96c5-5ec91068b257 | -13.34047 | -45.49316 | 2025-06-07 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6e6d817-87af-3d04-a231-25660efa4db6 | -12.33214 | -52.47707 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2b68c09-4c89-388b-aee7-520a8468496d | -11.38341 | -56.55258 | 2025-06-07 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09548c12-e953-3711-85f6-5f5d894ced67 | -12.52959 | -58.35695 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3e0c57f9-1d79-3436-b372-507c20711cb6 | -14.73107 | -45.08501 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d61e66d5-d0c8-3eb1-ba3c-4934b7e8de87 | -14.21654 | -45.4877 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4855b019-a5da-3090-a969-60c426e747ed | -14.9276 | -46.00513 | 2025-06-07 04:23:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9365d069-5556-3d00-bcc3-109fedd0d7e7 | -12.7051 | -58.02567 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8947c807-9626-355d-9dd2-044a1db11266 | -12.96762 | -46.77124 | 2025-06-07 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09cb9b12-85d4-32b4-bc72-ea63740fe1a3 | -17.26048 | -42.65561 | 2025-06-07 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a2a6c7c-0826-343d-a332-db54536f55bd | -15.82966 | -48.26004 | 2025-06-07 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f096c496-3342-3402-925c-87dd09d8e9d0 | -17.81276 | -51.01264 | 2025-06-07 04:23:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 759990bc-dd2d-3e05-934f-bf025698be9b | -13.07635 | -49.24125 | 2025-06-07 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42db18fb-614f-3bc0-b28a-8f9713f37e0f | -12.33061 | -52.4857 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d636de1-8682-3618-aedb-a2ae87920f2d | -12.32598 | -52.48414 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3578d57-c1a4-3d2b-a25d-fe67201508b7 | -12.70888 | -58.24277 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29cae61a-a6a2-366b-980a-201cd29201a8 | -11.88926 | -56.40948 | 2025-06-07 04:23:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 276643bd-bc20-3952-85d5-f213a2883e55 | -13.28837 | -58.01338 | 2025-06-07 04:23:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5fe56ee-8164-3d4b-88c9-5e59d86f1952 | -12.32414 | -52.47112 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0d9baf8-8eab-3ded-8cc7-de31fca4f309 | -10.6719 | -57.6298 | 2025-06-07 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fd8fd40-a09c-3965-ae56-460380010365 | -17.4547 | -48.17644 | 2025-06-07 04:23:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05de5661-03bf-3b53-8d18-e3c7b5c328c7 | -12.29068 | -50.10848 | 2025-06-07 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ccc08a53-f3ac-3f78-a7a5-55759a492530 | -12.96705 | -46.77481 | 2025-06-07 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb37ba83-6d39-3192-9490-06460129fc7a | -11.36432 | -56.55743 | 2025-06-07 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb66e274-8591-3778-8607-a041d8428f85 | -14.88619 | -48.11111 | 2025-06-07 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed9072b8-7a2d-3cb4-ab1f-6371b5755e9c | -12.28391 | -50.10245 | 2025-06-07 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 13bdbe38-deae-3026-a8dc-5482b77c0165 | -14.23334 | -45.49042 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 330fff94-6836-39e9-a1c1-d7abffd7e639 | -14.72938 | -45.07317 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1241745-1f96-35f6-a989-49cc336fd244 | -14.88281 | -48.11048 | 2025-06-07 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 358a0c49-0521-3d8d-866a-7180f1e54b13 | -18.82135 | -46.43566 | 2025-06-07 04:23:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 950fd511-a396-3e60-bf96-19dd1c52a087 | -17.26438 | -42.65625 | 2025-06-07 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7ea59de4-57a0-3969-aa22-47b919fca00f | -14.03911 | -55.13948 | 2025-06-07 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff1cb392-c7f1-3360-ab59-0e214c211d55 | -14.04472 | -55.13771 | 2025-06-07 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9d97a39-2c01-35cf-a399-86df97856c57 | -12.33652 | -52.47791 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1321e3b6-2978-3211-9283-09310a832413 | -12.87716 | -52.20528 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5a6df66-b770-30b0-b2c0-7a5958ebcae0 | -12.53067 | -58.3517 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca37e8f8-01cd-3a6c-915b-b10579cae33b | -14.02901 | -55.13728 | 2025-06-07 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfaf23fa-296f-322c-98c4-a43fda3f952b | -15.08007 | -48.94612 | 2025-06-07 04:23:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6dab3c4-bc8c-3dad-88e8-538cd6f48bdc | -13.96033 | -50.10228 | 2025-06-07 04:23:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7840d66a-c6c3-3dc9-8b9e-cbd937a858b1 | -14.20143 | -45.49645 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae85cdc2-f4eb-3693-9aa6-8aeca9914e1b | -12.32622 | -52.48487 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 138c80f9-1018-34eb-a48c-285a4afe8d7f | -12.33633 | -52.47719 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53b3e857-a2b4-3683-867e-b00562fbd495 | -14.72881 | -45.07693 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37c1cbe6-0c55-3450-80c7-18381e3d89a8 | -14.73788 | -45.08606 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6133f734-4149-3f7c-a25d-736ac4cae3f0 | -13.34103 | -45.48957 | 2025-06-07 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f71da2cf-7774-38aa-ad3d-df702fbd289b | -14.22158 | -45.47734 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d605d7b-0a75-3b8b-8249-5fe634023e69 | -12.28111 | -49.52796 | 2025-06-07 04:23:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9745d687-9a7e-3b4a-b4c9-e4319942f72b | -14.02959 | -55.1343 | 2025-06-07 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8577556-768f-3e78-b21d-5e4700e999f5 | -12.32757 | -52.47554 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4128972d-9242-357e-af33-c20afc4703a8 | -12.29227 | -50.09915 | 2025-06-07 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8e37c60b-d0e8-3bf4-bb83-16aa29905aaa | -18.96043 | -45.37734 | 2025-06-07 04:23:00 | NPP-375D | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35d479fb-6e17-3c4f-9245-6874d42a91ce | -14.03076 | -55.12834 | 2025-06-07 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1d3463c-8fe1-36a5-aeec-ac3096735b88 | -16.06559 | -43.65299 | 2025-06-07 04:23:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f9457d0-d391-3b7f-b187-1e9535434f9c | -17.27287 | -42.65235 | 2025-06-07 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f79a686b-36e1-3008-a727-4e5364258907 | -12.78118 | -48.71965 | 2025-06-07 04:23:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8aa74d74-2c57-38f3-9f03-f35232691d98 | -14.73902 | -45.07854 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a8d47fd-fb7d-3eec-a6bc-75f2983108c6 | -12.28311 | -50.10712 | 2025-06-07 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 40e1f9db-5971-3f83-864c-83c9c8411fb8 | -12.8779 | -52.20117 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 400c15b7-6b24-32c6-bffc-505572eba96e | -13.07207 | -49.24479 | 2025-06-07 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bf58576-2e01-314a-a477-3ef7cbdc3d22 | -11.88849 | -56.41344 | 2025-06-07 04:23:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84ddd832-64d1-35ea-b687-e7e0257f20ad | -14.22046 | -45.48461 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0487f5ec-7ab8-391b-99a6-72389e966611 | -14.21766 | -45.48043 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e59474a-88a8-3cae-af41-985e99d803d2 | -14.74638 | -45.09887 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6248a73-1511-3ecf-8fd2-4f2b745fb15a | -12.28477 | -49.52863 | 2025-06-07 04:23:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 862ea8e5-3592-3d93-b4d3-d0d2e10a462c | -12.96152 | -46.76655 | 2025-06-07 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b11b7fe-8bae-3820-8743-f99d5cbc3be8 | -12.28769 | -50.10313 | 2025-06-07 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b6283ad-d8ea-351f-9ff7-173a0de3f11b | -17.60554 | -49.29352 | 2025-06-07 04:23:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed1eac05-dc8d-3dd3-a30b-43f99eeb9625 | -14.20479 | -45.49699 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2e17120-a1c9-392a-88c4-c63f883cc9bd | -12.20937 | -49.63757 | 2025-06-07 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d39e898-f88e-352c-aefe-fa0c927754a0 | -14.2395 | -45.49514 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85ce7b3a-a7af-3712-bd67-a926b2ec204f | -17.6385 | -44.54635 | 2025-06-07 04:23:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41f44ad4-2ef2-3095-ba06-e96f55a32d9d | -11.54251 | -56.44127 | 2025-06-07 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a4bd2ec-5071-35bb-bb7f-e80da39d2985 | -13.09731 | -52.28314 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5d84a47-e339-3bbd-bacd-5479374b7314 | -11.38258 | -56.55679 | 2025-06-07 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 593e5f0d-25f8-3e6a-8f31-2d3c68d8b70a | -12.7805 | -48.72365 | 2025-06-07 04:23:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b7077ba8-903f-3800-b0a7-81342ec9a976 | -12.47845 | -54.4249 | 2025-06-07 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7202438f-6d53-362f-a1dc-202e2284ac68 | -14.82002 | -40.78416 | 2025-06-07 04:23:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| adf35ea0-ea2c-3a29-9565-a90640582708 | -17.78088 | -42.80945 | 2025-06-07 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fca8d78c-0f66-3b73-bcf3-915957c2a281 | -12.33554 | -52.48149 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5568e48-a724-37a7-85af-de76ee7f7b08 | -12.70615 | -58.2434 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3691f36d-6d50-3362-b937-c707fbf3774a | -12.3329 | -52.47277 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5f831e5-0a6f-3357-b808-90151fc20a21 | -14.21822 | -45.47679 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8004bed3-12b0-360d-9f21-6c729e5675e6 | -14.74581 | -45.10261 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bca59250-bfdb-36ac-a24e-c5205fe75713 | -12.28849 | -50.09847 | 2025-06-07 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4fdd0ce3-e668-3ec1-9fab-f9902cdf4382 | -12.33712 | -52.47289 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3b17812-888d-3aa0-acb9-065206620bbc | -14.92815 | -46.00153 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35d5202c-95c9-3408-8340-e6804ec398e2 | -12.59951 | -48.37523 | 2025-06-07 04:23:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 980ba4f3-5123-3b77-8691-551963564f7a | -16.03696 | -43.72578 | 2025-06-07 04:23:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83856a9e-180b-3381-a567-deda84e3ac90 | -12.52317 | -58.3559 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70272cd4-6e4b-3476-a843-a3d2be42aa3f | -12.33036 | -52.48496 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4552368e-310c-3adf-9d9b-ec0127a5281d | -13.51774 | -56.56335 | 2025-06-07 04:23:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 010e75ef-4e5f-3710-98c4-c9d350be0f88 | -14.23614 | -45.4946 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ce7a241-2d7d-33aa-adf3-73b7874544c7 | -11.56755 | -54.5665 | 2025-06-07 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04272e47-dee1-3203-afb7-41f5ea659a0c | -12.28481 | -57.26932 | 2025-06-07 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 158c5e2c-2c4e-3b51-afd9-e7b9f07cb205 | -13.09658 | -52.28725 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba0ceee1-8f77-354f-88d7-dc9e365e2664 | -11.36926 | -56.563 | 2025-06-07 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3654d10b-5d04-3743-aa17-9d9d1f236889 | -12.77767 | -48.71905 | 2025-06-07 04:23:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 066ae43d-c835-3270-967c-63bd27ef7e9b | -13.29266 | -57.93847 | 2025-06-07 04:23:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24f191ca-d5a1-3c03-a92d-ac6bd962f246 | -14.7254 | -45.0764 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24cb40e1-0b16-3aed-aaef-8f3e5cb3c6f6 | -18.3808 | -47.25807 | 2025-06-07 04:23:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README17.md)
