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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fd30a84-f90b-30ed-ae1e-4cf3b7af7eb0 | -16.1003 | -50.302601 | 2024-10-02 01:23:44 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff2b8cfc-9a27-3ada-bebd-69eb576b7c55 | -16.103201 | -50.3139 | 2024-10-02 01:23:44 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0938f968-1d2f-3d1d-b3cc-1bd050a741bc | -16.0905 | -50.305199 | 2024-10-02 01:23:44 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5abd467f-30b5-3d7c-bbbf-fb16e951269b | -16.093399 | -50.316502 | 2024-10-02 01:23:44 | METOP-C | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cc346d86-cec4-3634-a99e-78c0b2030ea3 | -16.0797 | -50.344398 | 2024-10-02 01:23:44 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8bd4bd34-0685-3c3f-b169-cab19e86ad41 | -16.066 | -50.3722 | 2024-10-02 01:23:44 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| accd2534-5ca2-3182-9f2a-7a208ba3ddde | -14.557 | -44.8241 | 2024-10-02 01:23:45 | METOP-C | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9cb2f2e9-a22a-3420-8d3b-6e3dc659878e | -14.5666 | -44.821201 | 2024-10-02 01:23:45 | METOP-C | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 56cba70e-e906-362e-904c-d7bcff967842 | -17.2271 | -56.1637 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7b5ede1e-6853-3e96-8810-04124332ba1e | -17.228701 | -56.170898 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0a2c1da8-897f-30a1-a46e-355aa14867ce | -17.2174 | -56.166 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2b25aec8-e9e7-3715-8b22-7eac9061e4ea | -17.219 | -56.173199 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 16e8b3be-9a61-30f6-8ae2-ad77d6a47749 | -17.2206 | -56.180401 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7df07db2-a348-330b-863a-74000f1ff4c2 | -17.2012 | -56.1395 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a648eae8-19e1-3680-8777-2769f14a2fd6 | -17.202801 | -56.146702 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d4db9bd7-1ea7-3352-bced-d82728f5b0ec | -17.204399 | -56.1539 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 75b6f6df-48e2-387e-8efd-a30608c7d835 | -17.205999 | -56.161098 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 253335dd-cf5e-3481-9904-1e50c51648aa | -17.2076 | -56.168301 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 52617da5-1af3-3c71-92ac-1f99772dbc91 | -17.193001 | -56.148998 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5982e147-ef06-38f3-aeb5-dfa024cb24ab | -17.1978 | -56.170601 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c5555816-48ea-3f2a-b9a1-9f7ed97c1efc | -17.1994 | -56.177799 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d12527dd-ca46-3195-8fc8-9d6c4751b212 | -17.201 | -56.185001 | 2024-10-02 01:23:48 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2b3e3105-c42e-35c3-adb1-8d49d4ff2e30 | -17.2026 | -56.1922 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40795afa-d534-36e7-adcd-2eb10031d9c9 | -17.2041 | -56.199299 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e1b31ce1-1d44-399c-9389-00b81b0ce6a4 | -17.2057 | -56.206501 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 56632883-3cfb-3c5d-a59b-f2b60146ebbc | -17.2073 | -56.213699 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fdc498bd-c5e4-31ec-b1f5-c01fbe82a00a | -17.2089 | -56.220901 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| de4594ea-7a93-3421-849b-691931186ef8 | -17.210501 | -56.228199 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 710b533b-8930-3e80-964d-a4690684ef1b | -17.212099 | -56.235401 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 725762f9-d6aa-37b7-af3e-da8403ac9d1d | -17.183201 | -56.151299 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a8306abe-abe7-3219-ada6-af84add00cfa | -17.186399 | -56.165699 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1998453-3900-3b47-a502-0269d9b1d227 | -17.188 | -56.172901 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 140f1909-3f48-3351-89c6-a8a73efb0345 | -17.1896 | -56.180099 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e4f045ac-bf3f-3847-acfb-e20133d873f0 | -17.1912 | -56.187302 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c73e6f83-89ca-361c-950d-24ca3d2bcc63 | -17.192801 | -56.1945 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ad279961-ffc1-3db2-9f90-af53f530f799 | -17.1943 | -56.201599 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a7c30c6-8e7e-3583-801e-9fae55ac5127 | -17.1959 | -56.208801 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f9b6d2a-a65b-30fa-a25f-3fdaa28c791f | -17.1975 | -56.216 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 916253cd-16a4-3add-8a36-c86675da65c7 | -17.1991 | -56.223202 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f518ff60-9049-3cdf-9e3f-1d8f652de045 | -17.200701 | -56.230499 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 847cbc25-b196-3879-ba5a-c4c0323b96c9 | -17.202299 | -56.237701 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 115a283e-7a85-38f3-86f9-ca274bcd7ae6 | -17.203899 | -56.2449 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2632e33-651a-36de-bb0d-7bb4c66a92d1 | -17.2054 | -56.252102 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 56b28739-d84d-3f2c-b840-367a78ec5227 | -17.207001 | -56.2593 | 2024-10-02 01:23:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b230813-6395-3bef-9303-e06a44a693a0 | -17.1782 | -56.175098 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 43c9243c-4751-306a-a421-b6c64b6b074e | -17.1798 | -56.182301 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 79bb4245-7bdc-32b3-b663-7c97c152b5cb | -17.1814 | -56.189499 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c60d6de7-7b3c-32ef-8444-aff73a6880bd | -17.183001 | -56.196701 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8d10a7d8-10ab-33e5-ac96-cbe44cedf46c | -17.1845 | -56.203899 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 585ad0b6-c745-30df-84df-fbed8a2caba7 | -17.1861 | -56.211102 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e14d64b6-449f-37d4-9867-199cfc5e3628 | -17.1877 | -56.2183 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 09110ca4-19c0-36aa-8424-da2276d78599 | -17.189301 | -56.225498 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 265af0f9-6652-36d7-8c42-48620659fc7b | -17.190901 | -56.2327 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4eed012d-08a3-3bf1-b528-5db5cefe8a30 | -17.192499 | -56.239899 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 572d0479-d9ad-3cc5-8af7-8a9c43e72b5e | -17.194099 | -56.247101 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8e7ca5b6-200c-3941-aa24-645b306a6ae0 | -17.195601 | -56.254299 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 038df222-cd7f-3bb6-ab3c-f64fc12a2ea5 | -17.197201 | -56.261501 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7110be14-7917-3dcb-9971-c72e179def3a | -17.1763 | -56.213299 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f1d25c77-49b6-3a13-b0d1-abafdc7c5675 | -17.1779 | -56.220501 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2bff5e43-6b87-3722-a65f-3222f070c396 | -17.179501 | -56.227699 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a0e7a15-6e94-3df9-81ca-cc7665784b3e | -17.184299 | -56.249401 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fb9e8dfd-69d1-3a98-83f9-6859059ef6c2 | -17.185801 | -56.256599 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3af0f92a-df00-30ea-8261-8d22d8c010e7 | -17.187401 | -56.263802 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f827c8e2-0bc4-3561-9319-da677c1187b4 | -17.188999 | -56.271 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b6777877-347b-35cf-af36-b3cc43f6c267 | -17.190599 | -56.278198 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae693333-3b34-3d3c-9bb8-7ad464e2ff4d | -17.1922 | -56.2854 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a5c8f014-4cc9-334d-bf3e-2cd613e32193 | -17.1938 | -56.292599 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 15d214a8-f74f-323e-b564-3114d0a21979 | -17.1539 | -56.1581 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9661f377-53ac-3f76-839c-a59720208f72 | -17.1555 | -56.165298 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 05b75370-8f9e-399b-b58a-7803ae561669 | -17.157101 | -56.172501 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b07186a2-c3df-3f4f-87a7-8f7a4163daf8 | -17.158701 | -56.179699 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e815e0db-146e-3ea3-8402-2a37d4e4cc65 | -17.1635 | -56.201302 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cae95f9e-c25d-3260-8694-eafa03f29651 | -17.165001 | -56.208401 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 570abd1c-71d4-3bbd-8a8d-3e7ed0f9c7a7 | -17.166599 | -56.215599 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a321aa13-8c94-34fb-ade6-7046973c3592 | -17.1745 | -56.251701 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 887feb08-133b-38bf-9e65-f9ba92990fd0 | -17.1761 | -56.2589 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a42515d-7656-3762-b6d2-99af2d207016 | -17.1777 | -56.266102 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 24349216-d8d5-3251-a95f-14ea339638eb | -17.1793 | -56.2733 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 56874ed8-3050-31f1-b569-e255d5dc6430 | -17.180901 | -56.280499 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1e9118f1-80e1-32d0-a868-15ab0a2706d7 | -17.1457 | -56.167599 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| abd771eb-dcf6-3df1-bd37-3a3d0fe163d0 | -17.147301 | -56.174801 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| edf3b81e-e28c-31d5-8e53-b82740ee3ed9 | -17.148899 | -56.181999 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c44e45b7-5d05-3b56-9381-7f20bb931e8e | -17.150499 | -56.189201 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 158cd1a7-bb9e-3c9b-84d6-74df0e0222bc | -17.1521 | -56.1964 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 974da36d-5f9b-3b11-ab63-e906eb4c2f8c | -17.1537 | -56.203602 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dec2c0b3-6f9a-320d-bd13-b0f399ceeb22 | -17.155199 | -56.210701 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 692b980e-4527-3987-822a-4600d5a5945c | -17.137501 | -56.177101 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b8092d7a-c514-3b55-8994-0a5a322a75b9 | -17.139099 | -56.184299 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 80beba32-5eb1-39d0-b369-e8168113d9fb | -17.140699 | -56.191502 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 092ddff0-3326-3f42-b21b-e2d3ce637a59 | -17.1087 | -56.093201 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 43560808-47d5-3878-a1bf-d91c8707d86a | -17.110201 | -56.100399 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cc8ef114-7920-39c8-8a03-f990d1577d28 | -17.111799 | -56.107498 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6461f784-d186-37e2-8f97-9888f6aac200 | -17.1134 | -56.1147 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0d41ff56-f863-3b8a-9b67-5bbe78a864c7 | -17.1166 | -56.129101 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6ba3bb93-ac2b-387d-8bc4-17df0c23a2d5 | -17.127701 | -56.179401 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7b414501-5a7e-331d-a0ef-a362f9c26117 | -17.129299 | -56.1866 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fbd2812e-8f4b-3f09-aba6-874eb0815eeb | -17.130899 | -56.193802 | 2024-10-02 01:23:49 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6567126d-9cff-3a9b-b367-0feb7776ff6f | -17.0989 | -56.095501 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a74576ba-e861-39ef-baa3-eb9f6d3c5ee2 | -17.100401 | -56.102699 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f9fe0927-92bd-3fae-b00a-71abfcc22f1e | -17.101999 | -56.109798 | 2024-10-02 01:23:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README22.md)
