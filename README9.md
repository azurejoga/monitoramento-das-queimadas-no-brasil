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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d731c39d-fd1c-351c-ae65-9d7922b737cf | -13.22674 | -54.51166 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 454b720c-4d95-3be8-98df-110d77c5ff08 | -17.92871 | -51.34108 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19138831-d554-35bf-8b87-8ee462ff30a0 | -13.22749 | -54.50723 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0671fe0-b05f-364d-a9fe-a622a52d5916 | -12.72468 | -54.19221 | 2026-05-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e61ce766-c3ff-34e9-9f80-99588f39e67f | -12.72321 | -54.2009 | 2026-05-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1683c31a-f67a-3acf-8137-c403210fcf56 | -13.20032 | -54.51146 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d39d936-1a86-3fb7-9a97-385786299780 | -13.21575 | -54.50964 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a806edd-2f8a-301c-9687-758732807e85 | -17.93149 | -51.32294 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ce54a683-5c67-3580-a61d-4fb7d4cd31a6 | -13.21133 | -54.5134 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95ec5b90-5ca5-3a75-8d1c-ac608fdd7c7f | -13.36918 | -54.27021 | 2026-05-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8333ff8a-1f60-34e8-9578-a4f9ca8d3ee6 | -11.79622 | -57.01215 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a96e8d7f-fa0d-3770-8f11-597478c0a0e4 | -13.21941 | -54.5103 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 144a9b17-1905-3d53-914c-1d6d9f75dddd | -16.16382 | -58.47647 | 2026-05-28 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4bf4b551-aaa1-3ba8-b017-610e34bf48b0 | -13.21866 | -54.51474 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aec44010-2c0b-34b5-9971-bb137ed5580d | -11.63259 | -56.86097 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 26d03393-0273-3ba6-92c0-078f6e496e1e | -15.74592 | -54.50969 | 2026-05-28 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b862849-85fb-3082-b9df-accb44a28a46 | -13.2069 | -54.51719 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6223157-85db-3991-ade0-db14b5e70e6b | -13.20108 | -54.50704 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b64064e-bc41-3019-acbf-9468667e876c | -11.79543 | -57.01654 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce1458ff-0c9a-3937-b7cf-7e50ab758925 | -16.16165 | -58.47354 | 2026-05-28 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 707d43cb-fcd8-314a-bd64-fb13865800ed | -13.3728 | -54.27084 | 2026-05-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc13e689-351d-3353-9576-1aff2f7a76d4 | -13.20475 | -54.50767 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10977c27-d604-3686-8819-b44b93516926 | -11.72268 | -56.84068 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e369ad6-d96d-3c04-800c-9fee4928bdad | -11.93617 | -57.04042 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a843a62-7ea3-3a64-a614-7d24537a0ef3 | -12.54933 | -54.58251 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34dad2ac-6e6c-3c90-b889-ee39fcfc37d7 | -13.19956 | -54.5159 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34244067-b410-3f93-8683-8b6c086fc085 | -17.93363 | -51.33038 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 74c9d184-475e-332b-b0e3-f87b67633f91 | -13.22017 | -54.50587 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fde3dfa4-0309-3b55-a312-38b6dab9a5b5 | -14.06836 | -47.55036 | 2026-05-28 04:42:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae8de808-18fc-34ed-9742-d38d6af99629 | -13.2179 | -54.51919 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c5cc604-6a03-3044-a3fc-b39464aa208f | -13.2055 | -54.50327 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 852f7ad7-1096-317c-9d42-e4e26b8715f3 | -17.71448 | -53.28402 | 2026-05-28 04:42:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cec1d43-35e9-3acc-b8a8-6a4712805559 | -13.20399 | -54.51209 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88494269-0ab8-35cf-a6d2-ddc3c7e9dc38 | -13.65666 | -55.29646 | 2026-05-28 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6daa8b6d-d7b7-3996-85f6-b1a60bff1e99 | -13.20247 | -54.52098 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e385fb6-100d-361a-809a-141d18a73115 | -11.79957 | -57.35238 | 2026-05-28 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aafa081-2aa8-30f6-a61c-261de0067d5b | -11.93103 | -57.04393 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae95b15c-3d08-3b40-9a66-85432f855b17 | -13.20917 | -54.50391 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0fd475a1-915a-37b2-afe8-053e58e88ffe | -13.65286 | -55.29576 | 2026-05-28 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12f30a87-ba51-391c-8785-0563f217d702 | -11.72192 | -56.84494 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 392cc015-e2c3-3930-8b42-4e26a6fb9c85 | -13.218 | -54.49642 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f0c9dd4-de90-3706-9d8f-9c80546d146c | -17.93197 | -51.34127 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4adf3548-3a75-307e-908d-d4eceab3a5ce | -13.20183 | -54.50262 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| faec11e4-2bc2-3a7c-ac1e-176b1af0501d | -13.22167 | -54.49707 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a4650cd-0a64-3239-939c-56291462afaa | -11.63694 | -56.86172 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 849a35d9-cbe5-382e-b594-acf8f09c73ab | -13.22608 | -54.49334 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ed060aa-79e0-3826-9daf-f145ac0e5af7 | -17.93529 | -51.34182 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59303c15-1d4b-36b5-8396-679631b00a05 | -16.16611 | -58.47441 | 2026-05-28 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 35800028-60d7-3cae-be32-5a45e210acf5 | -12.54263 | -57.19851 | 2026-05-28 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43733ca2-a806-3124-b4a4-285d1f079e17 | -11.79184 | -57.01139 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c045ea82-be09-329c-9e30-7c51023a30fd | -17.92762 | -51.32602 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 87cf60cd-cd45-3173-8aeb-c77b83117d56 | -13.22092 | -54.50146 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ab9ea8fd-11e3-3223-afdf-3639ae2e28be | -14.4753 | -47.89567 | 2026-05-28 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48fee396-7f5a-3c12-ab06-f203cba869aa | -13.22533 | -54.49773 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6b60311-185a-31cc-ab57-40b57b89cca4 | -14.15346 | -45.27761 | 2026-05-28 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6651d32-ee5e-3245-a582-eabd4f0d039d | -13.21284 | -54.50456 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2358fbce-40b5-375f-befb-53aa232e58c7 | -14.78514 | -45.62129 | 2026-05-28 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d65de11d-53c1-3466-9653-3f66f4ab4d63 | -11.80604 | -57.3561 | 2026-05-28 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7447f065-715d-385a-bdcc-54f4aeea8d24 | -17.92927 | -51.33745 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ebdbcbe-33bd-3c64-9213-677d7711fb42 | -12.55833 | -48.35463 | 2026-05-28 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6914130e-7de2-37d6-9537-5041d85e2f9d | -11.9354 | -57.04474 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fea9b65-aaef-3389-a206-6d53961e0047 | -13.22156 | -54.51987 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 564982f4-ee30-3219-8d7c-93a443172257 | -17.93087 | -51.34852 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54ce390d-a732-3474-af3d-8448005b31cf | -11.9318 | -57.03959 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fe7f697b-a18e-3294-bb04-2696b933bd06 | -13.22383 | -54.50655 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 519206e0-cb46-3009-bf28-3aa1547aee26 | -17.9254 | -51.34053 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79857c45-cfc5-3337-8d06-0a4605583393 | -13.21423 | -54.51852 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a37a157-9e18-3859-9654-89a84cad7838 | -13.21875 | -54.49204 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6219591f-08ca-3e9a-8aab-5955a938222f | -13.22241 | -54.49269 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fdfe07ab-60a0-381e-a358-c64038084a65 | -13.20323 | -54.51653 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7b98f31-8ac7-378d-aefd-9db5069d7797 | -17.31643 | -49.91255 | 2026-05-28 04:42:00 | NOAA-21 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3aee375-7463-313d-b6e8-be74abacd57d | -11.80156 | -57.3553 | 2026-05-28 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5247c398-67c1-3a0e-869e-686c6df3bf19 | -13.20766 | -54.51274 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3906b645-367e-39a5-b6ca-85e6a14fd4b3 | -14.78464 | -45.62511 | 2026-05-28 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19e7664e-5aa6-317a-80be-3b63812ecde5 | -13.22458 | -54.50213 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75022bd0-aaa1-38e3-a5c3-cad4a2339a6b | -12.55068 | -49.90365 | 2026-05-28 04:42:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c839ed3d-dad3-3164-bd5a-d3cfc644d617 | -12.54341 | -57.19419 | 2026-05-28 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16108db8-a2fa-3164-a91d-18abf94c023f | -13.21499 | -54.51406 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09fa6b3a-f2ff-387c-9613-16ce4f29442f | -13.21725 | -54.50082 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 49993c96-1b9c-3b26-8fb1-ad5183a5a8a2 | -16.16078 | -58.4782 | 2026-05-28 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5dfe35ac-b4bc-3429-9688-9b7ec1623525 | -13.2165 | -54.50521 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d3f0775b-ab16-366e-83fb-93fd126292e3 | -13.22824 | -54.50281 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7c1b4c5-f472-3cf8-a9c7-8f78ebbe5b55 | -14.39678 | -43.52052 | 2026-05-28 04:42:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c447f5e-69f6-3010-8154-2f9947708b77 | -12.72395 | -54.19654 | 2026-05-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19f3228c-0a66-3eae-91f7-f832df876bde | -11.80406 | -57.35315 | 2026-05-28 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca2aff7d-0132-36e9-ba16-51f3056e0221 | -12.54185 | -57.20282 | 2026-05-28 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a43872e-7afc-3d45-98a2-a678c27e1379 | -12.72541 | -54.1879 | 2026-05-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3d6f30f-f5b7-35e1-8cdc-e5615e3d137b | -17.93694 | -51.33093 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4aff1ca5-b3a0-3c20-8c3a-0b2d857030b3 | -17.882 | -51.75606 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a222384-c415-32db-9aa0-df4f0b889570 | -17.93038 | -51.3302 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c87c2f1-6f44-3f44-a0e3-dd1d63ce63f9 | -16.21842 | -59.66661 | 2026-05-28 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c520007-9262-322e-8feb-46e3c1fdd216 | -13.22232 | -54.51542 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ffe8443-e097-313c-bba9-09848b6e5007 | -12.51465 | -48.27692 | 2026-05-28 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efd56f18-e79a-3379-8fb7-56b0747c0643 | -13.94964 | -53.8678 | 2026-05-28 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1e9b2ec-81ce-3b72-84e6-e28d5dc1f561 | -13.22308 | -54.51098 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6941692a-2521-35ed-abd2-71f42e8baf5a | -11.72776 | -56.83727 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5af3681-2c45-37d8-89bc-f597c3f08132 | -13.22899 | -54.4984 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bab85810-a326-3339-b7a2-63581bacf755 | -11.44974 | -55.11055 | 2026-05-28 04:42:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7bf000b-41d7-338f-88d9-94159f620272 | -14.07263 | -47.54657 | 2026-05-28 04:42:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f144ab4e-bcda-367c-abb7-842e13fa4ac6 | -17.93418 | -51.32675 | 2026-05-28 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README10.md)
