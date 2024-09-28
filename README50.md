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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2893d901-9750-3cfd-890a-5c6d9cc3f01b | -11.1835 | -45.59234 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8faefee9-f7ef-35ce-9b56-0b73dd08d202 | -11.16995 | -45.98389 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a7e5e9d-e768-319f-8b5a-37e7a3d90351 | -11.16939 | -45.98739 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4904d790-34c6-3bb5-ac81-39fd141f1067 | -13.34899 | -46.29765 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1dea8529-ab00-343a-9efc-fc15ca27c38f | -13.34843 | -46.30117 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c08f266-68e7-3b17-8284-1c696d9ee02a | -13.34569 | -46.2971 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c984f518-f206-3f48-bafd-a6a47d89eb62 | -13.34513 | -46.30063 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 896dbb0e-f87f-39fa-9dc7-ce78ecf034d4 | -13.34458 | -46.30415 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b69978b8-6c31-3148-a92e-a61665b6898d | -13.34184 | -46.30009 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2033ebcc-bc69-3765-875e-ad9b9c010ea9 | -13.34128 | -46.30362 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 449ac718-670e-3a8b-a8cd-443b50ad5241 | -13.32803 | -46.34479 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc5fea5b-849c-35c4-8b58-fce7dd9a1eff | -13.32529 | -46.34073 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78253430-55fe-37d2-8fbd-ec85a1d651e2 | -13.29133 | -46.31657 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a31f7e08-03d4-34ec-84bb-c45aa6cc269c | -13.28418 | -46.31902 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 17cab10a-8201-3124-b239-5f23cb6cbff1 | -13.28308 | -46.32607 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e7e06d1-2b2e-3838-83ba-b545dd60e588 | -13.27978 | -46.32553 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1abd6ced-0023-3afe-ae44-1ec4cb7fc0ef | -13.27922 | -46.32905 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2b326bbb-daca-3702-aef2-33783af14bae | -13.27703 | -46.32147 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a7589345-1bdc-3d4f-89ba-7688385e10cd | -13.27648 | -46.32499 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ed60a5ad-a0cb-37ac-aa75-c147f839ed72 | -13.27593 | -46.32851 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 60da4a06-1968-3569-b39f-9d095cc334c9 | -13.27429 | -46.31741 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5923bea-b5a4-3b9c-be3a-af117c882737 | -13.27373 | -46.32093 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 32b3d42a-7d18-3fec-8a16-39a806af9843 | -13.27318 | -46.32445 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| efb3ac9a-bf40-3ce9-b76a-cf513a10039e | -13.27263 | -46.32797 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ee36e1ff-d279-32cf-8f0b-899bc128b84c | -13.27207 | -46.33149 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6b387397-2109-3e44-9122-d93be7c9f710 | -13.27154 | -46.31334 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a743626-0657-38b1-a227-e854de6b6f9d | -13.27099 | -46.31686 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0346163-2abd-3fbf-8a23-f0533c1ad4a5 | -13.27044 | -46.32038 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd5c1ee6-c3a5-3cfc-b114-2e1522a926c8 | -13.26988 | -46.32391 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81a9e184-e7fd-397f-94f0-79a910ea893d | -13.26933 | -46.32743 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5318fed-475d-38f2-a1c5-c3de9708e5f5 | -13.26877 | -46.33095 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fb73a83-4f1f-3840-8677-d4c42151e567 | -13.26769 | -46.31632 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7119072e-8b35-3b7d-bfcc-7f376dfa5a8e | -13.26714 | -46.31985 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec8e8bb1-6324-3e6a-9497-2764fc13aa6f | -13.26658 | -46.32337 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1d8ad46-7564-3898-98b0-a6f74385d4f5 | -13.26547 | -46.33041 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bbbdf7e-4c29-3e24-8f11-e7525c51a11b | -13.26218 | -46.32986 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 66434718-768d-3fc3-b1bd-88aa2ab6d7e4 | -13.26162 | -46.33339 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 76b3610b-87f7-3265-a5e9-ac0bbcae137a | -13.26109 | -46.31524 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2fa8f1ad-5b94-3fd0-b799-66ff7fbe645f | -13.26107 | -46.3369 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 66845979-d4ac-3403-b911-3ebfbb60e5a2 | -13.26054 | -46.31876 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 500af198-f7fa-33ed-be7a-5dde1582d876 | -13.25998 | -46.32228 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 335b8e0f-3d14-3563-9260-b9b0c5506d36 | -13.25943 | -46.32579 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2bcf9387-07d7-30a3-aa5b-68a1a00ade28 | -13.25888 | -46.32931 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3801a98d-85cb-3e2a-868c-d9d9f539ff2c | -13.25833 | -46.33283 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eca6a550-b6df-37ef-8ab3-ca2aa9956684 | -13.2578 | -46.31469 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88cf8581-e1f2-331e-b2f3-b049114b322d | -13.25777 | -46.33635 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c138ae94-80fd-396b-b1a9-e298c19ff37f | -13.25724 | -46.31821 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2dd1391e-40e0-3999-be42-cce4d83a8b6b | -13.25669 | -46.32172 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0e17b0bb-a543-3680-86a1-5aefe7bc64fb | -13.25614 | -46.32524 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d23502ec-5b06-3579-a0e1-a1b4e7131166 | -13.25558 | -46.32876 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d136938-e83d-307c-9d2c-f25672c68227 | -13.25448 | -46.3358 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a5f2824-a651-31c0-bb04-30aee212b968 | -13.25118 | -46.33526 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9332048f-cf8a-324f-a851-753e6fda3ac3 | -13.25062 | -46.33879 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 956df3ab-8d6b-34f3-971a-51e474310f23 | -13.24788 | -46.33472 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56c15ac7-0245-332f-baa8-1519f57dd4f7 | -13.24514 | -46.33065 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3923aeb8-4827-346e-9c9d-94e1ad75ebd5 | -13.24458 | -46.33418 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28a4c664-1b37-3d36-945d-d1adc85a770c | -13.18133 | -45.58321 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3cae4dc-b52d-3cd9-8edc-d093297131a7 | -13.1757 | -45.4659 | 2024-09-28 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0703487-450e-3a5a-baf4-ef3c1cf71f8a | -13.17515 | -45.46946 | 2024-09-28 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 226ffd4c-584e-3631-b6d3-cafbaa35635f | -13.12857 | -45.37443 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 09f8ae35-6404-39c9-8bdf-c4e351885fe1 | -12.96779 | -45.42504 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8d08428-cfcf-3896-9756-f47db6b00dc0 | -12.93398 | -45.35767 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1438805b-7f91-3368-a442-4738d60ff4d5 | -12.7446 | -45.57052 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4d9d250-af20-3a25-aba7-9bec1fe6b247 | -12.74129 | -45.56999 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 106b8b16-14db-3eee-a049-a52adc400325 | -12.73853 | -45.56592 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6558bf17-a132-321f-9fe0-673fddbba9ed | -12.73522 | -45.5654 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c10d63e0-44cb-3a3d-b9c6-a6a2773f3e4a | -12.73246 | -45.56133 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5bb61588-0444-35df-9a98-d9276b79f4cb | -12.72916 | -45.5608 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59edcacb-77f3-33b5-9b55-21e71d4f5790 | -12.72585 | -45.56027 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a48069d2-30e4-3d8d-8359-b08891e1ec75 | -14.17378 | -46.44058 | 2024-09-28 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b3b5217-502d-30c1-a70d-829b13b52897 | -14.17322 | -46.44411 | 2024-09-28 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7102082e-51e0-3606-a6a4-67400522a57b | -14.17267 | -46.44765 | 2024-09-28 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7857b3c2-88f8-35e4-afcc-bb08b03e600e | -14.16992 | -46.44357 | 2024-09-28 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 208ae9b2-135c-350c-8901-3e39da6dd0cd | -14.16937 | -46.44711 | 2024-09-28 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5c61f6d-9bd4-3fca-ad3d-bb79d273e492 | -16.49527 | -45.98447 | 2024-09-28 04:21:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cddfd029-aa7c-303a-b105-ecf67aaf98ba | -16.58354 | -46.93295 | 2024-09-28 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7ccf2bc-514e-3c5c-b95c-66a34c9c184d | -16.58298 | -46.93653 | 2024-09-28 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2a2ecd2-9f37-3103-b6a6-66e6f9113391 | -16.5808 | -46.92881 | 2024-09-28 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f613b7c2-1044-3d9b-a21f-e096d70aa89c | -16.58024 | -46.9324 | 2024-09-28 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 705a2c09-73fc-3348-892d-bfae8b09616e | -16.5775 | -46.92826 | 2024-09-28 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93196233-3d52-3371-922a-786c957389cb | -16.57694 | -46.93184 | 2024-09-28 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51315b94-5c2c-3223-b9dd-dc0b944ce437 | -16.57582 | -46.939 | 2024-09-28 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3097053-2bb7-38ab-8b32-2538d2c9b646 | -16.57308 | -46.93486 | 2024-09-28 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9178e1fa-1d8c-3023-95e7-f42b49a23759 | -16.57252 | -46.93844 | 2024-09-28 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 318d5566-c3e1-333e-896b-34e4332aee1f | -13.48233 | -48.57901 | 2024-09-28 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 698073a1-aaf8-3143-8a8d-a7f5bab3d53d | -9.15525 | -46.38442 | 2024-09-28 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c2c84f1-9d61-3f54-a30e-5c10b758565a | -9.25411 | -45.74452 | 2024-09-28 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbc10a96-66ba-3b27-8468-31ad39a2a56f | -10.89663 | -46.41769 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ab2893f6-e3e7-38a1-814b-58326380f679 | -10.89607 | -46.42123 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed1d3f79-3a38-3a99-b1ec-e00c1ed07836 | -10.88065 | -46.38966 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfa0237a-f4a5-37fb-b2e7-2ca5deb08a7c | -10.87949 | -46.41843 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c796ba0-4746-376e-ba86-6001715068f0 | -10.86077 | -46.38646 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 71a105c2-19e1-35e2-a623-7f84cdbd0ccd | -10.85017 | -46.43172 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 636724d0-3e25-3d9b-b772-2dfa0ba7e925 | -10.84961 | -46.43523 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 868ecebe-be6f-3b43-ba5f-8e1b7665ee76 | -10.84909 | -46.4171 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fca4d50-1a6a-33d2-9332-b2eebf9e8283 | -10.84797 | -46.42414 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03f87259-7957-311e-a03d-fa89e34840fb | -10.84741 | -46.42767 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f82e9f6-5c24-382a-b59a-c0795423499c | -10.48351 | -46.36107 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d25e5f4c-ab5c-304e-acb6-99296aff77ee | -10.48019 | -46.36053 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9fcd292-8da8-3892-808f-59db301b892e | -10.64952 | -46.02422 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README51.md)
